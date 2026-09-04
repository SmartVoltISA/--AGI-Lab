# EXP-0014 — Metacontrol stress test

Status: EXECUTED / FAILURE FOR ROBUSTNESS CLAIM
Date: 2026-09-04

## Purpose

Independent challenge to EXP-0013. Test whether the apparent benefit of verification metacontrol survives repeated rule changes, bursty misleading evidence and imperfect verification.

## Environment

- 150-step deterministic episode;
- latent rule changes at steps 45 and 90;
- 15% ordinary misleading feedback;
- misleading-feedback bursts at steps 35–39 and 80–84 with 65% noise;
- verification reliability 80%;
- verification budget 18/episode;
- novel context from step 120;
- reward +5 correct / −5 incorrect;
- verification cost −0.5;
- 1000 identical seeds per agent.

## Agents

B uses fixed verification schedule `t mod 7 == 0`.

D uses the EXP-0013 metacontrol rule: accumulated contradiction triggers verification, with sparse fallback `t mod 11 == 0`, same finite budget.

C is a direct affect/action control and is included only as a reference.

## Results

| Metric | B_memory | C_affect_action | D_metacontrol | D − B |
|---|---:|---:|---:|---:|
| Reward mean | 416.82 | 460.61 | **478.35** | +61.53 |
| Adaptation mean | **3.981** | 4.466 | 4.503 | +0.522 |
| Transfer | **0.8100** | 0.8492 | 0.7136 | **−0.0964** |
| False switches/episode | **0.000** | 4.867 | 0.506 | +0.506 |
| Verifications/episode | 18.000 | 0.000 | 17.993 | −0.007 |

D's reward remained higher than B, but the primary robustness criteria were not preserved: D adapted more slowly, generated false switches where B generated none, and transfer dropped by 9.64 percentage points.

Paired Wilcoxon D vs B:

- reward: `p = 2.55e-16`;
- adaptation: `p = 0.0357`;
- transfer: `p = 1.23e-05`;
- false-switch rate: `p = 1.11e-79`.

## Classification

**FAILURE for the robustness/generalization claim.** EXP-0013's benefit does not survive this independent stress protocol. The metacontrol mechanism is sensitive to the statistical structure of misleading evidence and imperfect verification.

## Architectural consequence

No promotion to canonical `--AGI`. EXP-0013 remains evidence for a bounded metacontrol effect in its original protocol, not a general architectural principle.

The next research question is narrower: can metacontrol estimate evidence reliability / persistence before spending verification, without gaining hidden information or extra compute?

## Cleanup

Temporary executable machinery was used only locally and was not committed. No canonical repository or Space was modified. Only this evidence record and journal are retained.
