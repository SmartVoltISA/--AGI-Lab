# Journal — 2026-09-04 / EXP-0018_TEMPORAL_EVIDENCE_STRESS

## Scope

Independent stress/generalization test of the EXP-0017 temporal-evidence mechanism.

Protocol was committed before execution. Canonical `--AGI` and Space were not modified.

## Execution

3000 paired episodes: three pre-registered scenarios × 1000 seeds. Rule-change timings and noise bursts were changed from EXP-0017. D retained exactly the same accumulator and threshold; no retuning.

## Result

Aggregate reward: B `104.567`, D `118.074` (Δ `+13.507`).

Aggregate false switches: B `27.251`, D `7.075` (Δ `−20.176`).

Correct-action rate: B `0.87346`, D `0.92169` (Δ `+0.04824`).

Model revisions: B `29.558`, D `7.242` (Δ `−22.316`).

All four paired Wilcoxon comparisons were `p < 1e-300` at reporting precision.

Every individual stress scenario showed the same direction: D had higher reward and fewer false switches.

Raw stress-data digest: `93b4680a41a288a08fa41696fbe6e2c9b59ac76c8d41b6d05bda792a4cbfb715`.

## Classification

**SUCCESS — independent stress/generalization support.**

The mechanism did not merely exploit the original timing/noise arrangement. Across the three altered regimes it retained a large robustness and utility advantage over immediate revision.

## Architectural consequence

No canonical promotion. We now have a replicated laboratory result for temporal evidence accumulation as a metacontrol primitive. The next test should challenge the mechanism with adversarial temporal patterns designed to make persistent noise resemble a regime change, rather than simply varying parameters.

## Cleanup

No executable runner or raw dataset was committed. Local raw data was hashed and removed. Only protocol, reproduction specification, aggregate result and journal remain. Canonical boundary preserved.
