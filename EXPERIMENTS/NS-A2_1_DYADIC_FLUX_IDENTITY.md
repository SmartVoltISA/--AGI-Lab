# NS-A2.1 — Exact Dyadic Energy-Flux Identity

**Status:** COMPLETED DERIVATION / NOT A REGULARITY PROOF  
**Date:** 2026-09-10  
**Parent:** NS-A2 Littlewood–Paley attempt

## 1. Goal

Derive the exact shellwise kinetic-energy balance for a Littlewood–Paley decomposition of 3D incompressible Navier–Stokes and identify precisely which nonlinear terms are pure inter-scale transfer and which terms could represent genuine accumulation at high frequency.

## 2. Setup

On the periodic torus, for smooth solutions,

`∂_t u + (u·∇)u = -∇p + νΔu`,  `∇·u=0`.

Let `Δ_j` be standard self-adjoint homogeneous Littlewood–Paley projectors and `u_j=Δ_j u`. Define `E_j=1/2||u_j||_2²`.

Applying `Δ_j` and taking the `L²` product with `u_j` gives

`dE_j/dt = -<Δ_j((u·∇)u),u_j> - ν||∇u_j||_2²`.

Pressure vanishes because `u_j` is divergence-free:

`<Δ_j∇p,u_j>=0`.

## 3. Exact shell transfer

By self-adjointness,

`<Δ_j((u·∇)u),u_j>=<(u·∇)u,u_j>`.

Define

`Π_j := -<(u·∇)u,u_j>`.

Then exactly

`dE_j/dt = Π_j - ν||∇u_j||_2²`.

`Π_j` is not sign-definite: it is a shell contribution of nonlinear transport, not a positive production term.

## 4. Global nonlinear cancellation

Summing over shells for a smooth field,

`Σ_j Π_j = -<(u·∇)u,u> = 0`.

Indeed,

`<(u·∇)u,u> = 1/2 ∫u·∇|u|² dx = 0`

by periodicity and incompressibility. Hence nonlinear transport redistributes kinetic energy but does not change total kinetic energy:

`d/dt (1/2||u||_2²) = -ν||∇u||_2²`.

## 5. Cutoff flux

Let `S_J=Σ_{j≤J}Δ_j` and `E_{≤J}=1/2||S_Ju||_2²`. Then

`dE_{≤J}/dt = -<(u·∇)u,S_Ju> - ν||∇S_Ju||_2²`.

Define the nonlinear outward flux from the low-frequency sector by

`Φ_J := <(u·∇)u,S_Ju>`.

Thus

`dE_{≤J}/dt = -Φ_J - ν||∇S_Ju||_2²`.

Because the total nonlinear contribution is zero, the same quantity equals the opposite nonlinear contribution of the complementary sector. Therefore `Φ_J` is a genuine inter-scale transfer across the cutoff, with sign determined by the convention above.

## 6. What this proves—and what it does not

The exact identity proves that nonlinear transport has a conservative scale-transfer structure. It does **not** provide a bound preventing transfer into arbitrarily high frequencies.

A regularity argument still needs a scale-uniform estimate controlling the high-frequency tail strongly enough to combine with viscous dissipation. Algebraic cancellation alone is insufficient.

## 7. Critical target

Under Navier–Stokes scaling

`u_λ(x,t)=λu(λx,λ²t)`,

`||u_λ||_{Ḣ^{1/2}}` is invariant. A tempting target is a uniform critical estimate schematically of the form

`|Φ_J| ≤ C X_{1/2}^{1/2} D_{1/2}`

with a dissipative quantity `D_{1/2}` absorbable by viscosity. The exact flux identity does not establish this estimate. Endpoint paraproduct interactions can require stronger norms or incur losses.

## 8. Adversarial checks

The identity must remain valid under:

1. arbitrary signs of individual shell transfers;
2. narrow high-frequency concentration;
3. separated low/high scales;
4. nonlocal triadic interactions;
5. endpoint Sobolev/Besov losses;
6. Navier–Stokes rescaling;
7. finite-shell truncation followed by `J→∞`;
8. pressure projection and divergence-free constraints.

The conservative cancellation survives these checks. The required coercive critical estimate remains unproved.

## 9. Result

**Classification: NOT_PROVEN.**

**Verified structural result:** nonlinear Navier–Stokes transport redistributes kinetic energy across scales and has exact global cancellation.

**Unresolved bottleneck:** a scale-critical bound preventing dangerous high-frequency concentration.

## 10. Next attack

Proceed to **NS-A2.4 Fourier counterexample search** against concrete candidate critical inequalities. A finite-mode numerical violation rejects the candidate universal inequality; absence of a violation is not a proof.

`NOT_PROVEN ≠ FALSE`
