import json
import sys
from pathlib import Path

p = Path(sys.argv[1])
data = json.loads(p.read_text(encoding="utf-8"))
lines = [
    "# EXP-0012 — Primary result",
    "",
    f"Status: {data['status']}",
    f"Seeds: {len(data['seeds'])}",
    "",
    "| Agent | Adaptation mean | Success rate | Reward mean | Switch error | Transfer |",
    "|---|---:|---:|---:|---:|---:|",
]
for name, s in data["summary"].items():
    lines.append(
        f"| {name} | {s['adaptation_time_mean']} | {s['adaptation_success_rate']:.3f} | "
        f"{s['cumulative_reward_mean']:.2f} | {s['switch_error_rate_mean']:.3f} | "
        f"{s['transfer_accuracy_mean']:.3f} |"
    )
lines += ["", "This file is derived from the machine-readable raw result; it is not a canonical architectural claim."]
Path("RESULTS/EXP-0012/PRIMARY_SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
