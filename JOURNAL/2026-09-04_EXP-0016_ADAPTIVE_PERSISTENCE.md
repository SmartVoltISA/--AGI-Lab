# Journal — 2026-09-04 / EXP-0016_ADAPTIVE_PERSISTENCE

## Scope

EXP-0016 tested whether metacontrol can adapt its contradiction-confirmation threshold from observable evidence reliability, following the pre-registered protocol.

The experiment was isolated on `exp-0016-run`. Canonical `--AGI` and Space were not modified.

## Execution

- Protocol committed before execution.
- 1000 seeds (`0..999`).
- 120-step deterministic binary-rule environment.
- Same observation stream per seed for B and D.
- D used the pre-registered three-observation corroboration window and score thresholds `0.85/0.65`, producing persistence thresholds `1/2/3`.
- No hidden-state access or extra compute for D.
- D_off identity control used fixed threshold `1`.

## Result

B: reward `92.424`, false switches `8.825`, first adaptation `0.059`, second adaptation `0.059`, correct-action rate `0.89957`, revisions `19.386`.

D: reward `92.254`, false switches `5.318`, first adaptation `0.331`, second adaptation `0.968`, correct-action rate `0.89960`, revisions `12.461`.

Paired tests: reward `p=0.5239`; false switches `p=4.84e-155`; first adaptation `p=5.37e-55`; second adaptation `p=1.79e-124`; correct-action rate `p=0.7876`.

Raw per-seed result digest: `cd9dcb301f28fd6701e4e4d1c1076297784e59f7194ca391d36d6baf085558b4`.

## Classification

**INCONCLUSIVE / PARTIAL SUPPORT.**

Adaptive persistence clearly reduced false switching, but did not improve total reward and significantly slowed both measured adaptation points. The policy therefore demonstrates a robustness benefit without demonstrating a net performance advantage.

## Architectural consequence

No canonical change. Keep adaptive persistence as an experimental robustness mechanism only. The next question is whether the metacontroller can separate regime-change evidence from transient noise using only observable history, with the distinction pre-registered before testing.

## Cleanup

No executable experiment machinery was committed. The local runner and raw per-seed data were temporary; only protocol, reproduction specification, aggregate results and this journal were retained. The incomplete repository raw artifact was deleted before completion. Canonical boundary preserved.
