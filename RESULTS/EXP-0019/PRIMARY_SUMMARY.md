# EXP-0019 — Primary Summary

## Classification
**INCONCLUSIVE / PARTIAL SUPPORT**

The clean post-registration run was executed locally with 10,000 paired seeds for each of three noise conditions. The mechanism showed an efficiency advantage in low/noise settings, but the advantage disappeared at the highest tested noise level and did not improve final accuracy. Therefore this is not a general SUCCESS claim.

## Clean run results
| Noise | Fixed mean tests | Info mean tests | Fixed accuracy | Info accuracy |
|---|---:|---:|---:|---:|
| 0% | 3.8011 | 3.4036 | 1.0000 | 1.0000 |
| 5% | 3.8894 | 3.5917 | 0.8406 | 0.8406 |
| 15% | 4.0000 | 4.0000 | 0.5819 | 0.5811 |

At 0% noise, information-directed selection reduced mean tests by 0.3975 while preserving perfect accuracy. At 5% noise it reduced mean tests by 0.2977 with identical accuracy. At 15% noise, no efficiency advantage remained and accuracy was essentially unchanged.

## Mechanism preserved
The experiment formalizes a causal-diagnostic primitive:

`failure → hypothesis space → candidate tests → expected information gain → test → evidence → posterior update → next test`

The important distinction is between **repeating an action** and **obtaining discriminating evidence**. A diagnostic system should spend its limited actions on tests that eliminate or separate causal hypotheses.

## Interpretation
The result supports the narrower claim that active information-seeking can reduce diagnostic effort when the evidence is sufficiently reliable. It does **not** yet establish robustness to substantial measurement noise, nor general causal reasoning.

The next experiment should therefore make the diagnostic world less artificially informative: tests should overlap in their causal signatures, have unequal costs/reliabilities, and include misleading observations. The agent should then have to reason about both **which cause is plausible** and **which test is worth performing next**.

## Evidence limits
The per-seed execution was run locally and aggregate results were recorded here; raw per-seed data are not retained in the repository. Thus this remains a bounded laboratory result, not a fully reproducible benchmark release.

## Canonical boundary
No canonical `--AGI` or Space change. No promotion.
