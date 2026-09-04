# EXP-0013 — Memory, affect and metacontrol

Status: PROPOSED / NOT YET EXECUTED
Date: 2026-09-04

## Question

Can an internal significance/affective signal improve adaptation by changing the **mode of model checking** rather than directly selecting actions?

## Hypothesis

The failure of EXP-0012 may be caused by coupling affect directly to action selection. A metacontrol design may use surprise/error to increase checking, exploration or model revision while leaving the action policy otherwise comparable to the memory baseline.

## Agents

- **B_memory:** memory → action.
- **C_affect_action:** memory + affect → action. Reproduces the EXP-0012 causal pattern.
- **D_metacontrol:** memory/model → surprise → bounded internal significance → checking/revision mode → action.

## Environment

Deterministic discrete environment with:

1. an initially stable rule;
2. sufficient experience to form a useful memory/model;
3. a hidden rule change;
4. post-change observations that can contradict the old model;
5. occasional misleading/noisy evidence so that immediate switching is not always optimal;
6. a later novel context testing transfer.

Fixed action/observation spaces and identical seeds across agents.

## Controls

- Same environment and seeds.
- Same observable information available to all agents.
- Comparable computational budget.
- Predefined metrics before execution.
- Ablation of D's metacontrol signal.
- Identity control: D with metacontrol disabled should reproduce B's decision trace where implementation permits.
- No LLM and no external model.

## Metacontrol mechanism

A bounded internal variable is derived from prediction error/surprise. It does **not** directly choose an action. Instead it can modify one or more predefined control variables:

- number/depth of model checks;
- evidence threshold for model revision;
- exploration probability;
- confidence threshold before committing to the old strategy.

All variables remain bounded and are logged.

## Primary metrics

- adaptation time after true rule change;
- cumulative reward;
- false-switch rate after misleading evidence;
- model-revision precision;
- number of unnecessary checks;
- transfer performance in novel context.

## Critical comparison

The key test is not whether D reacts faster than B. It is whether D can **distinguish real model failure from misleading evidence** better than C/B while preserving or improving cumulative reward.

## Falsification

The hypothesis fails if:

- D does not improve the predefined primary criterion;
- gains disappear across seeds;
- gains come from extra compute/information rather than metacontrol;
- D merely reacts faster but increases false switches enough to reduce utility;
- disabling metacontrol does not causally remove the observed effect.

## Evidence policy

PROPOSED ≠ EXECUTED.
EXECUTED ≠ SUCCESSFUL.
UNKNOWN ≠ TRUE.
RESULT ≠ CANONICAL.

## Cleanup

All executable experiment machinery is temporary. After execution it must be deleted; results, raw observations, parameters, failures and journal remain. Canonical `--AGI` and Space must remain unchanged.
