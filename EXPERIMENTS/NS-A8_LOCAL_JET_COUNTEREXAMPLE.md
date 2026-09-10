# NS-A8.4 — Localized Divergence-Free Jet Counterexample

**Status:** CLOSED / NOT_PROVEN (candidate coercivity refuted)  
**Date:** 2026-09-10

## Goal

Turn the earlier pointwise matrix obstruction into an actual smooth, compactly supported, divergence-free velocity field. The purpose is to test whether the scalar pressure source

`Q = |S|^2 - |ω|^2/2`

can by itself determine or coercively control vortex stretching

`G_point = ω^T S ω`.

This is a local algebraic obstruction, not a Navier–Stokes blow-up result.

## Step 1 — prescribe the local velocity gradient

Use

`S = diag(1,-1,0)`.

Choose two vorticities

`ω+ = (sqrt(2),0,0)`,

`ω- = (0,sqrt(2),0)`.

Both have `|ω|^2=2` and `|S|^2=2`, hence

`Q+ = Q- = 1`.

But

`G+ = ω+^T S ω+ = +2`,

`G- = ω-^T S ω- = -2`.

Thus the same scalar pressure source is compatible with opposite stretching signs.

## Step 2 — realize the jets by divergence-free affine fields

Let `A± = S + Ω±`, where `Ω` is the antisymmetric matrix corresponding to the selected vorticity under

`Ω_ij = -(1/2) ε_ijk ω_k`.

Set

`u_aff(x) = A x`.

Because `tr(A)=tr(S)=0`,

`div u_aff = 0`.

The curl is exactly the prescribed `ω`.

## Step 3 — localize without destroying divergence-freeness

For any trace-free affine field `u_aff=A x`, define the quadratic vector potential

`Φ(x) = -(1/3) x × u_aff(x)`.

Direct differentiation gives

`curl Φ = u_aff`.

Choose a smooth radial cutoff `χ` with `χ=1` on a neighborhood of the origin and compact support. Define

`u_compact = curl(χ Φ)`.

Then automatically

`div u_compact = 0`,

`u_compact` is smooth and compactly supported, and because `χ=1` near the origin,

`u_compact = u_aff`

on that neighborhood. Therefore the prescribed `S`, `ω`, `Q`, and stretching values occur inside a genuine smooth divergence-free compactly supported field.

## Consequence

The scalar quantity `Q` does not encode the orientation of `ω` relative to the eigenframe of `S`. Therefore no pointwise universal coercivity statement of the form

`ω^T S ω = F(Q, |ω|, |S|)`

can hold without an additional directional/geometric variable.

This does **not** refute every possible pressure-Hessian inequality. A nonlocal tensorial quantity may contain additional information. What is refuted is the weaker idea that the scalar pressure Poisson source alone closes vortex stretching.

## Next attack

The remaining meaningful question is stronger:

> Can the **full nonlocal pressure Hessian**, together with a scale-critical quantity, control the orientation-dependent stretching term?

That requires a genuine periodic/whole-space construction and an integrated inequality. We do not assume the answer.

## Verdict

**H8.1 scalar-source closure: REFUTED.**  
**H8 full pressure-Hessian coercivity: OPEN / NOT_PROVEN.**
