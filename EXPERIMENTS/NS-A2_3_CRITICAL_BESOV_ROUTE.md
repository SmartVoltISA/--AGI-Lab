# NS-A2.3 — Critical Besov Route

**Status:** OPEN / NOT_PROVEN  
**Date:** 2026-09-10  
**Parent:** NS-A2 Littlewood–Paley

## Goal

Test whether a critical Besov formulation gives a genuinely scale-invariant route to control of the nonlinear Navier–Stokes term, while avoiding the false premise that shellwise energy cancellation itself implies regularity.

## Scaling

For 3D Navier–Stokes,

`u_λ(x,t)=λu(λx,λ²t)`.

The homogeneous Besov norm `||u||_{Ḃ^{-1+3/p}_{p,q}}` is scaling critical for velocity. A particularly important endpoint family is `Ḃ^{-1+3/p}_{p,q}` with `p>3`, together with the classical critical spaces around `L^3`.

The research target is not to assume a known regularity theorem as a solution. Instead we ask whether the dyadic dynamics can independently recover a closed continuation estimate from the equation.

## Dyadic equation

For `u_j=Δ_j u`,

`∂_t u_j + Δ_j((u·∇)u) = -∇p_j + νΔu_j`.

Taking the `L^p` or suitable mixed norm requires estimating

`Δ_j((u·∇)u)`

through low-high, high-low and comparable-frequency interactions.

## Candidate route B3.1 — Critical product closure

Seek a scale-uniform estimate of schematic form

`||Δ_j((u·∇)u)||_p ≤ C 2^j ||u||_X ||u_j||_p`

where `X` is a critical Besov norm whose coefficient can be integrated in time or absorbed by viscosity.

Acceptance requires:

1. exact scaling balance;
2. no hidden supercritical norm on the right;
3. summability over shells with constants independent of truncation;
4. a continuation criterion that actually follows from the estimate;
5. no circular use of regularity being proved.

## Immediate obstruction

Generic product estimates at critical endpoints are delicate. A bound that places one factor in an `L^∞`-type space is generally stronger than the critical information available from energy. Bernstein inequalities introduce powers of frequency, and summing them can lose precisely the derivative needed for closure.

Therefore the following implication is **not accepted** without proof:

`critical norm bounded ⇒ nonlinear term harmless`.

## Candidate route B3.2 — Flux in critical Besov norm

Instead of estimating each nonlinear term absolutely, search for a signed shell flux `Π_j` and a cumulative flux

`F_J = Σ_{j≤J} Π_j`.

The target is a bound in which dangerous positive transfer to high frequencies is compensated by viscosity or by a summable critical flux condition.

A successful result would need a quantitative statement such as

`sup_J |F_J| ≤ C(control quantities)`

with the control quantities critical and independently verified.

The exact dyadic energy identity from NS-A2.1 supplies the conservation structure but not this bound.

## Adversarial tests

Any proposed Besov closure must be tested against:

- narrow-band fields;
- low-high frequency separation;
- high-low interactions;
- nonlocal triads;
- endpoint `q=∞` accumulation;
- frequency rescaling;
- finite-shell truncations;
- divergence-free Fourier fields;
- fields with strong strain/vorticity alignment;
- configurations where shell flux changes sign.

## Current result

No independent closure theorem has been obtained.

The branch remains **NOT_PROVEN**. The useful advance is a sharper target: any successful route must control the nonlinear dyadic flux at critical scaling, not merely exploit total-energy cancellation.

## Next attack

Construct an explicit finite-mode optimizer for candidate critical Besov inequalities and search for frequency-dependent violations. If a candidate survives, derive its dyadic estimate symbolically and test whether the shell sum closes without an endpoint loss.

`NOT_PROVEN ≠ FALSE`
