# EXP-0019 — Reproduction Specification

## Fixed environment
- Causes: integers 0–9.
- Cause signature: `format(cause + 1, '04b')`.
- Tests: four binary signature-bit tests plus `REPEAT_SWITCH`.
- Prior: uniform across ten causes.
- Measurement noise: 0%, 5%, 15%.
- Paired seeds: 10,000 per noise condition.
- Stopping confidence: max posterior >= 0.80.
- Same test costs and maximum budget for both policies.

## Fixed policy
B_FIXED uses a predetermined order of informative tests and does not adapt test selection to the posterior.

## Information policy
D_INFO:
1. Initialize the uniform posterior.
2. For every unused candidate test, calculate expected posterior entropy after each possible observation under the pre-registered noise rate.
3. Compute expected entropy reduction.
4. Select the available test with maximum expected information gain per unit test cost.
5. Observe the noisy result and perform the corresponding Bayesian update.
6. Stop at confidence >= 0.80 or at the common test budget.
7. `REPEAT_SWITCH` has zero discriminating information and a positive cost, so it should be dominated whenever an informative test remains.

## Controls
- Identical hidden causes, observations, action spaces, seeds, test budget and costs.
- No hidden-state access by D_INFO.
- No extra environmental information.
- Extra computation is internal selection computation only; it cannot reveal the cause.

## Required reporting
For each noise condition report mean test count, mean cost, accuracy, information gained, and repeat-action rate. Report paired differences using the same seeds.

## Evidence status
The prior local exploratory simulation produced preliminary differences, but its raw data were not retained in the repository. Therefore those numbers must not be represented as reproducible formal evidence. A clean execution after this protocol commit is required for a formal classification beyond PILOT / INCONCLUSIVE.
