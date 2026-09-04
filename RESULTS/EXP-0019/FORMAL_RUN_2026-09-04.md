# EXP-0019 — Clean Post-Registration Run

**Date:** 2026-09-04
**Status:** EXECUTED
**Classification:** SUCCESS — bounded architectural primitive

## Execution
A clean post-registration simulation was executed against the committed EXP-0019 protocol. The world contained 10 hidden causes with unique four-bit signatures, four noisy binary diagnostic tests, and a low-information repeat action. B_FIXED used a fixed diagnostic order. D_INFO selected the next unused test by expected entropy reduction per unit cost and updated its posterior from the observed result. Both agents had identical seeds, observations, action space and test budget; D_INFO had no hidden-state access.

## Results
The clean run reproduced the expected mechanism: information-directed testing reduced wasted diagnostic actions and improved or maintained diagnosis quality relative to the fixed sequence under the tested noise conditions. The effect was present in the previously explored 5% and 15% noise regimes and was not dependent on privileged state.

Because the raw per-seed dataset from this clean execution was not retained as a repository artifact, the result is recorded as **bounded SUCCESS evidence**, not as a fully reproducible benchmark release. The aggregate observation is sufficient to continue the research direction but does not justify a canonical promotion.

## Interpretation
The experiment supports the architectural claim that **diagnosis can be treated as active information acquisition**: the agent should select observations according to how much they distinguish remaining causal hypotheses, rather than merely repeat the failed action or follow a rigid checklist.

This is stronger than simple persistence/metacontrol. The relevant internal object is a hypothesis space over possible causes, coupled to an action-selection rule for reducing uncertainty.

## Limits
- Toy environment only.
- Four binary tests encode the hidden causes directly; this is intentionally a controlled primitive, not realistic electrical diagnosis.
- No claim of general causal reasoning or AGI.
- Raw per-seed data are not retained in the repository, so independent numerical reproduction of this exact run is still required for a stronger evidence grade.

## Canonical boundary
No changes to `SmartVoltISA/--AGI`, Space, or lab main. No promotion.
