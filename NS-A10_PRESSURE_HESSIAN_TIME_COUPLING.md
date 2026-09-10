# NS-A10 — Pressure Hessian Time-Coupling Attack

Status: **PARTIAL / NOT_PROVEN**

## Goal

After A8/A9, stop asking whether a pointwise pressure quantity determines instantaneous vortex stretching. Test the stronger dynamical possibility: whether the pressure-Hessian term can be universally absorbed by the stretching dynamics after adding time evolution.

For incompressible 3D Navier–Stokes, write

- `A = ∇u = S + Ω`,
- `ω = curl u`,
- `G = ωᵀ S ω`.

The vorticity equation contains `Sω`. Differentiating the stretching vector gives a pressure-Hessian contribution. The exact matrix-gradient equation is

`D A/Dt + A² + H = ν ΔA`,

with `H = ∇²p`. Taking the symmetric part gives the strain evolution.

## Local affine consistency test

Consider an affine incompressible jet

`u(x,t) = A(t)x`, `tr A(t)=0`.

Then `ΔA=0` and the material derivative at the origin is `A'(t)`, so the gradient equation reduces to

`A' + A² + H = 0`.

Taking the trace gives

`tr H = -tr(A²)`.

For `A=S+Ω`,

`tr(A²) = |S|² - |ω|²/2`.

Thus the trace of `H` is fixed by the same scalar invariant already tested in A8. The traceless part of `H` is not determined by this trace relation.

Now fix

`S = diag(1,-1,0)`.

Choose two vorticities

`ω⁺ = (√2,0,0)`,

`ω⁻ = (0,√2,0)`.

Both have

`|S|² = 2`, `|ω|² = 2`, `tr(A²)=1`.

Therefore both require the same pressure-Hessian trace

`tr H = -1`.

Yet

`G⁺ = (ω⁺)ᵀSω⁺ = +2`,

`G⁻ = (ω⁻)ᵀSω⁻ = -2`.

For any chosen symmetric `H` with `tr H=-1`, define

`A' = -H-A²`.

Then `tr A'=0`, so the incompressibility constraint is preserved at the jet level. Therefore the local Navier–Stokes evolution law can accommodate the same prescribed pressure-Hessian trace while the instantaneous stretching signs remain opposite.

## What this does and does not prove

This is an algebraic/local-jet obstruction, not a global finite-energy counterexample. It proves only that the trace constraint and instantaneous gradient algebra do not close `G`.

It does **not** prove that arbitrary identical full Hessians `H(x,t)` can be realized by two global divergence-free finite-energy Navier–Stokes solutions. The pressure Hessian is nonlocal, so that stronger realization remains open.

## Next test

The remaining meaningful route is therefore genuinely space-time and nonlocal:

1. construct periodic divergence-free fields;
2. solve the pressure Poisson equation spectrally;
3. compare the time-integrated quantities

   `∫ ωᵀHω dx dt` and `∫ |Sω|² dx dt`;

4. search for a scale-uniform inequality compatible with Navier–Stokes scaling;
5. actively seek frequency-localized counterexamples before attempting any proof.

Acceptance requires an explicit universal inequality with constants, or an explicit admissible counterexample family. Numerical evidence alone is insufficient.

## External sanity check

The standard gradient equation and the role of the pressure Hessian are independently documented in the fluid-mechanics literature. That is used only as a consistency check; it is not evidence for the proposed closure.

**Conclusion:** A9 does not close. The next target is the genuinely nonlocal space-time coupling, not another pointwise pressure identity.
