import json, random
from dataclasses import dataclass

SEEDS = range(20)
STEPS = 80
CHANGE_STEP = 30

@dataclass
class Result:
    adaptation: int | None
    reward: float
    false_switches: int
    revisions: int
    unnecessary_checks: int
    transfer_reward: float


def run(seed, mode):
    rng = random.Random(seed)
    # True rule: before change action 0 pays +5, action 1 pays -4.
    # After change action 1 pays +5, action 0 pays -4.
    # Between steps 30-44, 25% of observations are misleading. This creates
    # a genuine distinction between fast reaction and evidence-weighted revision.
    rule = 0
    remembered_rule = 0
    evidence_for_new = 0
    confidence = 0
    reward = 0.0
    adaptation = None
    false_switches = 0
    revisions = 0
    checks = 0
    unnecessary_checks = 0
    for t in range(STEPS):
        if t == CHANGE_STEP:
            rule = 1
        # Surprise is based on prediction error under remembered rule.
        expected = 5 if remembered_rule == rule else -4
        misleading = (t >= CHANGE_STEP and t < CHANGE_STEP + 15 and rng.random() < 0.25)
        observed_reward = expected
        if misleading:
            observed_reward = -expected
        surprise = abs(observed_reward - expected)

        if mode == 'B':
            action_rule = remembered_rule
            if t >= CHANGE_STEP and observed_reward < 0:
                remembered_rule = 1 - remembered_rule
            confidence = 0
        elif mode == 'C':
            # Direct affective response: a single surprising negative outcome
            # immediately pushes the policy to switch.
            action_rule = remembered_rule
            if t >= CHANGE_STEP and surprise:
                remembered_rule = 1 - remembered_rule
                confidence = 0
            else:
                confidence += 1
        else:  # D metacontrol
            action_rule = remembered_rule
            # Affect is a control signal, not an action selector. Surprise
            # increases checking; revision requires repeated supporting evidence.
            if surprise:
                confidence = 0
            else:
                confidence += 1
            check_depth = 1 + min(2, int(surprise > 0) + int(confidence < 3))
            checks += check_depth
            if t < CHANGE_STEP or t >= CHANGE_STEP + 15:
                unnecessary_checks += max(0, check_depth - 1)
            if t >= CHANGE_STEP:
                if observed_reward < 0:
                    evidence_for_new += 1
                else:
                    evidence_for_new = max(0, evidence_for_new - 1)
                if evidence_for_new >= 3:
                    remembered_rule = 1 - remembered_rule
                    revisions += 1
                    evidence_for_new = 0
                    confidence = 3

        actual_reward = 5 if action_rule == rule else -4
        reward += actual_reward
        if t >= CHANGE_STEP and adaptation is None and action_rule == rule:
            adaptation = t - CHANGE_STEP
        if t >= CHANGE_STEP and action_rule != rule and observed_reward > 0:
            false_switches += 1

    # Novel context: true rule remains changed. Evaluate without further training.
    transfer_reward = 5 if remembered_rule == rule else -4
    return Result(adaptation, reward, false_switches, revisions, unnecessary_checks, transfer_reward)


def aggregate(mode):
    rs = [run(s, mode) for s in SEEDS]
    return {
        'adaptation_mean': sum(r.adaptation for r in rs if r.adaptation is not None) / len(rs),
        'reward_mean': sum(r.reward for r in rs) / len(rs),
        'false_switch_mean': sum(r.false_switches for r in rs) / len(rs),
        'revisions_mean': sum(r.revisions for r in rs) / len(rs),
        'unnecessary_checks_mean': sum(r.unnecessary_checks for r in rs) / len(rs),
        'transfer_mean': sum(r.transfer_reward for r in rs) / len(rs),
        'raw': [r.__dict__ for r in rs],
    }

if __name__ == '__main__':
    print(json.dumps({m: aggregate(m) for m in ('B','C','D')}, indent=2))
