# NS-A8.3 — Finite-Mode Pressure / Stretching Stress Test

**Status:** OPEN / NOT_PROVEN  
**Date:** 2026-09-10

## Purpose

The scalar pressure identity does not control the orientation of vortex stretching. The next adversarial test is therefore a finite Fourier construction designed to separate:

- scalar gradient invariants;
- pressure-Hessian response;
- stretching orientation `ω·Sω`.

## Required construction

On the periodic torus choose a divergence-free trigonometric polynomial

`u(x)=Σ_{k∈K} a_k exp(i k·x)`, `k·a_k=0`.

The test family must preserve real-valuedness by including conjugate modes.

For each member compute exactly:

`S=(∇u+∇u^T)/2`,

`ω=curl u`,

`G=∫ω·Sω dx`,

`D=ν∫|∇ω|^2 dx`,

`P_H=∫ F(S,ω,∇²p) dx` for any proposed pressure-Hessian coercive term.

## Failure condition

A proposed pressure-Hessian coercivity claim is rejected if there exists a scale family for which the proposed positive pressure term stays bounded while `G/D` grows without the required compensating scale factor.

A single finite-mode example is not a proof of non-regularity; it only falsifies the specific universal inequality being tested.

## Important safeguard

Do not infer pointwise statements from integrated cancellation. The pressure Hessian is nonlocal, and changing the Fourier phases can alter spatial alignment while preserving several scalar norms.

## Current result

No universal coercive inequality has yet been established. This file is an adversarial test specification, not a claimed counterexample.

**Status remains NOT_PROVEN.**
