# NS-A2.4 — Fourier Counterexample Search

**Status:** EXECUTED / CANDIDATE REJECTED  
**Date:** 2026-09-10  
**Parent:** NS-A2

## Purpose

Before accepting a critical dyadic inequality, actively search for divergence-free finite Fourier fields that make the proposed nonlinear interaction large relative to the proposed control norm.

## Candidate attacked

The naive universal estimate

`∫ ω·Sω dx ≤ C ||ω||_2²`

with a constant `C` independent of spatial scale.

Here `ω=∇×u` and `S=(∇u+(∇u)^T)/2`.

## Test family

Periodic finite Fourier fields were generated with

`u(x)=Σ a_k exp(i k·x)`

subject to `k·a_k=0` and the conjugate symmetry needed for a real field. Random divergence-free amplitudes were generated with fixed seed and then the complete configuration was rescaled spatially by factors `m=1,2,4,6`.

The ratio tested was

`R = (∫ω·Sω dx) / ||ω||_2²`.

A numerical violation is sufficient to reject the universal candidate; absence of a violation is not a proof.

## Result

A positive witness was found by deterministic random search (seed 123, 200 configurations). For the same field shape under spatial rescaling:

| spatial scale m | R |
|---:|---:|
| 1 | 0.2237537712 |
| 2 | 0.4475075424 |
| 4 | 0.8950150849 |
| 6 | 1.3425226273 |

The ratio grows linearly with the spatial frequency scale for this witness.

## Classification

**REJECTED — universal scale-independent candidate is false.**

The failure is also consistent with the Navier–Stokes scaling obstruction: the proposed bound compares a quantity with one extra spatial derivative against `||ω||_2²`, so a scale-independent constant cannot be expected.

## What this does NOT show

This rejects only the specific inequality above. It does **not** produce a Navier–Stokes singularity, does not disprove regularity, and does not establish any Millennium Prize result.

## Next target

Attack a genuinely scale-compatible critical quantity instead of the dimensionally inconsistent estimate. Priority branches:

1. critical Besov/dyadic flux bounds;
2. geometric depletion of vortex stretching;
3. shell-to-shell flux inequalities with scale-normalized quantities;
4. adversarial searches for configurations saturating or violating each proposed critical bound.

**NOT_PROVEN remains the global status of the Navier–Stokes problem.**
