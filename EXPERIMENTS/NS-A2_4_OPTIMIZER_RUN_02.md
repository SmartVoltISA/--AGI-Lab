# NS-A2.4 — Fourier Optimizer Run 02

**Status:** INCONCLUSIVE  
**Date:** 2026-09-10  
**Parent:** NS-A2.4

## Change from Run 01

The optimizer was stress-tested with triad-aware initialization: candidate Fourier supports are seeded from closed triads `k+p+q=0`, rather than selecting unrelated modes. Multiple independent hill-climbs were run from these supports.

The objective was the dimensionless cubic vortex-stretching ratio

`R = |∫ ω·Sω dx| / ||ω||_2^3`.

This is an adversarial test of a candidate scale-independent inequality of the form

`|∫ω·Sω| ≤ C ||ω||_2^3`.

## Local results

Using 3 independent starts per cutoff:

| N | best R | mean R |
|---|---:|---:|
| 1 | 0.1110 | 0.1105 |
| 2 | 0.1343 | 0.1021 |
| 3 | 0.1149 | 0.1149 |

These are finite-dimensional numerical observations only.

## Interpretation

No frequency-growing violation was found in this small triad-aware search. The result does **not** establish the inequality, because:

- the search space is finite;
- the hill-climb is not guaranteed to find a global extremum;
- the tested ratio itself may be bounded for structural reasons unrelated to Navier–Stokes regularity;
- a bound on this cubic ratio alone is not the missing global regularity estimate.

Therefore the candidate is **not rejected**, but also **not accepted**.

## Important correction

This run exposes a methodological distinction: even if a universal cubic inequality exists, it has the same superlinear enstrophy-growth character identified in NS-001. Consequently it cannot by itself close global regularity.

The next target should therefore be a genuinely critical **time-integrated/dyadic flux estimate**, not merely a bounded cubic ratio.

## Reproducibility

Seed base: `20260910 + N`.  
Triad-aware support generation.  
Offline NumPy computation.  
No canonical writes.

**Classification: INCONCLUSIVE / CANDIDATE NOT REJECTED.**

`NOT_PROVEN ≠ FALSE`
