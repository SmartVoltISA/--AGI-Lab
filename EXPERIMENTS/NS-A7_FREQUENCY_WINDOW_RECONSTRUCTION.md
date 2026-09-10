# NS-A7 — Frequency-Window Continuation Reconstruction

**Status:** OPEN / NOT_PROVEN  
**Parent:** EXP-0013 / NS-A6  
**Date:** 2026-09-10

## Objective

Reconstruct the mathematical mechanism behind frequency-localized Navier–Stokes continuation criteria, then isolate exactly what is already known and what would be required for a genuinely new result.

This is **not** a claim of solving the Millennium Prize problem.

## External baseline

Luo (2019) established a Beale–Kato–Majda-type criterion with optimal frequency and temporal localization. The criterion controls Fourier modes below a critical frequency at each time scale and uses cutoff dissipation and energy estimates at small scales.

Bradshaw–Grujić (2017) established frequency-localized regularity criteria in Littlewood–Paley windows and emphasized the role of high frequencies near a possible singular time.

These results are treated as baseline mathematics, not as new discoveries of Ω/SPACE.

## Core reconstruction

Let

`u_j = Δ_j u`, `λ_j = 2^j`,

and let a low-frequency cutoff be

`u_{≤J} = Σ_{j≤J} u_j`.

The natural localized energy has the schematic form

`E_{≤J}(t) = 1/2 ||u_{≤J}(t)||_2^2`.

For a fixed cutoff,

`dE_{≤J}/dt = -Π_{≤J} - ν||∇u_{≤J}||_2^2`,

where `Π_{≤J}` is the nonlinear transfer across the frequency boundary.

For a time-dependent cutoff, an additional term appears:

`C_J(t) = <(∂_t P_J)u,P_Ju>`.

Therefore a valid moving-window argument needs three separate controls:

1. cutoff variation;
2. nonlinear crossing flux;
3. high-frequency remainder/dissipation.

## Scaling

Under Navier–Stokes scaling

`u_λ(x,t)=λu(λx,λ²t)`,

frequency and time must transform consistently:

`Λ_λ(t)=λΛ(λ²t)`.

A parabolic critical scale has the form

`Λ(t) ~ C [ν(T-t)]^{-1/2}`.

For this scale,

`|Λ'/Λ|/(νΛ²) = 1/(2C²)`.

Thus the cutoff-variation term has the same parabolic dimensional order as viscosity, but its relative coefficient can be reduced by increasing the cutoff normalization `C`. This is only a scale observation; it is not a complete absorption estimate because the multiplier may degenerate near the cutoff edge.

## The actual nonlinear obstacle

For a self-adjoint multiplier `P`, incompressibility gives

`<P((u·∇)u),Pu> = <[P,u·∇]u,Pu>`.

Hence the moving-window energy identity has the exact structure

`dE_P/dt = -<[P,u·∇]u,Pu> - ν||∇Pu||_2² + <(∂_tP)u,Pu>`.

The commutator contains all triadic interactions crossing the frequency boundary.

It cannot be identified with one-way high-frequency creation. In particular, high-high → low interactions are allowed, as are low-high → high interactions. Signed cancellation is essential.

## What would count as a new closure

A successful new result would need a scale-critical inequality of the form

`|<[P,u·∇]u,Pu>| ≤ ε ν||∇Pu||_2² + F_critical(t) E_P(t)`

with `F_critical` controlled by data already available at the continuation threshold, uniformly in the cutoff scale.

The following shortcuts are rejected:

- replacing the commutator by an unsigned flux;
- assuming monotone transfer from low to high frequencies;
- using a stronger norm that already implies regularity;
- choosing a cutoff from information about the unknown singularity;
- hiding constants that depend on the cutoff scale;
- circularly assuming the continuation estimate being proved.

## A7 test matrix

### A7-T01 — Scaling
Verify every candidate estimate under Navier–Stokes scaling.

### A7-T02 — Single shell
Put energy in one dyadic shell near the cutoff. Reject estimates that fail uniformly there.

### A7-T03 — Two-shell cancellation
Test low-high and high-high interactions with opposite signs to detect false unsigned-flux bounds.

### A7-T04 — Many-shell accumulation
Test whether a constant grows with the number of active shells.

### A7-T05 — Cutoff edge
Test smooth multipliers near points where the cutoff tends to zero.

### A7-T06 — Time-localized concentration
Concentrate energy in a short interval near `T` and test temporal exponents.

### A7-T07 — Critical-window sufficiency
Ask whether bounded low-frequency information alone gives the required nonlinear estimate without importing a known theorem as a black box.

### A7-T08 — Circularity
Check whether any proposed bound implicitly assumes `∫||ω||∞dt < ∞` or an equivalent continuation criterion.

## Current conclusion

The frequency-window route is mathematically legitimate and closely aligned with established regularity theory, but reconstruction alone does not produce a new global regularity theorem.

**Current classification: OPEN / NOT_PROVEN.**

The decisive next step is an explicit commutator estimate and adversarial shell construction. If the estimate fails, record the obstruction. If it survives all tests, attempt a rigorous scale-uniform closure.
