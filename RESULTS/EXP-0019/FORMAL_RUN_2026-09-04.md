# EXP-0019 — Clean Post-Registration Run

**Date:** 2026-09-04
**Status:** EXECUTED
**Classification:** INCONCLUSIVE / PARTIAL SUPPORT

## Execution
A clean post-registration simulation was executed against the committed EXP-0019 protocol with 10,000 seeds per noise condition (0%, 5%, 15%). The world contained 10 hidden causes with unique four-bit signatures and four noisy binary diagnostic tests. B_FIXED used a fixed diagnostic order. D_INFO selected the next unused test by expected entropy reduction and updated its posterior from the observed result. Both agents had identical seeds, observations, action space and test budget; D_INFO had no hidden-state access.

## Results
| Noise | B_FIXED mean tests | D_INFO mean tests | B_FIXED accuracy | D_INFO accuracy |
|---|---:|---:|---:|---:|
| 0% | 3.8011 | 3.4036 | 1.0000 | 1.0000 |
| 5% | 3.8894 | 3.5917 | 0.8406 | 0.8406 |
| 15% | 4.0000 | 4.0000 | 0.5819 | 0.5811 |

The information-directed policy reduced mean tests by 0.3975 at 0% noise and 0.2977 at 5% noise, with no accuracy loss. At 15% noise the efficiency advantage disappeared and accuracy was effectively unchanged.

## Interpretation
The run provides **partial support** for the mechanism: active information-seeking can reduce diagnostic effort when observations are reliable enough. It does not yet establish robustness under substantial noise or demonstrate general causal reasoning.

The important architectural distinction remains:

`failure → hypothesis space → candidate tests → information gain → test → evidence → posterior update → next test`

This is stronger than merely persisting with the same action. The agent is selecting an observation because of what that observation can tell it about competing causes.

## Limits
- Toy environment only.
- Four binary tests encode the hidden causes directly.
- No claim of real electrical troubleshooting competence, general causal reasoning, or AGI.
- Raw per-seed data were run locally but are not retained as a repository artifact; aggregate results therefore have a limited evidence grade.

## Next test
Move to overlapping/non-unique causal signatures, unequal test costs/reliabilities, and misleading observations. The diagnostic policy should then optimize information value under uncertainty rather than exploit uniquely encoded bits.

## Canonical boundary
No changes to `SmartVoltISA/--AGI`, Space, or lab main. No promotion.
