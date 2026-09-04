# EXP-0016 — Adaptive persistence in metacontrol

## Status

**PROPOSED / PRE-REGISTERED** — protocol written before execution.

## Question

Can metacontrol adapt its contradiction-confirmation threshold to recent evidence reliability, reducing false switching without paying the full adaptation cost of fixed persistence?

## Hypothesis

An adaptive persistence policy will outperform fixed persistence by using short persistence when recent evidence has proved reliable and longer persistence when evidence has proved noisy. Success requires improvement in both robustness (false switching) and utility, without a material loss of useful adaptation.

## Agents

- **B_memory**: revise model immediately on the first surprising observation.
- **D_adaptive**: maintain contradiction streak and an evidence-reliability estimate. The estimate changes only from observable post-revision corroboration; no hidden state is exposed.

### Pre-registered D rule

Maintain `reliability_score` in `[0,1]`, initialized to `0.95`, and `confirmation_threshold` initially `1`.

After every model revision, inspect the next **three** observations only for corroboration of the newly adopted model. For each of these observations, add `+1` to corroboration count if it agrees with the model and `-1` otherwise. Update the score by:

`reliability_score = 0.5 * reliability_score + 0.5 * (corroboration_count / observations_seen)`

After at least three post-revision observations, set the next contradiction threshold:

- score `>= 0.85` → threshold `1`
- score `0.65–0.849999...` → threshold `2`
- score `< 0.65` → threshold `3`

A threshold decision is frozen until the next completed three-observation reliability update. A contradiction increments the streak; corroboration resets it. The model is revised when the streak reaches the current threshold. A revision resets the contradiction streak and starts a new three-observation reliability window.

No extra verification calls or computation are allowed for D beyond this state update; B and D receive identical observations and the same action space.

## Environment

Deterministic binary-rule environment:

- Seeds: `0..999`
- Episode length: `120` steps
- Initial rule: `+1`
- Rule changes: step `50 → -1`; step `90 → +1`
- Observation reliability: `0.95`, except steps `60–74` inclusive: `0.55`
- Reward: `+1` if action equals current rule, otherwise `-1`
- Initial model: `+1`
- Same observation stream per seed for B and D
- No hidden-state access

## Controls

- **D_off identity control**: run D's action path with adaptive persistence disabled and fixed threshold `1`; decision trace must match B exactly when model state is identical.
- Same seeds, episode length, observation streams and action space.
- No extra computation budget or privileged information for D.

## Primary metrics

1. Total reward.
2. False switches (model revisions not corresponding to a true rule change).
3. First adaptation delay after step 50.
4. Second adaptation delay after step 90.
5. Correct-action rate.
6. Number of model revisions.

## Secondary metrics

- Reliability-score trajectory.
- Threshold trajectory.
- Robustness during the 60–74 noise burst.
- Paired per-seed differences and non-parametric significance tests.

## Falsification

The hypothesis is not supported if D does not reduce false switching and does not improve utility, or if any apparent advantage depends on unequal observations, hidden state, extra compute, post-hoc threshold tuning, or a broken identity control.

A result showing robustness at the cost of materially slower adaptation is classified as **PARTIAL SUPPORT / INCONCLUSIVE**, not success.

## Canonical boundary

No writes to canonical `SmartVoltISA/--AGI` or Space are permitted. This experiment is disposable. Only protocol, reproducibility specification, raw/result evidence, journal and cleanup verification may remain in the lab branch.
