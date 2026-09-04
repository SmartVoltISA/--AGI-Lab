"""Paired ablation: C with affect enabled vs the same organism with affect disabled."""
import json
import statistics
from pathlib import Path

from experiment import DeterministicWorld, OrganismAgent

SEEDS = list(range(20))


def run(seed, affect_enabled):
    world = DeterministicWorld(seed)
    agent = OrganismAgent(seed, affect_enabled=affect_enabled)
    rows = []
    while True:
        obs = world.observation()
        p = agent.exploration_probability()
        action = agent.act(obs)
        obs, reward, done = world.step(action)
        agent.observe(obs, action, reward)
        rows.append((reward, p, action))
        if done:
            break
    switch = 80
    transfer = 160
    rewards = [x[0] for x in rows]
    return {
        "seed": seed,
        "adaptation": _adaptation(rewards[switch:transfer]),
        "reward": sum(rewards),
        "switch_error": sum(r < 0 for r in rewards[switch:transfer]) / 80,
        "transfer_accuracy": sum(r > 0 for r in rewards[transfer:]) / 40,
        "trace": rows,
    }


def _adaptation(rewards, window=8):
    for i in range(len(rewards) - window + 1):
        if sum(r > 0 for r in rewards[i:i + window]) / window >= 0.75:
            return i
    return None


def main():
    on = [run(s, True) for s in SEEDS]
    off = [run(s, False) for s in SEEDS]
    paired = []
    for a, b in zip(on, off):
        paired.append({
            "seed": a["seed"],
            "adaptation_delta_on_minus_off": (a["adaptation"] - b["adaptation"]) if a["adaptation"] is not None and b["adaptation"] is not None else None,
            "reward_delta_on_minus_off": a["reward"] - b["reward"],
            "switch_error_delta_on_minus_off": a["switch_error"] - b["switch_error"],
            "transfer_delta_on_minus_off": a["transfer_accuracy"] - b["transfer_accuracy"],
            "trace_identical_when_affect_disabled": a["trace"] == b["trace"] if not a["trace"] else None,
        })
    payload = {
        "experiment": "EXP-0012-ABLATION",
        "status": "EXECUTED",
        "seeds": SEEDS,
        "paired": paired,
        "summary": {
            "adaptation_delta_mean": statistics.mean(x["adaptation_delta_on_minus_off"] for x in paired if x["adaptation_delta_on_minus_off"] is not None),
            "reward_delta_mean": statistics.mean(x["reward_delta_on_minus_off"] for x in paired),
            "switch_error_delta_mean": statistics.mean(x["switch_error_delta_on_minus_off"] for x in paired),
            "transfer_delta_mean": statistics.mean(x["transfer_delta_on_minus_off"] for x in paired),
            "disabled_trace_identity_rate": statistics.mean(1.0 if x["trace_identical_when_affect_disabled"] else 0.0 for x in paired),
        },
    }
    path = Path("RESULTS/EXP-0012/ablation_results.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = payload["summary"]
    Path("RESULTS/EXP-0012/ABLATION_SUMMARY.md").write_text(
        "# EXP-0012 — Affect ablation\n\n"
        f"Status: {payload['status']}\nSeeds: {len(SEEDS)}\n\n"
        f"Adaptation delta (C_on − C_off): {summary['adaptation_delta_mean']:.3f} steps\n\n"
        f"Reward delta (C_on − C_off): {summary['reward_delta_mean']:.3f}\n\n"
        f"Switch error delta: {summary['switch_error_delta_mean']:.3f}\n\n"
        f"Transfer delta: {summary['transfer_delta_mean']:.3f}\n\n"
        f"Disabled-affect trace identity rate: {summary['disabled_trace_identity_rate']:.3f}\n\n"
        "Ablation is evidence about causal contribution of the affective modulation; it is not a canonical architectural claim.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
