# EXP-0020 — Model-Level Diagnosis

**Date:** 2026-09-04
**Classification:** INCONCLUSIVE / PARTIAL SUPPORT

## Question
Can an information-seeking diagnostic agent recognize when the causal model itself is uncertain and use evidence to distinguish competing models?

## Run
A controlled toy world contained two competing causal models and six causes per model. Three ordinary diagnostic observations were model-dependent, and a separate `MODEL_CHECK` observation directly but noisily discriminated the models. B_FIXED followed a fixed test order. D_INFO maintained a posterior over the joint hypothesis `(model, cause)` and selected tests by expected information gain per unit cost.

10,000 paired seeds were run at each noise level: 0%, 5%, 15%, 25%. Same hidden state, observations, action space and budget; D had no privileged access to the hidden model.

## Aggregate observations
| Noise | B accuracy | D accuracy | B model accuracy | D model accuracy |
|---:|---:|---:|---:|---:|
| 0% | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 5% | 0.8336 | 0.8313 | 0.9261 | 0.9438 |
| 15% | 0.5610 | 0.5610 | 0.8232 | 0.8533 |
| 25% | 0.3582 | 0.3566 | 0.7482 | 0.7221 |

At 0% noise D used fewer tests on average (4.6709 vs 4.8325). At 5% and above the fixed six-step budget was usually exhausted, so efficiency differences disappeared.

## Interpretation
The joint posterior does represent model uncertainty and D selected evidence that improved model identification at 5% and 15% noise. However, overall causal-state accuracy did not improve robustly, and at 25% noise model identification was worse than the fixed baseline.

Therefore the experiment does **not** establish model-revision competence. It establishes only a partial primitive: model uncertainty can be represented and tested, but the agent still lacks a robust strategy for deciding when its current causal model should be abandoned or replaced under adversarial/noisy evidence.

## Architectural consequence
The next mechanism should explicitly score **model contradiction** over time and compare competing explanations, rather than treating every observation as evidence only about `(model, cause)`. A dedicated model-check action should be chosen when internal predictions become persistently inconsistent.

## Boundary
No canonical `--AGI` or Space changes. No promotion. This negative/partial result is retained as evidence.
