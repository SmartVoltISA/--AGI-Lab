# EXP-0017 — Temporal evidence: regime change vs transient noise

## Status

**PROPOSED / PRE-REGISTERED** — protocol fixed before execution.

## Question

Can a metacontroller distinguish a persistent regime change from transient contradictory observations using only the temporal structure of observed evidence?

## Hypothesis

A decaying contradiction-evidence accumulator will reduce false model switching while preserving faster adaptation than fixed three-consecutive persistence. The mechanism treats repeated contradiction as accumulating evidence, while corroboration decays unresolved contradiction rather than resetting it instantly.

## Agents

- **B_memory**: immediate model revision on first contradiction.
- **D_temporal**: maintain scalar contradiction evidence `S`.

### Pre-registered D rule

Initialize `S = 0`.

At each observation:

- if observation contradicts current model: `S := S + 1`
- if observation corroborates current model: `S := 0.5 * S`
- revise the model to the current observation when `S >= 2.0`
- after revision: `S := 0`

No threshold changes, parameter tuning, hidden-state access, extra verification calls, or additional computation are permitted after execution begins.

The threshold `2.0` and decay factor `0.5` are fixed in this protocol before the run.

## Environment

Base environment is the EXP-0015/0016 binary-rule environment:

- 1000 seeds (`0..999`)
- 120 steps
- initial rule `+1`
- true rule changes at steps `50 → -1` and `90 → +1`
- observation reliability `0.95`, except steps `60–74` inclusive at `0.55`
- reward `+1` for correct model/action, `-1` otherwise
- identical observation stream for B and D per seed
- no hidden-state access

## Primary metrics

1. Total reward.
2. False switches.
3. First adaptation delay after step 50.
4. Second adaptation delay after step 90.
5. Correct-action rate.

## Controls

- D_off: temporal accumulator disabled and immediate-revision path used; its decision trace must match B.
- Same seeds, observations, action space and computational budget.

## Falsification

The hypothesis is not supported if D fails to reduce false switches while preserving adaptation sufficiently to improve or maintain utility, or if any advantage depends on information unavailable to B.

A robustness gain with a substantial utility loss is **PARTIAL SUPPORT / INCONCLUSIVE**, not success.

## Canonical boundary

No writes to canonical `SmartVoltISA/--AGI` or Space. The experiment is disposable; only protocol and verified evidence survive.
