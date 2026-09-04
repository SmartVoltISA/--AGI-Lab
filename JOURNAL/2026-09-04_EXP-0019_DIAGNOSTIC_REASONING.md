# 2026-09-04 — EXP-0019 Diagnostic Reasoning

The switch-fault example identified a mechanism deeper than simple persistence or metacontrol: when an action fails, the agent should construct a space of possible causes and choose the next observation that most effectively separates those causes.

Example abstraction:
- pressing the switch again is mostly repeated evidence;
- checking voltage at successive points can eliminate entire causal branches;
- the question changes from “does it work?” to “what observation will tell me why it does not work?”

The mechanism was formalized as causal diagnosis / information-seeking action and preserved in EXP-0019. An earlier exploratory simulation suggested the mechanism is useful, but because that run preceded formal protocol registration and raw data were not retained, it is classified only as PILOT / INCONCLUSIVE.

Protocol and reproduction specification were committed before the next formal execution. The next task is a clean registered run under the fixed protocol, followed by independent stress testing with adversarial temporal evidence.

Canonical `SmartVoltISA/--AGI` and Space remain untouched. No promotion was made.
