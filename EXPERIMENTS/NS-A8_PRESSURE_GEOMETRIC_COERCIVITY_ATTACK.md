# NS-A8 — Pressure / Geometric Coercivity Attack

**Status:** OPEN / NOT_PROVEN  
**Parent:** EXP-0013 Navier–Stokes line  
**Date:** 2026-09-10

## Motivation

A2–A7 repeatedly reduce the unresolved difficulty to controlling vortex stretching / critical nonlinear transfer. A different route is therefore required: use the pressure Hessian and strain geometry rather than another frequency-window rearrangement.

For incompressible 3D Navier–Stokes,

`∂t u + (u·∇)u = -∇p + νΔu`, `div u = 0`.

The strain tensor is `S=(∇u+∇u^T)/2`, and vorticity satisfies

`D_t ω = Sω + νΔω`.

The enstrophy production is

`G = ∫ ω·Sω dx`.

The pressure satisfies

`-Δp = tr((∇u)^2) = |S|^2 - |Ω|^2`.

Thus pressure is not an independent scalar decoration: its Hessian is nonlocally tied to the same velocity-gradient geometry that creates stretching.

## H8.1 — Pressure-Hessian depletion

Test whether the stretching production can be decomposed into a coercive pressure-Hessian contribution plus terms controlled by viscous dissipation:

`G ≤ C_1 D + C_2 R`,

where `D=ν||∇ω||_2^2` and `R` is a scale-critical remainder that is strictly weaker than the original stretching term.

Acceptance requires an exact identity or inequality with explicit constants and no hidden `||ω||_∞` assumption.

## H8.2 — Strain eigenframe evolution

Write `ω=|ω|ξ` and diagonalize `S`. Then

`ω·Sω = |ω|^2 ξ·Sξ`.

Attack the possibility that sustained positive stretching forces either:

1. rapid rotation of `ξ` away from the most expansive eigenvector;
2. growth of transverse gradients producing viscous depletion;
3. pressure-Hessian feedback that prevents persistent alignment.

Any argument must survive the zero-vorticity set and cannot divide by `|ω|` without a zero-safe formulation.

## H8.3 — Pressure-free counterexample

Construct finite-dimensional divergence-free Fourier fields for which:

- `G>0` is large;
- pressure Hessian contribution is small or cancelling;
- viscous dissipation is fixed;
- the ratio is scale invariant.

If such a family exists, the proposed coercive route is rejected.

## H8.4 — Self-similar / Type-I stress test

Check the candidate mechanism against the Navier–Stokes scaling

`u_λ(x,t)=λu(λx,λ²t)`.

Any estimate with a noncritical dimensional coefficient is rejected unless it comes with a controlled scale parameter.

## Relation to known mathematics

Geometric regularity criteria based on vortex direction and vortex-stretching geometry are established research directions. This experiment therefore does **not** assume novelty. Its purpose is to determine whether the specific pressure-Hessian coupling closes the unresolved estimate in our stack.

Recent work also studies pressure criteria and coarse-grained pressure/flux depletion, reinforcing that pressure can carry useful structural information but does not by itself establish global regularity.

## Acceptance criteria

A8 is accepted only if it produces:

- an exact pressure/strain identity;
- a scale-critical coercive inequality;
- explicit treatment of the pressure nonlocality;
- zero-safe treatment of vorticity direction;
- adversarial finite-mode tests;
- no circular use of a regularity criterion;
- independent verification.

Otherwise classify as `CLOSED / NOT_PROVEN` or `PARTIAL / NOT_PROVEN` with the exact obstruction recorded.

## Current hypothesis

**H8:** Pressure-Hessian feedback may supply the missing coercive control of sustained vortex stretching.

**Prior:** unknown.

**Status:** NOT_PROVEN.
