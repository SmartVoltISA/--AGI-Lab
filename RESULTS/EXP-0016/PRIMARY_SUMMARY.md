# EXP-0016 — Primary result

## Run

1000 seeds (`0..999`), 120 steps, same observation streams for B and D.

## Aggregate

| Metric | B_memory | D_adaptive | D − B | Paired p |
|---|---:|---:|---:|---:|
| Reward | 92.424 | 92.254 | -0.170 | 0.5239 |
| False switches | 8.825 | 5.318 | -3.507 | 4.84e-155 |
| First adaptation delay | 0.059 | 0.331 | +0.272 | 5.37e-55 |
| Second adaptation delay | 0.059 | 0.968 | +0.909 | 1.79e-124 |
| Correct-action rate | 0.89957 | 0.89960 | +0.00003 | 0.7876 |
| Model revisions | 19.386 | 12.461 | -6.925 | — |

Delays are measured from the true rule-change step to the first step at which the model equals the new rule. Episodes where adaptation was not achieved use the episode horizon as the censored value; none materially affected the reported means.

## Identity control

D_off with adaptive persistence disabled and threshold `1` matched B's decision path by construction/trace comparison. No hidden state or extra compute was supplied to D.

## Classification

**INCONCLUSIVE / PARTIAL SUPPORT.**

Adaptive persistence substantially reduced false switching, but the pre-registered policy did not recover the adaptation-speed cost and did not improve total reward. Correct-action rate was effectively unchanged. Therefore the hypothesis of a clear overall advantage is not supported.

## Architectural consequence

No canonical change or promotion. Evidence supports retaining **adaptive persistence as a robustness mechanism**, but not as a generally superior metacontrol policy. The next useful question is whether reliability estimation should distinguish abrupt regime changes from intermittent noise without using hidden state or post-hoc tuning.
