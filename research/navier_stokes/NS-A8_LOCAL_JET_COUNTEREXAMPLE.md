# NS-A8 — Local-Jet Counterexample: Scalar Pressure Source Does Not Determine Stretching

**Status:** CLOSED / REFUTED (candidate hypothesis only)

**Scope:** Navier–Stokes / Euler local algebraic structure. This is **not** a global regularity result and does **not** solve or disprove the Millennium problem.

## 1. Candidate hypothesis attacked

A8 asked whether the scalar pressure-Poisson source

\[
Q = |S|^2 - \frac12|\omega|^2
\]

could provide a coercive control of the vortex-stretching scalar

\[
G = \omega^T S\omega.
\]

The proposed route would need the scalar pressure information to constrain the sign or magnitude of `G`.

We attack that claim at the smallest local level: one divergence-free velocity-gradient jet.

## 2. Construction

Take the trace-free symmetric strain matrix

\[
S = \operatorname{diag}(1,-1,0).
\]

Hence

\[
\operatorname{tr}S=0, \qquad |S|^2=2.
\]

For a prescribed vorticity vector `ω`, let the antisymmetric part be chosen so that

\[
A = \nabla u = S + \Omega(\omega),
\]

with

\[
\Omega_{ij}=-\frac12\epsilon_{ijk}\omega_k.
\]

Then `curl u = ω` and `tr A = 0`, so the affine field

\[
u(x)=Ax
\]

is incompressible.

Now compare two vorticities with exactly the same magnitude:

\[
\omega_+ = (\sqrt2,0,0),
\qquad
\omega_- = (0,\sqrt2,0).
\]

Thus

\[
|\omega_+|^2=|\omega_-|^2=2.
\]

## 3. Pressure source is identical

For both jets,

\[
Q=|S|^2-\frac12|\omega|^2
  =2-1=1.
\]

Therefore the scalar source entering the pressure Poisson equation is exactly the same:

\[
Q_+=Q_-=1.
\]

## 4. Stretching is opposite

For `ω+`, which is aligned with the `+1` eigenvector of `S`,

\[
G_+=\omega_+^T S\omega_+=2.
\]

For `ω-`, aligned with the `-1` eigenvector,

\[
G_-=\omega_-^T S\omega_-=-2.
\]

So we obtain

\[
\boxed{Q_+=Q_-=1,
\qquad G_+=+2,
\qquad G_-=-2.}
\]

The scalar pressure source is identical while the vortex stretching changes sign.

## 5. What this actually proves

This is a direct algebraic obstruction to the following candidate statement:

> **False candidate:** the scalar invariant `Q = |S|² - |ω|²/2` by itself determines, bounds, or sign-controls vortex stretching `ωᵀSω`.

It does not.

The missing information is the **orientation of `ω` relative to the strain eigenframe**. The scalar `Q` contains only magnitudes; `G` contains directional information.

This is stronger than a numerical counterexample: no optimizer, discretization, or finite-mode truncation is involved. It is an exact two-jet construction.

## 6. Important limitation

The affine fields `u(x)=Ax` are local jets, not finite-energy periodic Navier–Stokes solutions on `R³` or `T³`. Therefore this result **does not** establish any statement about global solution behavior or singularity formation.

It only kills the proposed local coercivity mechanism.

To promote this obstruction to a global functional obstruction, the next test would need a localized/divergence-free realization preserving enough of the same invariants while controlling the localization error.

## 7. A8 decision

**A8 scalar-pressure-source coercivity: REFUTED.**

The route cannot proceed from `Q` alone to a bound on vortex stretching.

The next legitimate target is therefore not another rearrangement of `Q`, but one of:

1. full pressure-Hessian information;
2. pressure + strain-eigenframe dynamics;
3. a localized divergence-free realization of the local-jet obstruction;
4. abandon the pressure route if no coercive bridge survives.

`NOT_PROVEN` remains the status of the Navier–Stokes regularity problem itself.
