# NS-001 — Navier–Stokes Growth Run 01

**Status:** NOT_PROVEN
**Date:** 2026-09-10
**Experiment:** EXP-0013
**Mode:** independent research attempt; no canonical write-back

## Target

For 3D incompressible Navier–Stokes

∂t u + (u·∇)u = −∇p + νΔu + f,   ∇·u = 0,

starting from smooth finite-energy data, determine whether a finite-time singularity can be proved to exist, or global regularity can be proved.

This run attempts both directions and accepts neither without an independently checkable closure.

## Seed hypothesis H1 — enstrophy closure

Let ω = ∇×u and E(t)=1/2∫|ω|² dx. Formally,

dE/dt = ∫ ω·(ω·∇)u dx − ν∫|∇ω|²dx + ∫ω·curl(f)dx.

The first term is vortex stretching. A useful upper estimate has the form

|∫ω·(ω·∇)u| ≤ C E^(3/2)

under suitable interpolation assumptions.

### Attempted conclusion

A superlinear differential inequality such as E' ≤ C E^(3/2)+F does **not** prove finite-time blow-up: it is only an upper bound and does not force the stretching term to be positive or large. Conversely, the estimate does not close global regularity because E^(3/2) is superlinear.

**Result:** H1 does not close the Millennium problem.

## Seed hypothesis H2 — force a positive stretching mechanism

Try to establish a universal lower bound

∫ω·(ω·∇)u dx ≥ c Φ(ω)

for a coercive nonnegative functional Φ.

### Falsification

No such sign condition follows from incompressibility alone. The stretching contribution depends on the geometry and alignment of ω with the strain tensor. Special configurations can suppress stretching, so a universal positive lower bound cannot be assumed.

**Result:** H2 rejected as a universal route.

## Seed hypothesis H3 — self-similar singularity

Use the Leray-type ansatz

u(x,t)=(T−t)^(-1/2) U(y),   y=x/(T−t)^(1/2),

with pressure p(x,t)=(T−t)^(-1)P(y).

Substitution gives the profile equation (after scaling ν=1)

−1/2 U − 1/2(y·∇)U +(U·∇)U = −∇P + ΔU,
∇·U=0.

A nontrivial admissible finite-energy profile would provide a concrete blow-up mechanism.

### Falsification target

The profile equation itself is not a construction. Any candidate U must satisfy the PDE, divergence constraint, regularity/integrability conditions, and the matching reconstruction back to the original variables. A numerical or symbolic approximate profile is insufficient unless the residual and all required estimates are rigorously controlled.

**Result:** no admissible profile constructed in this run; H3 remains NOT_PROVEN.

## Seed hypothesis H4 — grow a critical regularity estimate

The promising direction is not to guess a singularity but to seek a scale-critical quantity X(t) for which

X(t) finite on [0,T] ⇒ ||∇u||∞ is integrable on [0,T],

or an equivalent continuation criterion that closes using the Navier–Stokes structure.

The growth rule is: every proposed inequality must be checked for scaling, endpoint validity, domain assumptions, and whether it actually closes the nonlinear term.

### Current obstruction

The ordinary energy estimate controls ||u||₂, while the nonlinear regularity problem requires stronger control. A candidate estimate that merely reproduces a known supercritical bound is not progress.

**Result:** open branch; requires further candidate generation.

## Organism decision

The first-generation branches were not promoted to VERIFIED_PROGRESS.

- H1: **REJECTED AS A COMPLETE PROOF ROUTE** — inequality does not close.
- H2: **REJECTED** — required universal stretching sign is false/unjustified.
- H3: **NOT_PROVEN** — no admissible singular profile constructed.
- H4: **OPEN** — critical estimate search remains active.

## What counts as growth

A new branch may be promoted only if it supplies a genuinely new, independently checkable lemma, estimate, reduction, counterexample, or formally verified intermediate result. Model agreement, numerical pattern, or an elegant derivation is not sufficient.

## Next growth seeds

1. Dyadic/Littlewood–Paley decomposition of vortex stretching; search for a critical-frequency flux bound.
2. Geometric depletion: quantify whether restricted vortex-direction variation can force a subcritical estimate.
3. Search for a coercive modified enstrophy functional whose nonlinear production can be bounded at critical scaling.
4. Attempt adversarial counterexamples against each proposed closure before promotion.

## Final classification

**NOT_PROVEN.**

This run did not solve Navier–Stokes and did not establish a blow-up theorem. It did, however, eliminate three tempting but insufficient proof routes and isolate the current research bottleneck: a scale-critical closure controlling the nonlinear vortex-stretching mechanism.

`MODEL_CONFIDENCE ≠ MATHEMATICAL_VALIDITY`
`NOT_PROVEN ≠ FALSE`
`REJECTED_ROUTE ≠ PROBLEM_REJECTED`
