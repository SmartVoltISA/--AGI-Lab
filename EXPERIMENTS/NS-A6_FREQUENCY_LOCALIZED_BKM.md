# NS-A6 — Frequency-Localized BKM Attack

**Status:** OPEN / NOT_PROVEN  
**Parent:** NS-A5  
**Date:** 2026-09-10

## Objective

Attack the continuation threshold through the frequency-localized BKM mechanism rather than a global BMO or pointwise estimate.

Published work shows that 3D Navier–Stokes admits BKM-type criteria localized to Fourier modes below a critical frequency, with the critical frequency tied to the relevant time scale. This is an established criterion, not a new discovery. The research question for Ω/AGI-Lab is narrower:

> Can the exact frequency-localized continuation mechanism be connected to the dyadic energy-transfer structure already derived in NS-A2, in a way that exposes a new independently provable obstruction or estimate?

Reference facts are treated as external mathematical background, not as evidence for a new result.

## Known mechanism

For smooth 3D incompressible Navier–Stokes,

`∂_t u + (u·∇)u = -∇p + νΔu`, `∇·u=0`.

The vorticity equation is

`D_t ω = Sω + νΔω`.

The BKM continuation threshold involves time accumulation of high vorticity. Frequency-localized criteria show that one does not necessarily need to control the entire Fourier spectrum uniformly at every instant; only a suitable low-frequency window needs to be controlled, with the window depending on the time scale.

## New research question

Let `J(t)` be a time-dependent critical shell index and define

`ω_{≤J(t)} = Σ_{j≤J(t)} Δ_j ω`.

Investigate whether the continuation condition can be expressed as a coupled bound of the form

`∫_0^T ||ω_{≤J(t)}(t)||_X dt < ∞`

together with a separately controlled high-frequency flux/dissipation remainder.

The key point is that the moving cutoff may allow the exact conservative shell-transfer identity from A2 to enter the continuation argument.

## Candidate hypotheses

### H6.1 — Moving-cutoff continuation

There exists a scale-selection rule `J(t)` determined only by observable solution quantities and viscosity such that low-frequency vorticity control plus viscous control of shells above `J(t)` implies continuation.

### H6.2 — Flux-controlled remainder

The high-frequency remainder can be bounded by the cumulative outward shell flux plus viscous dissipation, with constants uniform as `J(t)→∞`.

### H6.3 — Critical-window cancellation

Dangerous stretching inside the low-frequency window admits a cancellation after summing the relevant shells, leaving only a boundary flux term at `J(t)` plus dissipative terms.

### H6.4 — Obstruction

Construct a finite-shell or multi-shell configuration where the low-frequency continuation quantity remains bounded but the high-frequency remainder grows without the required flux/dissipation compensation. Such a construction would reject H6.2/H6.3.

## Exact identities available from A2

For dyadic kinetic-energy shells,

`dE_j/dt = Π_j - ν||∇u_j||_2²`,

with

`Σ_j Π_j = 0`.

Thus nonlinear transport redistributes kinetic energy between scales while viscosity removes energy.

This identity alone does **not** control enstrophy and cannot be promoted to a continuation estimate without a new coercive inequality.

## Adversarial tests

1. Single moving shell crossing `J(t)`.
2. Narrow-band concentration immediately above `J(t)`.
3. Many-shell accumulation above the cutoff.
4. High-high → low transfer.
5. Low-high → high transfer.
6. Rapid time variation of `J(t)`.
7. Rescaling `u_λ(x,t)=λu(λx,λ²t)`.
8. Cutoff-independent constants as `J→∞`.
9. Pressure/nonlocal interactions crossing the cutoff.
10. A scenario where the low-frequency criterion is satisfied but the full BKM integral is not visibly controlled.

## Hard acceptance criteria

A successful new result requires:

- exact NS scaling;
- precise definition of `J(t)`;
- explicit continuation theorem or a rigorous reduction to one;
- explicit treatment of the moving-cutoff derivative/commutator;
- control of all triadic interactions crossing the cutoff;
- uniform constants;
- no hidden use of the desired regularity;
- independent verification of every nontrivial inequality.

## Important boundary

The published frequency-localized BKM criterion itself cannot be claimed as our discovery. Our only claim can be a new derivation, reduction, counterexample, or connection to the A2 flux framework if independently established.

## Current decision

**NOT_PROVEN.**

The branch is retained because it targets the exact gap left by A2: a mechanism that turns scale-localized information into a continuation statement without requiring a global pointwise bound on vorticity.

## References

- Luo, X., *A Beale–Kato–Majda Criterion with Optimal Frequency and Temporal Localization*, Journal of Mathematical Fluid Mechanics 21 (2019).
- Bradshaw, Z. & Grujić, Z., *Frequency Localized Regularity Criteria for the 3D Navier–Stokes Equations*, Archive for Rational Mechanics and Analysis 224 (2017).
