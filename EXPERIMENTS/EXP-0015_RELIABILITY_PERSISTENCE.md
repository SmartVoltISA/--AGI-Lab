# EXP-0015 — Reliability and persistence in metacontrol

**Status:** EXECUTED
**Date:** 2026-09-04

## Question
Can temporal persistence of contradictory evidence make metacontrol more robust to intermittent misleading observations?

## Hypothesis
A metacontrol state that requires persistent contradictory evidence before revising the internal model should reduce false switching under intermittent noise, while preserving useful adaptation. This is a hypothesis about a bounded control mechanism, not consciousness or emotion.

## Baseline
**B_memory:** identical observation stream and action policy; revises the model after the first surprising observation.

**D_persistence:** identical observation stream and action policy; maintains a bounded contradiction streak and revises only after 3 consecutive surprising observations.

## Fairness controls
- same deterministic environment;
- same action and observation spaces;
- same 1000 seeds (`0..999`);
- identical observations for B and D per seed;
- no hidden-state access;
- no additional information or unbounded computation;
- identical action rule when model state is identical.

## Environment
Binary rule. Initial rule is `+1`; changes to `-1` at step 50 and returns to `+1` at step 90. Observation reliability is 95% except for a predefined high-noise interval at steps 60–74 where reliability is 55%. Reward is +1 for matching the current rule and -1 otherwise.

## Procedure
For every seed, run B and D for 120 steps on the same environment. Record first adaptation latency after each rule change, cumulative reward, and false model switches. D's persistence threshold is fixed at 3 before execution and is not tuned from results.

## Primary metrics
- cumulative reward;
- false-switch count.

## Secondary metrics
- adaptation latency after first rule change;
- adaptation latency after second rule change.

## Falsification
The hypothesis is weakened if persistence does not reduce false switching, reduces utility, or prevents useful adaptation. Faster adaptation alone is not sufficient for success.

## Evidence policy
`PROPOSED ≠ EXECUTED`; `EXECUTED ≠ SUCCESSFUL`; `UNKNOWN ≠ TRUE`; result is not canonical.

## Cleanup requirement
The executable organism and runner are temporary and must not be committed. Raw observations and result summaries are retained.

## Canonical boundary
`--AGI` and Space are out of scope. No automatic promotion is permitted.
