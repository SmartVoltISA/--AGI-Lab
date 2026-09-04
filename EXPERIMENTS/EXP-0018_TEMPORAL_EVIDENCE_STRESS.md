# EXP-0018 — Temporal evidence stress/generalization

## Status

**PROPOSED / PRE-REGISTERED** — fixed before execution.

## Question

Does the EXP-0017 temporal-evidence mechanism remain useful when rule-change timing and noise structure differ from the training-like protocol?

## Hypothesis

The fixed temporal accumulator from EXP-0017 (`contradiction +1`, `corroboration ×0.5`, revision at `S>=2`) will retain a net utility advantage over immediate revision across altered temporal regimes, without privileged information.

## Agent rules

B: immediate revision on contradiction.

D: exactly the EXP-0017 accumulator, with no parameter changes.

No tuning after execution begins.

## Stress suite

Three pre-defined scenarios, 1000 seeds each, 140 steps each:

**A — early/late changes + short noisy burst**
- rule changes: `35 → -1`, `105 → +1`
- noise burst: `55–63`, reliability `0.60`
- otherwise reliability `0.90`

**B — clustered changes + long noisy burst**
- rule changes: `45 → -1`, `75 → +1`, `110 → -1`
- noise bursts: `20–34` at `0.70`; `82–101` at `0.55`
- otherwise reliability `0.95`

**C — irregular changes + moderate bursts**
- rule changes: `28 → -1`, `67 → +1`, `119 → -1`
- noise bursts: `40–52` at `0.65`; `88–96` at `0.60`
- otherwise reliability `0.92`

Reward is `+1` for model matching the current rule, `-1` otherwise.

## Primary metrics

Aggregate across all scenarios and separately by scenario:
1. total reward;
2. false switches;
3. correct-action rate;
4. adaptation delay after each true change.

## Falsification

If D loses utility in a majority of scenarios, or robustness gains are consistently purchased by excessive adaptation delay, the mechanism is not considered generalizable.

## Canonical boundary

No writes to canonical `SmartVoltISA/--AGI` or Space. Temporary execution machinery and raw data are disposable; verified aggregate evidence remains.
