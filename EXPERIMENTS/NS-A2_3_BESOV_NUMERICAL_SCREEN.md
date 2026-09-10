# NS-A2.3 — Numerical Besov/Scaling Screen

**Status:** EXECUTED / INCONCLUSIVE  
**Date:** 2026-09-10  
**Parent:** NS-A2.3 Critical Besov Route

## Purpose

Perform a small offline spectral screen to check whether finite Fourier fields immediately violate the cubic vortex-stretching control suggested by critical scaling.

## Test

Random divergence-free Fourier fields were generated on periodic grids with resolutions `N=8,12,16`. For each field we evaluated

`R = |<ω,Sω>| / <|ω|²>^(3/2)`

where `ω=curl(u)` and `S=(∇u+∇uᵀ)/2`.

Five random fields were sampled at each resolution.

Observed maximum ratios:

- `N=8`: approximately `0.01118`
- `N=12`: approximately `0.01756`
- `N=16`: approximately `0.00543`

These values do **not** establish a universal inequality; they only show that this small random sample did not immediately produce a violation of the dimensionless cubic control.

## Critical warning

The test is deliberately weak. Random sampling is not optimization, does not cover the full Fourier coefficient space, and cannot prove a bound. Resolution dependence is also non-monotone in this sample.

Therefore the result is **INCONCLUSIVE**, not `SUPPORTED`.

## Research consequence

The earlier linear-looking target `|stretching| ≤ C ||ω||₂²` is dimensionally false as a universal scale-independent estimate. The cubic normalization above has the correct homogeneity for this local vortex-stretching functional, so it is a more meaningful adversarial target.

However, even a valid cubic estimate would normally give superlinear enstrophy growth and therefore would not by itself close global regularity. A successful route needs additional critical structure, depletion, flux control, or another coercive mechanism.

## Next step

Replace random sampling with an actual constrained optimizer over finite Fourier coefficients, then test dyadic/Besov quantities shell-by-shell and across increasing maximum frequency.

`INCONCLUSIVE ≠ TRUE`
