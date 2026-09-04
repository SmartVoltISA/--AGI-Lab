"""Paired ablation: C_on vs C_off, with B as an identity control."""
import json
import statistics
from pathlib import Path

from experiment import DeterministicWorld, MemoryAgent, OrganismAgent

SEEDS = list(range(20))


def run(seed, mode):
    world = DeterministicWorld(seed)
    if mode == "C_on":
        agent = OrganismAgent(seed, affect_enabled=True)
    elif mode == "C_off":
        agent = OrganismAgent(seed, affect_enabled=False)
    else:
        agent = MemoryAgent(seed)
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
    switch, transfer = 80, 160
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
    on = [run(s, "C_on") for s in SEEDS]
    off = [run(s, "C_off") for s in SEEDS]
    baseline = [run(s, "B") for s in SEEDS]
    paired = []
    for a, b, base in zip(on, off, baseline):
        paired.append({
            "seed": a["seed"],
            "adaptation_delta_on_minus_off": (a["adaptation"] - b["adaptation"]) if a["adaptation"] is not None and b["adaptation"] is not None else None,
            "reward_delta_on_minus_off": a["reward"] - b["reward"],
            "switch_error_delta_on_minus_off": a["switch_error"] - b["switch_error"],
            "transfer_delta_on_minus_off": a["transfer_accuracy"] - b["transfer_accuracy"],
            "off_equals_B_trace": b["trace"] == base["trace"],
        })
    summary = {
        "adaptation_delta_mean": statistics.mean(x["adaptation_delta_on_minus_off"] for x in paired if x["adaptation_delta_on_minus_off"] is not None),
        "reward_delta_mean": statistics.mean(x["reward_delta_on_minus_off"] for x in paired),
        "switch_error_delta_mean": statistics.mean(x["switch_error_delta_on_minus_off"] for x in paired),
        "transfer_delta_mean": statistics.mean(x["transfer_delta_on_minus_off"] for x in paired),
        "off_equals_B_trace_rate": statistics.mean(1.0 if x["off_equals_B_trace"] else 0.0 for x in paired),
    }
    payload = {"experiment": "EXP-0012-ABLATION", "status": "EXECUTED", "seeds": SEEDS, "paired": paired, "summary": summary}
    path = Path("RESULTS/EXP-0012/ablation_results.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    Path("RESULTS/EXP-0012/ABLATION_SUMMARY.md").write_text(
        "# EXP-0012 — Affect ablation\n\n"
        f"Status: {payload['status']}\nSeeds: {len(SEEDS)}\n\n"
        f"Adaptation delta (C_on − C_off): {summary['adaptation_delta_mean']:.3f} steps\n\n"
        f"Reward delta (C_on − C_off): {summary['reward_delta_mean']:.3f}\n\n"
        f"Switch error delta: {summary['switch_error_delta_mean']:.3f}\n\n"
        f"Transfer delta: {summary['transfer_delta_mean']:.3f}\n\n"
        f"C_off trace equals B trace: {summary['off_equals_B_trace_rate']:.3f}\n\n"
        "Ablation is evidence about causal contribution of affective modulation; it is not a canonical architectural claim.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
