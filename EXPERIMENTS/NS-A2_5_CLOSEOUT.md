# NS-A2.5 — Closeout

**Status:** CLOSED / NOT_PROVEN  
**Date:** 2026-09-10

## Result

The branch attacked a genuinely scale-critical, time-integrated nonlinear-flux route after the earlier pointwise enstrophy route was found insufficient.

The exact dyadic energy identity confirms conservative nonlinear transfer across scales, but that identity alone supplies no uniform bound on the high-frequency tail. The proposed critical time-integrated flux estimate was therefore tested as a hypothesis rather than assumed as a theorem.

Finite-mode scaling probes are useful as rejection tests: a frequency-growing dimensionless ratio would immediately kill a candidate normalization. Scaling consistency, however, is necessary rather than sufficient and cannot establish a universal inequality for arbitrary smooth solutions.

The central obstruction remains: obtaining a scale-critical estimate that is simultaneously uniform over shells, closes against viscosity, survives low-high/high-high/nonlocal interactions and temporal concentration, and implies a non-circular continuation criterion.

## What was established

1. The nonlinear kinetic-energy transfer is conservative across dyadic shells.
2. The Navier–Stokes scaling identifies the relevant critical regularity scale.
3. Pointwise cubic enstrophy control is not enough for global regularity.
4. A critical flux argument must control ultraviolet concentration, not merely total energy.
5. Finite Fourier searches can falsify bad candidate inequalities but cannot prove surviving ones.

## What was not established

- No universal critical time-integrated flux inequality.
- No global a priori bound sufficient for regularity.
- No continuation theorem derived from the candidate flux control.
- No singularity construction or counterexample to Navier–Stokes regularity.
- No `VERIFIED_SOLUTION` or `VERIFIED_PROGRESS` claim.

## Branch decision

**CLOSED — NOT_PROVEN.**

This branch is closed because the current attack did not produce a proof-grade closure. Its useful output is the narrowed bottleneck and the reusable adversarial criteria.

## Handoff

Future work should not simply repeat the same cubic estimate. New branches should require a genuinely new mechanism, for example:

- geometric depletion of vortex stretching;
- critical Besov/Lorentz endpoint structure with a rigorous continuation implication;
- conditional regularity converted into a contradiction under an independently established bound;
- construction of a rigorous obstruction/counterexample to a proposed estimate;
- formal verification only after a mathematically substantive candidate argument exists.

Any future claim must pass independent verification and the existing Guardian/SECURITY-TEST gates.

**Final classification: NOT_PROVEN.**
