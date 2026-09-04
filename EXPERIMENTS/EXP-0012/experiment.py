"""Temporary, disposable organisms for EXP-0012.

This module is experimental evidence machinery only. It must not be promoted to
--AGI or Space without a separate proposal and independent validation.
"""
from dataclasses import dataclass
import random
from typing import Dict, Tuple


def clip(x: float, lo: float = -1.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


@dataclass(frozen=True)
class Step:
    relation: int
    context: int
    phase: str


class DeterministicWorld:
    """Two-action world with a hidden rule that flips after training.

    Observation contains only relation and context. The optimal action is the
    relation before the switch and its inverse after the switch. Transfer uses
    unseen context IDs while preserving the learned relation.
    """

    def __init__(self, seed: int, train_steps: int = 80, switch_steps: int = 80, transfer_steps: int = 40):
        self.seed = seed
        self.rng = random.Random(seed)
        self.train_steps = train_steps
        self.switch_steps = switch_steps
        self.transfer_steps = transfer_steps
        self.total_steps = train_steps + switch_steps + transfer_steps
        self.t = 0

    def observation(self) -> Step:
        if self.t < self.train_steps:
            phase, context_base = "train", 0
        elif self.t < self.train_steps + self.switch_steps:
            phase, context_base = "switch", 0
        else:
            phase, context_base = "transfer", 10
        relation = self.t % 2
        context = context_base + (self.t % 2)
        return Step(relation=relation, context=context, phase=phase)

    def correct_action(self, obs: Step) -> int:
        return obs.relation if obs.phase == "train" else 1 - obs.relation

    def step(self, action: int) -> Tuple[Step, float, bool]:
        obs = self.observation()
        reward = 1.0 if action == self.correct_action(obs) else -1.0
        self.t += 1
        return obs, reward, self.t >= self.total_steps


class ReactiveAgent:
    """A: reactive baseline; no persistent learning state."""

    name = "A_reactive"

    def __init__(self, seed: int):
        self.seed = seed

    def act(self, obs: Step) -> int:
        return obs.relation

    def observe(self, obs: Step, action: int, reward: float) -> None:
        pass


class MemoryAgent:
    """B: memory baseline with the same observable input and action space."""

    name = "B_memory"

    def __init__(self, seed: int, epsilon_start: float = 0.40, epsilon_min: float = 0.02, decay: float = 0.985):
        self.rng = random.Random(seed)
        self.epsilon = epsilon_start
        self.epsilon_min = epsilon_min
        self.decay = decay
        self.alpha = 0.20
        self.q: Dict[int, list[float]] = {0: [0.0, 0.0], 1: [0.0, 0.0]}

    def exploration_probability(self) -> float:
        return self.epsilon

    def act(self, obs: Step) -> int:
        if self.rng.random() < self.epsilon:
            return self.rng.randrange(2)
        q = self.q[obs.relation]
        return 0 if q[0] >= q[1] else 1

    def observe(self, obs: Step, action: int, reward: float) -> None:
        self.q[obs.relation][action] += self.alpha * (reward - self.q[obs.relation][action])
        self.epsilon = max(self.epsilon_min, self.epsilon * self.decay)


class OrganismAgent(MemoryAgent):
    """C: memory baseline plus bounded motivational-affective state.

    Affect is not an additional information channel: all variables are derived
    only from the same prediction error/reward already available to B.
    """

    name = "C_organism"

    def __init__(self, seed: int, affect_enabled: bool = True):
        super().__init__(seed)
        self.affect_enabled = affect_enabled
        self.interest = 0.0
        self.tension = 0.0
        self.satisfaction = 0.0
        self.uncertainty = 0.0
        self.significance = 0.0

    def exploration_probability(self) -> float:
        if not self.affect_enabled:
            return self.epsilon
        bonus = 0.55 * max(self.tension, self.uncertainty) + 0.10 * self.interest
        return min(0.95, self.epsilon + bonus)

    def act(self, obs: Step) -> int:
        if self.rng.random() < self.exploration_probability():
            return self.rng.randrange(2)
        q = self.q[obs.relation]
        return 0 if q[0] >= q[1] else 1

    def observe(self, obs: Step, action: int, reward: float) -> None:
        prediction = self.q[obs.relation][action]
        error = reward - prediction
        super().observe(obs, action, reward)
        if not self.affect_enabled:
            return
        magnitude = abs(error)
        self.tension = clip(0.70 * self.tension + 0.60 * magnitude)
        self.uncertainty = clip(0.80 * self.uncertainty + 0.40 * magnitude)
        self.satisfaction = clip(0.70 * self.satisfaction + 0.30 * reward)
        self.interest = clip(0.90 * self.interest + 0.30 * magnitude)
        self.significance = clip(0.80 * self.significance + 0.50 * magnitude)
