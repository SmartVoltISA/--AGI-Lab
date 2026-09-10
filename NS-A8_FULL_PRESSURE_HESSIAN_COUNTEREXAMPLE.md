# NS-A8 — Full Pressure Hessian Counterexample

Status: **CLOSED / NOT_PROVEN**

## Question

Can the full local pressure Hessian `H = ∇²p`, even together with the local incompressible velocity-gradient state, provide a coercive/sign-definite closure for vortex stretching?

The scalar pressure source was already insufficient. Here we test the stronger object: the complete symmetric Hessian.

## Construction

Use an instantaneous smooth affine divergence-free jet

`u(x,t0) = A x`, with `tr A = 0`.

Decompose

`A = S + Ω(ω)`,

where `S` is symmetric trace-free and `Ω` is antisymmetric with vorticity `ω`.

Choose

`S = diag(1,-1,0)`.

Two vorticity orientations:

`ω+ = (√2, 0, 0)`

`ω- = (0, √2, 0)`.

With the convention `A_ij = ∂_j u_i`,

`Ω(ω) = 1/2 [[0, ω3, -ω2],[-ω3,0,ω1],[ω2,-ω1,0]]`.

Therefore

`A+ = [[1,0,0],[0,-1,√2/2],[0,-√2/2,0]]`

and

`A- = [[1,0,-√2/2],[0,-1,0],[√2/2,0,0]]`.

Both satisfy `tr A = 0`.

## Same pressure Hessian

Choose the same symmetric pressure Hessian at the instant

`H = ∇²p = -(1/3) I`.

For both states,

`tr(A²) = 1`.

The incompressible pressure Poisson trace condition is therefore satisfied:

`tr H = -tr(A²) = -1`.

The instantaneous affine Euler equation can be satisfied by choosing the corresponding time derivative

`A_dot = -A² - H`.

It has zero trace in both cases, so incompressibility is preserved at the instant. Thus this is not merely an arbitrary matrix assignment: it is an admissible local affine Euler jet.

## What differs

The pressure Hessian is exactly the same in the two constructions:

`H+ = H- = -(1/3)I`.

The scalar pressure source is also the same:

`Q = |S|² - |ω|²/2 = 2 - 1 = 1`.

But vortex stretching is

`G = ωᵀ S ω`.

Hence

`G+ = +2`,

`G- = -2`.

The stretching has opposite sign while the **entire local pressure Hessian is identical**.

## Interpretation

This kills the stronger local hypothesis:

> "If we know the full pressure Hessian, then pressure geometry alone fixes or coercively controls the instantaneous vortex-stretching sign."

It does not.

The pressure Hessian enters the velocity-gradient/strain dynamics, but the instantaneous stretching `ωᵀSω` is controlled by the orientation of `ω` relative to the eigenstructure of `S`. The same `H` can coexist with opposite stretching in the local jet construction.

This does **not** prove that pressure is irrelevant to the long-time dynamics. It only proves that a pointwise closure of stretching from `H` alone (or from its trace alone) cannot be the missing regularity estimate.

## Important limitation

The affine field is unbounded on `R³` and is therefore not itself a finite-energy global Navier–Stokes solution. The result is a local-jet obstruction. A separate compact-support/divergence-free realization is required before treating it as a global field counterexample.

## A8 conclusion

**REFUTED:** pointwise scalar-pressure-source closure.

**REFUTED:** pointwise full-pressure-Hessian-only closure.

**OPEN:** whether a nonlocal, time-integrated, or scale-coupled pressure/stretching identity can provide a genuinely coercive estimate.

The next experiment must therefore test a relation involving **evolution/integrated history or spatial scale**, not another instantaneous pressure tensor inequality.
