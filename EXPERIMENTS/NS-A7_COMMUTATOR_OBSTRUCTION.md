# NS-A7.1 — Frequency-Window Commutator Attack

**Status:** CLOSED / NOT_PROVEN  
**Date:** 2026-09-10

## Exact identity

For a self-adjoint Fourier multiplier `P` and divergence-free `u`,

`<P((u·∇)u),Pu> = <[P,u·∇]u,Pu>`.

Therefore

`d/dt (1/2||Pu||_2²)
 = -<[P,u·∇]u,Pu>
   -ν||∇Pu||_2²
   +<(∂_tP)u,Pu>`.

This identity is exact at the formal smooth-solution level.

## Shell analysis

The commutator is a sum of triadic interactions. A candidate estimate that replaces it by a positive outward flux is invalid in general because the nonlinear transfer is signed and permits both directions across a frequency boundary.

A particularly dangerous configuration is high-high → low: two frequencies above the cutoff can generate an output below it. Conversely, low-high → high can move energy outward. Therefore the sign of the boundary transfer cannot be inferred from the location of the input frequencies alone.

## Critical estimate attempt

The desired structure would be

`|N_P| ≤ ε ν||∇Pu||_2² + F(t) ||Pu||_2²`,

with `F` at a scale-critical level and independent of the cutoff location.

The basic Hölder/Sobolev route gives bounds involving norms stronger than the critical continuation data. Those bounds therefore do not close the Millennium problem; they merely restate known conditional regularity mechanisms.

A dyadic Bony decomposition has the same issue at the endpoint: the paraproduct terms require either additional summability or a stronger norm. No scale-uniform critical closure was obtained here.

## Adversarial conclusions

### Single shell
No contradiction to the exact identity. It does, however, show that the cutoff boundary cannot be treated as a passive label.

### Two-shell signed interaction
Rejects an unsigned one-way flux model.

### Many-shell accumulation
A naive sum of absolute triad contributions is not scale-uniform; cancellation or stronger structure is required.

### Cutoff edge
Smooth multiplier estimates require care where the multiplier approaches zero. Pointwise absorption of the cutoff-variation term by the weighted dissipation is not automatic.

### Time concentration
A scale-critical temporal concentration cannot be excluded by dimensional analysis alone.

## Verdict

The moving frequency window does not yield a new regularity closure with the estimates currently available.

This is a **closed negative result for this attack formulation**, not a proof that no other frequency-localized argument can work.

**Classification: CLOSED / NOT_PROVEN.**

## What remains open

The remaining high-value direction is not to repeat the same cutoff estimate. It is to search for a genuinely new structural inequality that couples the nonlinear commutator to another coercive quantity—geometric depletion, pressure structure, or a new invariant/monotone functional—without assuming the desired regularity.
