# EXP-0013 — Pilot result

Status: EXECUTED / PILOT — NOT A VALIDATED RESULT
Seeds: 20

The isolated implementation was executed locally from the experimental branch. No canonical repository was modified.

| Agent | Adaptation mean* | Reward mean | False-switch mean | Revisions mean | Unnecessary checks mean | Transfer mean |
|---|---:|---:|---:|---:|---:|---:|
| B_memory | 1.35 | 358.15 | 1.05 | 0.00 | 0.00 | 5.00 |
| C_affect_action | 3.84 | 112.45 | 2.00 | 0.00 | 0.00 | -0.85 |
| D_metacontrol | 5.35 | 346.90 | 1.55 | 1.20 | 2.50 | 5.00 |

*Mean adaptation is calculated only over seeds that reached the criterion; C reached it on 19/20 seeds. B and D reached it on 20/20.

## Interpretation

This pilot does **not** validate the metacontrol hypothesis. D was slower than B and had lower cumulative reward, while C performed substantially worse. The implementation therefore does not yet provide evidence that routing surprise into model-checking improves the tested task.

More importantly, the pilot exposed a protocol/design problem: the current environment and update rule allow B to switch rapidly after a single negative outcome, so the intended distinction between robust model checking and simple memory revision is not cleanly isolated.

Classification: **INCONCLUSIVE — PROTOCOL REQUIRES REVISION**.

This is evidence about the pilot implementation only. It is not a canonical architectural claim.
