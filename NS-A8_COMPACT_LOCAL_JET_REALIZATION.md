# NS-A8 — Compactly Supported Realization of the Local Jet Counterexample

Status: **REFUTED (candidate scalar-pressure closure)**

## 1. Question

Can the scalar pressure-Poisson source

`Q = |S|^2 - (1/2)|ω|^2`

control, determine, or sign-control the vortex-stretching scalar

`G = ω^T S ω`?

We first found a pointwise algebraic counterexample using a trace-free strain matrix. The next question is whether that counterexample is merely an unphysical affine jet. It is not: the same first-order jet can be embedded exactly into a smooth compactly supported divergence-free velocity field.

## 2. Local target jet

Take

`S = diag(1,-1,0)`.

This is symmetric and trace-free.

Choose two vorticity vectors

`ω+ = (sqrt(2), 0, 0)`,

`ω- = (0, sqrt(2), 0)`.

Then

`|S|^2 = 2`,

`|ω+|^2 = |ω-|^2 = 2`.

Therefore both states have exactly the same scalar pressure source:

`Q+ = Q- = 2 - 1 = 1`.

But

`G+ = ω+^T S ω+ = +2`,

`G- = ω-^T S ω- = -2`.

Thus the same Q is compatible with opposite vortex stretching.

## 3. Turn the jet into an actual divergence-free field

For any trace-free matrix `A`, define the affine field

`u_aff(x) = A x`.

Since `tr(A)=0`,

`div u_aff = 0`.

The symmetric part of `A` is `S`, and its antisymmetric part can be chosen so that the curl is the desired `ω`.

The affine field itself is not finite-energy because it does not decay. We therefore localize it without changing the jet near the origin.

Let `χ(x)` be any smooth compactly supported cutoff satisfying

`χ(x)=1` in a neighborhood of `x=0`.

For the divergence-free affine field `u_aff`, introduce the vector potential

`B(x) = -(1/3) x × u_aff(x)`.

Using `div(u_aff)=0` and the fact that `u_aff` is homogeneous of degree one,

`curl B = u_aff`.

Now define

`u_loc = curl(χ B)`.

Automatically,

`div u_loc = 0`

and `u_loc` is smooth and compactly supported.

Inside the region where `χ=1`, `∇χ=0`, so

`u_loc = curl B = u_aff`.

Therefore at the origin, and indeed throughout that neighborhood, the localized field has exactly the prescribed velocity gradient, strain, and vorticity.

## 4. Consequence

This removes the main objection to the previous test.

The counterexample is not merely an abstract matrix configuration. It is realizable as the exact local jet of a smooth compactly supported divergence-free velocity field.

Hence the scalar quantity `Q` does not contain enough local information to determine the stretching scalar `G`.

The missing information is geometric: specifically, the orientation of `ω` relative to the eigenstructure of `S`.

## 5. What this does NOT prove

This does **not** prove that Navier–Stokes develops a singularity.

It does **not** prove that pressure is irrelevant.

It only refutes the narrower closure hypothesis:

> scalar pressure-Poisson information alone is sufficient to close vortex stretching.

A stronger pressure route would have to retain additional tensorial/nonlocal information, not merely the scalar `Q`.

## 6. Next attack

The natural next test is therefore:

1. retain the full pressure Hessian `H = ∇²p`, not only `tr(H)`;
2. test whether `H`, `S`, and `ω` admit a coercive relation capable of controlling `G`;
3. construct paired divergence-free fields with matched scalar pressure source and matched low-order pressure data but different stretching;
4. if that also fails, close the pressure route rather than recycling known criteria.

This is an Ω-style result: **candidate → explicit counterexample → closure rejected → next discriminating test**.

## 7. External sanity check

The standard velocity-gradient formulation indeed treats the pressure Hessian as a tensor coupled to the velocity-gradient dynamics, while the scalar pressure Poisson relation only supplies its trace. That is consistent with the distinction tested here, but the counterexample above was constructed independently rather than copied from that literature.
