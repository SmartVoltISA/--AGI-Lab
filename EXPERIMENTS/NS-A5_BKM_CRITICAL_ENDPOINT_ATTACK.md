# NS-A5 — BKM Critical Endpoint Attack

**Status:** OPEN / NOT_PROVEN  
**Parent:** NS-A4  
**Date:** 2026-09-10

## Objective

Open a genuinely new branch rather than rearranging the failed pointwise cubic, dyadic-flux, or static-alignment estimates.

The Beale–Kato–Majda continuation mechanism says, informally, that loss of smoothness is tied to accumulation of sufficiently strong vorticity in time. The research question here is whether that continuation threshold can be controlled by a scale-critical quantity already exposed by the A2 branch, or whether the endpoint necessarily loses information.

For smooth 3D incompressible Navier–Stokes,

`∂_t u + (u·∇)u = -∇p + νΔu`, `∇·u=0`.

The vorticity equation is

`D_t ω = Sω + νΔω`.

A continuation route of BKM type asks whether a bound of the form

`∫_0^T ||ω(t)||_∞ dt < ∞`

can be forced by another quantity with the correct scaling.

## Why this is new

A2 showed that exact energy transfer across dyadic shells is conservative but did not yield a critical high-frequency bound.  
A3 showed that static strain/vorticity alignment does not close the problem and that evolving alignment introduces nonlocal strain terms.  
A4 failed to establish a coercive bridge from stretching to energy flux.

A5 therefore attacks the continuation threshold itself.

## Candidate routes

### H5.1 — Critical Sobolev endpoint

Test whether a critical norm such as `||u||_{Ḣ^{1/2}}` can control the time integral required by continuation.

Immediate scaling check: `Ḣ^{1/2}` is invariant under Navier–Stokes scaling, but the pointwise quantity `||ω||_∞` is supercritical. A direct instantaneous inequality cannot be accepted merely because both quantities are finite for smooth solutions.

### H5.2 — Critical Besov endpoint

Test a route through critical Besov spaces, especially norms built from dyadic `L^p` blocks near the `L^3` scaling line.

Acceptance requires an actual continuation estimate with constants uniform in the shell cutoff. Endpoint accumulation (`q=∞` versus summability in `q`) must be handled explicitly.

### H5.3 — Logarithmic bridge

Test whether a logarithmic inequality can bridge a critical norm to the BKM quantity without secretly introducing a supercritical norm whose growth is exactly the original obstruction.

A schematic candidate is

`||∇u||_∞ <= C(1 + ||ω||_{BMO} log(e + ||u||_{X}/||ω||_{BMO}))`

for an appropriate critical `X`.

This is only a research template, not an asserted theorem in this document. Every functional inequality must be sourced and independently checked before use.

### H5.4 — Contrapositive obstruction

Instead of proving regularity, attempt to construct a mathematically consistent concentration scenario in which every proposed critical control remains bounded while the BKM quantity diverges.

A successful obstruction would reject that proposed bridge and sharpen the target.

## Hard acceptance criteria

A candidate survives only if all of the following are established:

1. exact Navier–Stokes scaling;
2. precise function spaces and norms;
3. every interpolation/product/commutator estimate stated with hypotheses;
4. no hidden stronger norm equivalent to the unknown regularity assumption;
5. uniformity under high-frequency truncation;
6. a genuine time-integrated continuation estimate or a rigorous reduction to a known criterion;
7. no circular use of smoothness beyond the local interval of derivation;
8. independent verification of every nontrivial inequality.

## Adversarial attacks

- narrow-band high-frequency concentration;
- many-shell accumulation;
- endpoint `q=∞` accumulation;
- rescaling by `u_λ(x,t)=λu(λx,λ²t)`;
- concentration in time near a candidate singular time;
- bounded critical norm with unbounded pointwise vorticity;
- pressure/nonlocal singular-integral effects;
- constants that diverge as cutoff `J→∞`;
- logarithmic inequalities whose logarithm hides the original supercritical quantity.

## Current analytical result

The scaling test already rejects the naive idea that a bounded instantaneous critical `Ḣ^{1/2}` quantity automatically supplies the BKM integral. Criticality alone is insufficient: the continuation quantity contains an additional concentration-in-time and high-frequency endpoint requirement.

The logarithmic/BMO route remains potentially meaningful, but it must be converted from a schematic inequality into an exact theorem with hypotheses and then checked against the full Navier–Stokes evolution. No such closure has been established here.

## Decision

No regularity proof, blow-up proof, or Millennium solution has been obtained.

**Classification: NOT_PROVEN.**

The branch is retained because it changes the question from “can we bound stretching pointwise?” to “can a critical spacetime control force the continuation threshold to remain finite?”
