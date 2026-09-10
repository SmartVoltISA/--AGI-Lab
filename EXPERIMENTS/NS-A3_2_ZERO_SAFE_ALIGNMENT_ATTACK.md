# NS-A3.2 — Zero-Safe Weighted Alignment Attack

**Status:** OPEN / NOT_PROVEN  
**Parent:** NS-A3.1  
**Date:** 2026-09-10

## Objective

Remove the `|ω|^{-1}` singularity from the vorticity-direction formulation and test whether a weighted alignment observable can yield a genuine depletion estimate.

Define

`ρ = |ω|`, `a = (ω·Sω)/(|ω|²)` where `ρ>0`.

Instead of evolving `ξ=ω/ρ` directly, use weighted quantities such as

`A_ε(t) = ∫ (ω·Sω)_+ / (ρ²+ε²)^{1/2} * w(ρ,ε) dx`

with a smooth bounded weight `w`. The exact choice is itself a hypothesis and must be fixed before testing.

## Necessary requirements

A successful functional must:

1. remain finite at `ω=0`;
2. have a clearly defined Navier–Stokes scaling;
3. produce an evolution identity with all commutator/error terms explicit;
4. avoid uncontrolled derivatives of `S` or pressure;
5. couple positive alignment to viscous dissipation or another coercive term;
6. yield a time-integrated bound strong enough for a continuation criterion;
7. remain valid as `ε→0` without constants diverging;
8. not assume a priori regularity beyond the smooth local solution used for derivation.

## Adversarial cases

- `ω` approaching zero while direction changes rapidly;
- nearly constant direction with large positive strain;
- concentration in a thin spatial region;
- high-frequency strain with moderate vorticity;
- mixed-sign strain eigenvalues;
- pressure-driven nonlocal strain;
- rescaled solutions;
- `ε→0` endpoint behavior.

## First analytical boundary

Differentiating any nonlinear alignment functional introduces derivatives of `S`, hence second derivatives of `u`, together with pressure Hessian terms. These terms are nonlocal and are not automatically controlled by the positive alignment itself.

Therefore a pointwise alignment observable is unlikely to close by itself. A viable route probably needs a cancellation, a singular-integral estimate at critical regularity, or a combined flux/alignment functional.

## Decision

No closure has been obtained.

**Classification: NOT_PROVEN.**

The useful result is a sharper bottleneck: any successful geometric proof must control the nonlocal evolution of strain simultaneously with vorticity alignment, not merely bound the angle at one instant.
