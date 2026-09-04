# EXP-0019 — Diagnostic Reasoning / Information-Seeking Action

**Status:** EXECUTED — PILOT / INCONCLUSIVE
**Date:** 2026-09-04

## Question
Can an agent diagnose a hidden cause more efficiently by choosing the next test for expected information gain instead of following a fixed troubleshooting sequence?

## Architectural idea
The target loop is:

`OBSERVATION → HYPOTHESIS SPACE → CURRENT BELIEF → CANDIDATE TESTS → INFORMATION GAIN → TEST → OBSERVATION → UPDATE CAUSAL MODEL → NEXT TEST`

Repeatedly performing the same low-information action is not equivalent to obtaining new evidence. A diagnostic agent should select an action that best separates the remaining causal hypotheses.

## Hypothesis
A bounded diagnostic policy that selects the next test by expected entropy reduction should reduce diagnostic cost and/or test count while maintaining or improving diagnosis accuracy, particularly when observations are noisy.

## Baselines
- **B_FIXED:** predetermined diagnostic test order.
- **D_INFO:** maintains a Bayesian posterior over the ten possible causes; selects the available test with the greatest expected entropy reduction under the known measurement-noise model; updates the posterior after each observation.
- A low-information `REPEAT_SWITCH` action is available as a control. It produces the same failure observation for every hidden cause and therefore should not be preferred while informative tests remain.

## Environment
Toy deterministic causal-diagnosis world:
- 10 possible hidden root causes, uniform prior.
- Four binary diagnostic tests encode a unique 4-bit signature for each cause.
- Measurements are independently noisy under pre-specified noise conditions.
- `REPEAT_SWITCH` returns the same observation for every cause and supplies no discriminating information.
- Same observations, action space, test budget, costs and seeds for B and D.
- D has no access to the hidden cause and receives no privileged state or extra environmental information.

## Conditions
Noise conditions: 0%, 5%, and 15%.
10,000 paired seeds per condition.
Stopping rule: stop when posterior confidence reaches 0.80 or the test budget is exhausted.

## Primary metrics
1. Mean number of diagnostic tests.
2. Mean diagnostic cost.
3. Final diagnosis accuracy.
4. Information gained.

Secondary metrics: per-cause accuracy, posterior confidence/calibration, paired seed differences, and frequency of selecting the no-information repeat action.

## Falsification / validity failure
The hypothesis is not supported if D shows no meaningful efficiency or accuracy advantage, or if any apparent advantage depends on hidden state, unequal observations, unequal test budget, or unbounded additional environmental information.

## Important scope boundary
This is an architectural toy experiment. It does **not** establish competence in real electrical troubleshooting or authorize unsafe physical diagnosis. The value being tested is the mechanism of causal hypothesis discrimination and information-seeking action.

## Provenance
An earlier local exploratory version of this mechanism was run before formal protocol registration. That exploratory run is retained only as motivation and is not treated as canonical evidence. The present record must distinguish proposed protocol, executed run, and resulting evidence.

## Canonical boundary
No changes to `SmartVoltISA/--AGI` are permitted. No result from this experiment is canonical without a separate promotion proposal and independent validation.
