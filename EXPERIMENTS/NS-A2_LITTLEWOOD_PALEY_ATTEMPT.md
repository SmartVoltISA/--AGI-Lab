# NS-A2 — Littlewood–Paley Critical-Flux Attempt

**Status:** NOT_PROVEN  
**Date:** 2026-09-10  
**Experiment:** EXP-0013  
**Parent:** NS-A1  
**Scope:** 3D incompressible Navier–Stokes, smooth solutions, unforced case for the core estimate.

## 1. Objective

NS-A1 isolated the bottleneck: control vortex stretching without losing the Navier–Stokes scaling. NS-A2 tests whether a dyadic decomposition can expose a cancellation or flux bound that closes at critical scale.

The target is **not** to assume regularity. The target is to derive an estimate of the form

`dX/dt + D <= C X`

for a scale-critical quantity `X`, or another inequality that prevents concentration of high frequencies.

## 2. Dyadic decomposition

Let `Δ_j` denote homogeneous Littlewood–Paley projections and write

`u = Σ_j u_j`, `ω = Σ_j ω_j`.

The nonlinear term in the vorticity equation is

`N = (ω·∇)u`.

Projecting onto frequency shell `j` gives

`Δ_j N = Δ_j[(ω·∇)u]`.

A Bony-type decomposition separates interactions into low–high, high–low and comparable-frequency pieces.

Schematically:

`N = T_ω(∇u) + T_{∇u}(ω) + R(ω,∇u)`.

The hope is that the transport structure cancels enough of the worst interactions when summed against `ω_j`.

## 3. Candidate critical estimate

Define a weighted dyadic quantity

`X_s(t) = Σ_j 2^{2sj} ||u_j||_2^2`.

For 3D Navier–Stokes the scaling suggests the critical Sobolev index `s = 1/2` for `u`.

Candidate claim H2.1:

`|Σ_j <Δ_j((ω·∇)u), ω_j>| <= C X_{1/2}(t)^{1/2} D_{1/2}(t)`

with a coefficient that can be absorbed by viscosity, where `D_{1/2}` is the corresponding dissipative dyadic quantity.

If this were true with the correct endpoint structure, it could potentially yield a continuation estimate.

## 4. Scaling stress test

Under the Navier–Stokes scaling

`u_λ(x,t) = λ u(λx, λ²t)`,

`||u_λ||_{Ḣ^{1/2}}` is invariant.

So the candidate quantity has the correct dimensional scaling.

This is necessary but not sufficient.

## 5. Falsification attempt

The dangerous contribution is a high-frequency mode interacting with a much lower-frequency strain. A generic product estimate produces terms schematically like

`Σ_j 2^{j/2} ||u_j||_2 · ||∇u_{<j-2}||_∞ · ||ω_j||_2`.

Controlling the low-frequency gradient by a critical norm requires an endpoint embedding that is not available in the required form. Replacing it by a stronger norm introduces supercritical information.

Likewise, the comparable-frequency remainder can be bounded by standard product estimates, but the resulting constant depends on a norm stronger than the critical quantity alone.

Therefore the desired closed estimate has **not** been obtained.

**Result:** H2.1 NOT_PROVEN.

## 6. Important partial result

The dyadic decomposition changes the problem from an undifferentiated global stretching term into identifiable interaction classes:

1. low–high strain/stretching;
2. high–low transport/stretching;
3. comparable-frequency interactions;
4. possible cancellation between neighboring shells.

This is useful structural decomposition, but it is not yet mathematical progress toward the Millennium claim unless one interaction class can be controlled more sharply than the generic estimate.

**Classification:** PARTIAL STRUCTURAL PROGRESS, not VERIFIED_PROGRESS.

## 7. New candidate H2.2 — flux cancellation

Instead of bounding every dyadic interaction absolutely, test whether the shell-to-shell transfer satisfies a signed flux relation. Define a nonlinear flux `Π_j` through frequency `2^j` and seek

`Σ_j Π_j = 0`

or a telescoping identity in the inviscid nonlinear part, leaving viscosity as the only net high-frequency sink.

The key question is stronger:

> Can the potentially dangerous positive production of enstrophy be represented as an internal redistribution across scales, with no uncontrolled creation at the top of the spectrum?

This must be tested without assuming smoothness beyond the finite stage of the argument.

**Status:** OPEN.

## 8. Adversarial checks

Any future flux claim must survive:

- arbitrary sign of vortex stretching;
- concentration into a narrow frequency band;
- long low–high frequency separation;
- cancellation failure for nonlocal interactions;
- endpoint Besov/Sobolev losses;
- rescaling by `u -> u_λ`;
- finite-shell truncation followed by a uniform-in-cutoff limit.

A bound that works only at fixed numerical resolution is not accepted.

## 9. Decision

NS-A2 does **not** solve Navier–Stokes.

It also does not justify claiming that critical regularity follows from Littlewood–Paley theory alone. The useful output is a sharper research tree: attack the frequency flux rather than trying to bound the full stretching term blindly.

**Decision:** preserve branch; promote only a rigorously derived flux identity/estimate.

## 10. Next branch

**NS-A2.1 — Dyadic flux identity:** derive the exact projected energy/enstrophy balance and identify which nonlinear terms telescope.

**NS-A2.2 — Nonlocal interaction bound:** test whether separated scales admit a stronger estimate than the generic product inequality.

**NS-A2.3 — Critical Besov route:** test borderline `B^{1/2}_{2,1}` or related norms while explicitly checking endpoint assumptions.

**NS-A2.4 — Counterexample generator:** construct finite-dimensional divergence-free Fourier fields that maximize each proposed interaction inequality and search for its sharp scaling.

**Final classification:** `NOT_PROVEN`.
