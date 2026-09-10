# NS-A4 — Flux ↔ Vortex-Stretching Coupling

**Status:** OPEN / NOT_PROVEN  
**Date:** 2026-09-10

## Objective

Combine the strongest surviving structural facts from NS-A2 and NS-A3:

- dyadic nonlinear transport conserves total kinetic energy;
- enstrophy growth is driven by `G(t)=∫ω·Sω`;
- dangerous stretching is a geometric alignment phenomenon;
- critical regularity requires control uniform across scales.

The target is to determine whether positive vortex stretching can be quantitatively tied to a high-frequency energy/enstrophy flux in a way that viscosity can absorb.

## Exact identities

For a smooth periodic incompressible solution,

`d/dt (1/2 ||u||_2^2) = -ν ||∇u||_2^2`.

For vorticity,

`(1/2)d/dt ||ω||_2^2 = ∫ω·Sω dx - ν||∇ω||_2^2`.

For a dyadic velocity shell,

`dE_j/dt = Π_j - ν||∇u_j||_2^2`,

and

`Σ_j Π_j = 0`.

These identities live at different regularity levels. The missing bridge is a coercive estimate connecting the stretching term to scale-localized transfer.

## Candidate H4.1

There exists a scale-localized decomposition

`G = Σ_j G_j`

and a critical functional `K(t)` such that

`Σ_j (G_j)_+ ≤ C K(t) + ε ν||∇ω||_2^2`

with `K` integrable in time under a scale-critical bound.

This is only a hypothesis.

## Candidate H4.2 — Flux compensation

Dangerous positive stretching at shell `j` must be accompanied by measurable transfer into scales `>j`, so that cumulative stretching obeys a bound involving outward flux plus dissipation.

This would create the desired three-way relation:

`stretching → high-frequency transfer → viscous dissipation`.

## Immediate adversarial attack

The claim cannot use total energy conservation as evidence for enstrophy control. Energy can remain finite while higher derivatives concentrate.

It also cannot assume that every positive stretching event produces outward flux: triadic interactions may transfer energy both up and down scale.

Therefore the candidate must be formulated with signed fluxes and absolute-value/error terms whose scaling is explicitly controlled.

## Required tests

1. Single-shell concentration.
2. Low-high triads.
3. High-high-to-low transfer.
4. Nonlocal triads.
5. Opposite-sign shell transfers.
6. Strong local vortex alignment.
7. Temporal concentration.
8. Navier–Stokes rescaling.
9. Uniform ultraviolet cutoff.
10. Zero-vorticity regions.

## Acceptance

A positive result requires an analytic inequality with explicit constants and a non-circular continuation implication. Numerical experiments alone cannot advance the classification beyond exploratory evidence.

A single admissible counterexample rejects the universal candidate.

## Current status

No such coupling inequality has been established.

**Classification: NOT_PROVEN.**

## Safety / provenance

Offline mathematical research. No canonical SPACE writes and no automatic architectural promotion.
