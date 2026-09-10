# NS-A3.1 — Dynamical Vorticity/Strain Alignment

**Status:** PARTIAL / NOT_PROVEN  
**Parent:** NS-A3  
**Date:** 2026-09-10

## Question

Can the evolution of the vorticity direction produce a quantitative depletion of vortex stretching strong enough to close the 3D Navier–Stokes regularity problem?

## Exact starting identities

For smooth incompressible Navier–Stokes,

`D_t ω = Sω + νΔω`,

where `D_t = ∂_t + u·∇`.

Write, wherever `|ω|>0`,

`ω = ρ ξ`, `ρ=|ω|`, `|ξ|=1`.

Then

`D_t ρ = (ξ·Sξ)ρ + ν ξ·Δω`.

Using

`Δω = Δ(ρξ) = ξΔρ + 2∇ρ·∇ξ + ρΔξ`,

and `ξ·Δξ = -|∇ξ|²`, one obtains

`D_t ρ = (ξ·Sξ)ρ + ν[Δρ - ρ|∇ξ|² + 2∇ρ·∇ξ·ξ]`.

The exact vorticity-direction equation has the schematic form

`D_t ξ = (I-ξ⊗ξ)Sξ + ν ρ^{-1}(I-ξ⊗ξ)Δω`.

Thus the strain changes both the magnitude and direction of vorticity, while diffusion contains a geometric penalty involving directional variation.

## Key observation

The desired mechanism would require a theorem saying that dangerous positive alignment

`a = ξ·Sξ`

cannot remain large in a scale-critical spacetime sense without generating enough directional variation/diffusion to compensate it.

The identities above show where such compensation could enter, but they do **not** establish it.

## Candidate H3.1-D — Dynamical depletion

Seek a scale-compatible inequality of schematic form

`∫_0^T ∫ a_+ |ω|^2 dx dt ≤ C * critical_control(u_0,T)`

or a stronger relation coupling `a_+` to `|∇ξ|²` and viscous dissipation.

Any useful inequality must avoid assuming the very regularity it is intended to prove.

## Immediate obstruction

The factor `ρ^{-1}` in the direction equation becomes singular near vortex zeros. Therefore an argument based directly on pointwise `ξ` needs a zero-vorticity-safe formulation, such as weighted quantities, regularized direction fields, or integral identities.

This is a genuine technical boundary, not a reason to declare failure of the overall idea.

## Adversarial requirements

A candidate must survive:

1. nearly constant vorticity direction;
2. rapid directional variation;
3. regions where `|ω|` is small;
4. strong positive strain alignment;
5. concentration at high frequency;
6. rescaling under Navier–Stokes scaling;
7. nonlocal pressure/strain effects;
8. temporal concentration.

## Current conclusion

We obtained the exact structural decomposition needed to formulate a dynamical alignment attack, including the appearance of directional-gradient dissipation. We did **not** derive the critical inequality needed for global regularity.

**Classification: PARTIAL / NOT_PROVEN.**

## Next branch

Do not attempt another static eigenvalue inequality. The next mathematical target is a zero-safe weighted alignment functional whose evolution can be integrated and compared directly with viscous dissipation and critical flux.
