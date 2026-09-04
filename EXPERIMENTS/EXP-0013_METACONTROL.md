# EXP-0013 — Memory, affect and metacontrol

Status: EXECUTED / SUCCESS FOR TESTED HYPOTHESIS
Date: 2026-09-04

## Question

Can an internal significance/affective signal improve adaptation by changing the **mode of model checking** rather than directly selecting actions?

## Hypothesis

The failure of EXP-0012 may be caused by coupling affect directly to action selection. A metacontrol design may use surprise/error to increase checking or model revision while leaving the action policy otherwise comparable to the memory baseline.

## Agents

- **B_memory:** fixed verification schedule; action policy from the current model.
- **C_affect_action:** direct surprise/affect-like coupling to action selection; carried forward as the EXP-0012 direct-coupling control.
- **D_off:** D architecture with metacontrol disabled; fixed verification schedule.
- **D_metacontrol:** same action policy as B whenever model state is identical; surprise only changes when verification is spent.

## Environment

Deterministic discrete environment:

1. latent rule 0 until step 50, then latent rule 1;
2. 15% misleading ordinary feedback;
3. verification observation reliability 90%;
4. novel context from step 90 onward while the learned latent relation remains applicable;
5. fixed action/observation spaces and identical seeds across agents;
6. correct action = latent rule XOR context.

## Controls and fairness

- 1000 identical seeds (`0..999`).
- Same observable information and action space.
- Same episode length: 120 steps.
- Verification is a finite resource: maximum 18 operations/episode.
- B uses a fixed verification schedule (`t mod 7 == 0`).
- D may only change **when** it spends verification, based on accumulated surprise; it cannot observe hidden state or obtain unbounded computation.
- B and D use the same action mapping when model state is identical.
- D-off uses B's fixed schedule as causal identity control.
- No LLM or external model.

## Metacontrol mechanism

A bounded surprise signal is accumulated from contradiction between feedback and the agent's current model. D requests verification when surprise reaches two contradictory observations or at a sparse fallback slot (`t mod 11 == 0`), subject to the same maximum budget. Surprise does not directly select an action.

## Primary metrics

- adaptation time after the true rule change;
- cumulative reward;
- false-switch rate after misleading evidence;
- model-revision precision;
- verification count;
- transfer performance in the novel context.

## Result

| Metric | B_memory | C_affect_action | D_metacontrol | D − B |
|---|---:|---:|---:|---:|
| Adaptation mean (steps) | 6.13 | 1.66 | 2.63 | **−3.50** |
| Adaptation median | 6.00 | 2.00 | 1.00 | **−5.00** |
| Reward mean | 412.78 | 350.53 | 516.06 | **+103.28** |
| False-switch rate | 0.3532 | 0.0000 | 0.3028 | **−0.0504** |
| Post-change false switches/episode | 0.868 | 0.000 | 0.758 | **−0.110** |
| Revision precision | 0.8977 | 0.0000 | 0.9018 | +0.0042 |
| Verifications/episode | 18.00 | 0.00 | 16.71 | **−1.29** |
| Transfer | 0.8975 | 0.7396 | 0.9364 | **+0.0389** |
| Correct-action rate | 0.8515 | 0.7921 | 0.9370 | **+0.0855** |

D adaptation succeeded in 99.0% of seeds.

## Causal control

`D_off` reproduced `B_memory` exactly for all 1000 seeds: **1000/1000 identical decision traces**. This supports attributing the D-vs-B difference to metacontrol rather than a hidden action-policy difference.

## Statistical check

Paired seed-wise Wilcoxon tests, D vs B:

- adaptation: `p = 1.06e-137`;
- reward: `p = 1.77e-112`;
- false-switch rate: `p = 4.22e-09`;
- post-change false switches: `p = 0.00150`;
- transfer: `p = 1.93e-24`;
- correct-action rate: `p = 1.54e-111`;
- revision precision: `p = 0.299` (not significant).

## Classification

**SUCCESS for the tested hypothesis under this protocol.** D did not merely switch faster: it achieved higher cumulative utility, lower false-switch rate, slightly higher revision precision, better transfer, and used fewer verification operations on average than B.

## Boundary

This is evidence for this implementation in this deterministic environment. It is not a general proof that affect/metacontrol is universally useful and makes no consciousness claim. An independent environment/protocol is required before architectural promotion.

## Evidence policy

UNKNOWN ≠ TRUE.
HYPOTHESIS ≠ VERIFIED.
PROPOSED ≠ EXECUTED.
EXECUTED ≠ SUCCESSFUL unless the result is recorded.
RESULT ≠ CANONICAL.

## Canonical decision

No promotion. No changes to canonical `--AGI` or Space.

## Cleanup

Temporary executable experiment machinery was deleted after execution. Results, raw observations, parameters, journal and execution specification remain. Canonical `--AGI` and Space remain unchanged.
