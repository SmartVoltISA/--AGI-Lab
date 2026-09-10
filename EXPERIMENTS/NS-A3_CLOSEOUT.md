# NS-A3 — Geometric Depletion Closeout

**Status:** CLOSED / NOT_PROVEN  
**Date:** 2026-09-10

## Outcome

The geometric route was formalized and attacked at its first decisive boundary.

The strain tensor is symmetric and trace-free, but this does not by itself suppress vortex stretching: `ω·Sω` can be positive when vorticity aligns with a positive strain eigendirection. Therefore trace-free geometry cannot serve as the missing regularity estimate on its own.

A finite-mode adversarial optimizer was added to search divergence-free Fourier fields for large normalized vortex-stretching configurations. Such computation can reject overly strong universal geometric inequalities, but survival of a finite search cannot establish a theorem.

The remaining potentially meaningful version is **dynamical depletion**: proving that the Navier–Stokes evolution cannot sustain sufficiently dangerous alignment/concentration for long enough to cause loss of regularity. That requires an analytic evolution inequality for a geometric observable, not a static alignment picture.

## Established boundary

- `tr S = 0` does not imply zero stretching.
- Pointwise alignment can be dangerous and must be controlled quantitatively.
- A universal pointwise angular gap cannot be assumed without proof.
- Finite-mode optimization is an adversarial rejection tool, not a proof engine.
- The real open target is a dynamical, scale-compatible depletion mechanism.

## Not established

- No global depletion estimate.
- No critical spacetime bound derived from alignment geometry.
- No continuation criterion obtained from the geometric route.
- No proof of global regularity or singularity.

## Decision

**CLOSED — NOT_PROVEN.**

Do not keep iterating static eigenvector inequalities under NS-A3. Any future geometric branch must begin with the evolution of the alignment observable and must survive the existing scaling, concentration, nonlocal-interaction, and falsification tests.

## Handoff

The strongest remaining research direction from this branch is a dynamical geometric identity/inequality, potentially combined with the critical flux framework from NS-A2.5. A candidate must demonstrate a real new coercive mechanism before promotion.
