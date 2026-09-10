# NS-A2.4 — Fourier Counterexample Search

**Status:** PROPOSED / NOT_EXECUTED  
**Date:** 2026-09-10  
**Parent:** NS-A2

## Purpose

Before accepting any critical dyadic inequality, actively search for divergence-free finite Fourier fields that make the proposed nonlinear interaction as large as possible relative to the proposed control norm.

## Test family

Use periodic trigonometric vector fields

`u(x) = Σ_{k∈K} a_k exp(i k·x)`,

with

`k·a_k = 0`,

and impose the reality condition `a_{-k} = conjugate(a_k)`.

Normalize the candidate critical norm, then maximize the target vortex-stretching or shell-flux functional over amplitudes and phases.

## Acceptance

A proposed inequality survives this test only if:

- no finite Fourier configuration violates it;
- the observed extremal scaling matches the claimed critical scaling;
- the result is stable as the maximum frequency increases;
- the test does not accidentally impose symmetry that removes the dangerous interaction.

## Rejection

Any explicit violating configuration rejects the proposed universal inequality. Numerical optimization alone cannot prove an inequality, but a reproducible violation is sufficient to kill one.

## Safety / scope

Purely mathematical offline computation. No external systems, no canonical repository writes, and no claim of proof from numerical evidence.

**Classification:** NOT_EXECUTED.
