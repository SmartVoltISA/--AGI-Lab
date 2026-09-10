# NS-A6.1 — Moving Cutoff Analytical Attack

**Status:** OPEN / NOT_PROVEN  
**Parent:** NS-A6_FREQUENCY_LOCALIZED_BKM.md  
**Date:** 2026-09-10

## Target

Test H6.3: whether a time-dependent dyadic cutoff can convert the low-frequency continuation mechanism into a boundary-flux identity compatible with NS-A2.

Let

`P_J(t) = Σ_{j≤J(t)} Δ_j`.

For a fixed cutoff,

`d/dt (1/2 ||P_J u||_2²) = -<(u·∇)u,P_Ju> - ν||∇P_Ju||_2²`.

For a moving cutoff, the formal differentiation introduces an additional cutoff-variation term. A rigorous treatment therefore cannot simply replace `J` by `J(t)` in the fixed-cutoff identity.

## First obstruction

If `J(t)` changes continuously through a smooth spectral multiplier, differentiation produces a commutator/weight-derivative contribution. If it changes discretely between dyadic shells, the energy observable itself jumps between projections.

Therefore any proposed proof must specify one of:

1. a smooth time-dependent Fourier multiplier `P_{≤Λ(t)}`;
2. a piecewise-constant shell cutoff with explicit jump accounting;
3. a stopping-time construction where the cutoff changes only at controlled events.

## Candidate smooth cutoff

Take `P_Λ(t)` with Fourier multiplier `χ(|ξ|/Λ(t))`, where `χ` is smooth and compactly supported. Then

`d/dt ||P_Λu||_2²`

contains both the Navier–Stokes contribution and

`< (∂_t P_Λ)u, P_Λu >`.

The second term is not part of the A2 conservative flux and must be controlled separately.

## Adversarial test

Choose a field concentrated near the moving cutoff `|ξ|≈Λ(t)`. Then even a small cutoff speed `|Λ'(t)|` can make the cutoff-variation term comparable to the shell energy itself.

This means H6.3 cannot be accepted merely from a fixed-cutoff flux identity.

## Triadic boundary issue

The nonlinear term contains interactions whose input frequencies lie on opposite sides of the cutoff and whose output frequency crosses the cutoff. In particular, high-high → low interactions show that outward flux is not equivalent to high-frequency creation.

Thus a successful estimate must classify all triads crossing the moving boundary rather than assume one-way transfer.

## Scaling check

Under

`u_λ(x,t)=λu(λx,λ²t)`,

frequencies scale as `Λ→λΛ` and time as `t→λ^{-2}t`. Therefore a valid cutoff law must transform as

`Λ_λ(t)=λ Λ(λ²t)`

up to the chosen normalization.

Any rule failing this test is rejected immediately.

## Current result

The moving-cutoff formulation exposes a genuine additional term absent from A2. This is a real obstruction, not a proof of impossibility.

**Classification: PARTIAL / NOT_PROVEN.**

## Next test

Derive the smooth-multiplier identity exactly and determine whether the cutoff-variation term can be absorbed into viscosity or the critical low-frequency control. If not, construct an explicit finite-mode counterexample.
