# NS-A5 — BKM Endpoint Falsification Matrix

**Status:** PROPOSED / NOT_EXECUTED  
**Parent:** NS-A5_BKM_CRITICAL_ENDPOINT_ATTACK.md  
**Date:** 2026-09-10

## Purpose

Prevent the BKM branch from turning a plausible critical-space slogan into an unsupported proof.

## Test matrix

| ID | Attack | Required failure mode |
|---|---|---|
| A5-T01 | Scaling | Reject any estimate with incorrect NS scaling |
| A5-T02 | Single-shell concentration | Detect cutoff-dependent constants |
| A5-T03 | Many-shell accumulation | Detect loss of summability |
| A5-T04 | Endpoint q=∞ | Reject unjustified replacement of supremum by summation |
| A5-T05 | Time concentration | Detect estimates that control snapshots but not the continuation integral |
| A5-T06 | Critical norm bounded / `||ω||∞` large | Reject false pointwise embedding claims |
| A5-T07 | Logarithmic bridge | Expose hidden supercritical quantities inside the logarithm |
| A5-T08 | Pressure nonlocality | Require explicit singular-integral hypotheses |
| A5-T09 | Truncation limit | Require constants uniform as `J→∞` |
| A5-T10 | Circular continuation | Reject use of the desired regularity in the estimate proving it |

## Evidence standard

A numerical experiment can falsify a proposed universal inequality by finding a genuine counterexample, but numerical survival cannot prove the inequality. An analytical proof must state the function spaces, constants, domain assumptions, boundary conditions, and all limiting operations.

## Promotion gate

Only one of the following outcomes is allowed:

- `REJECTED` — a rigorous counterexample or invalid inference is found;
- `PARTIAL` — a valid lemma/reduction survives but does not close continuation;
- `SUPPORTED` — a complete independently checked continuation estimate is established;
- `NOT_PROVEN` — the route remains plausible but lacks a required proof step;
- `INVALID` — the proposed argument violates the methodological rules.

`VERIFIED_SOLUTION` is impossible unless the full mathematical claim is independently verified outside the candidate-generation process.
