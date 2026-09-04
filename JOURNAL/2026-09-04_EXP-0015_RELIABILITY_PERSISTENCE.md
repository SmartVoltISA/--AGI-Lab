# Journal — 2026-09-04 / EXP-0015_RELIABILITY_PERSISTENCE

## Scope

EXP-0015 tested whether persistence of contradictory evidence can make metacontrol robust to intermittent misleading observations.

The experiment was isolated on `exp-0015-run`. Canonical `--AGI` and Space were not modified.

## Execution

- Deterministic binary-rule environment.
- 1000 seeds (`0..999`).
- Same observation stream per seed for B and D.
- B revises on first surprising observation.
- D revises only after 3 consecutive surprising observations.
- Noise burst: steps 60–74 at 55% observation reliability.
- Rule changes: step 50 and step 90.
- No hidden-state access or extra compute for D.

## Result

B: reward `92.424`, false switches `8.825`, first adaptation `0.508`, second adaptation `1.699`.

D: reward `98.726`, false switches `0.596`, first adaptation `2.276`, second adaptation `2.392`.

Reward improvement was statistically significant (`p = 3.073e-103`). False-switch reduction was extremely strong (`p < 1e-300`). First-adaptation slowdown was significant (`p = 1.858e-90`). Second-adaptation difference was not significant (`p = 0.1051`).

Raw result digest: `504ca6e6209370f4598ee1304a61f9caa3850d0455357a50f941bbbd7449e053`.

## Classification

**INCONCLUSIVE / PARTIAL SUPPORT.**

Persistence clearly improved robustness and utility in this protocol, but the cost in adaptation speed prevents a broad success claim.

## Architectural consequence

No canonical change. The next useful question is whether persistence can be adaptive to evidence reliability without introducing extra information or computation.

## Cleanup

No executable experiment machinery was committed. Only protocol, reproduction specification, result summary and journal were retained. Canonical boundary preserved.
