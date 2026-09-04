"""Run EXP-0012 and emit machine-readable raw observations and metrics."""
import argparse
import json
from pathlib import Path
import statistics

from experiment import DeterministicWorld, ReactiveAgent, MemoryAgent, OrganismAgent

SEEDS = list(range(20))
AGENT_FACTORIES = {
    "A_reactive": ReactiveAgent,
    "B_memory": MemoryAgent,
    "C_organism": OrganismAgent,
}


def adaptation_time(phases, rewards, switch_index, window=8, threshold=0.75):
    for i in range(switch_index, len(rewards) - window + 1):
        if phases[i] != "switch":
            continue
        acc = sum(1 for r in rewards[i:i + window] if r > 0) / window
        if acc >= threshold:
            return i - switch_index
    return None


def run_one(agent_name, seed):
    world = DeterministicWorld(seed)
    if agent_name == "A_reactive":
        agent = ReactiveAgent(seed)
    elif agent_name == "B_memory":
        agent = MemoryAgent(seed)
    else:
        agent = OrganismAgent(seed)

    rows = []
    while True:
        obs_before = world.observation()
        p = agent.exploration_probability() if hasattr(agent, "exploration_probability") else 0.0
        action = agent.act(obs_before)
        obs, reward, done = world.step(action)
        agent.observe(obs, action, reward)
        rows.append({
            "t": world.t - 1,
            "phase": obs.phase,
            "relation": obs.relation,
            "context": obs.context,
            "action": action,
            "reward": reward,
            "exploration_probability": p,
        })
        if done:
            break

    rewards = [r["reward"] for r in rows]
    phases = [r["phase"] for r in rows]
    switch_index = phases.index("switch")
    transfer_index = phases.index("transfer")
    transfer_rewards = rewards[transfer_index:]
    return {
        "agent": agent_name,
        "seed": seed,
        "adaptation_time_steps": adaptation_time(phases, rewards, switch_index),
        "cumulative_reward": sum(rewards),
        "switch_error_rate": sum(1 for r in rewards[switch_index:transfer_index] if r < 0) / (transfer_index - switch_index),
        "transfer_accuracy": sum(1 for r in transfer_rewards if r > 0) / len(transfer_rewards),
        "exploration_after_switch_mean": statistics.mean(r["exploration_probability"] for r in rows[switch_index:transfer_index]),
        "final_affect": {
            k: getattr(agent, k) for k in ("interest", "tension", "satisfaction", "uncertainty", "significance") if hasattr(agent, k)
        },
        "raw": rows,
    }


def summarize(runs):
    out = {}
    for agent in sorted({r["agent"] for r in runs}):
        rs = [r for r in runs if r["agent"] == agent]
        vals = [r["adaptation_time_steps"] for r in rs if r["adaptation_time_steps"] is not None]
        out[agent] = {
            "n": len(rs),
            "adaptation_time_mean": statistics.mean(vals) if vals else None,
            "adaptation_time_median": statistics.median(vals) if vals else None,
            "adaptation_success_rate": len(vals) / len(rs),
            "cumulative_reward_mean": statistics.mean(r["cumulative_reward"] for r in rs),
            "switch_error_rate_mean": statistics.mean(r["switch_error_rate"] for r in rs),
            "transfer_accuracy_mean": statistics.mean(r["transfer_accuracy"] for r in rs),
            "exploration_after_switch_mean": statistics.mean(r["exploration_after_switch_mean"] for r in rs),
        }
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    runs = [run_one(agent, seed) for seed in SEEDS for agent in AGENT_FACTORIES]
    payload = {
        "experiment": "EXP-0012",
        "status": "EXECUTED",
        "protocol": "EXP-0012_EMOTIONAL_MOTIVATION_LOOP.md",
        "seeds": SEEDS,
        "agents": list(AGENT_FACTORIES),
        "summary": summarize(runs),
        "runs": runs,
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
