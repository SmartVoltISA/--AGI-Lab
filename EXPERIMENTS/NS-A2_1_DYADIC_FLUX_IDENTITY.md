# NS-A2.1 — Dyadic Flux Identity Target

**Status:** OPEN / NOT_PROVEN  
**Date:** 2026-09-10  
**Parent:** NS-A2

## Research target

For divergence-free 3D Navier–Stokes, derive the exact shellwise balance for

`E_j = 1/2 ||u_j||_2^2`

and separate the nonlinear contribution into transfers between frequency shells and genuine boundary production terms.

The desired outcome is an identity, not an inequality guessed from dimensional analysis.

## Acceptance condition

A candidate flux decomposition is useful only if:

1. every term is explicitly defined;
2. the sum over shells reproduces the standard energy balance;
3. cancellations are algebraic and do not assume the conclusion;
4. constants are uniform under finite-shell truncation;
5. the passage from truncated sums to the full solution is justified;
6. any claimed critical estimate survives rescaling.

## Falsification condition

Reject the branch if the apparent cancellation disappears after including nonlocal interactions, pressure projection, cutoff terms, or the limit over shell number.

## Current state

No new theorem is claimed. This file records the next exact derivation required by NS-A2.

`NOT_PROVEN ≠ FALSE`
