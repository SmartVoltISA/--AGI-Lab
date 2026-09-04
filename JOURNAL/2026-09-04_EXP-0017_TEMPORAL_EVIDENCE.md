# Journal — 2026-09-04 / EXP-0017_TEMPORAL_EVIDENCE

## Scope

EXP-0017 tested whether temporal structure of contradictory observations can separate persistent regime change from transient noise.

Protocol was committed before execution on `exp-0017-run`. Canonical `--AGI` and Space were not modified.

## Execution

1000 paired seeds. B revised immediately; D used only the pre-registered accumulator `S`: contradiction adds 1, corroboration halves S, revision at S>=2. Same observations and no privileged information.

## Result

B reward `96.020`; D reward `102.872`.

B false switches `4.680`; D `0.280`.

B first/second adaptation `0.542 / 0.609`; D `1.160 / 1.212`.

B correct-action rate `0.90008`; D `0.92863`.

Paired p-values were strongly significant for reward, false switches, both adaptation delays and correct-action rate.

Raw per-seed digest: `b71f740d241417323babcd2fba865ef40c137f7b898b7cb0ea4f4a34ea641881`.

## Classification

**SUCCESS for the tested hypothesis, bounded to this protocol.**

The mechanism traded about 0.6 steps of adaptation delay for a ~94% reduction in false switching and a net reward increase. It also substantially reduced unnecessary model revisions. Compared with EXP-0015's fixed persistence, temporal accumulation recovered much of the adaptation cost.

## Architectural consequence

No promotion. This is a laboratory result. The next independent test must alter noise structure, timing and reliability so that the rule is not merely memorizing the current environment's temporal pattern.

## Cleanup

Temporary executable runner and raw data were not retained in the repository. Only protocol, reproduction specification, aggregate result and journal remain. The incomplete raw repository artifact was deleted. Canonical boundary preserved.
