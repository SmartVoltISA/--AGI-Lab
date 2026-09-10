# NS-A6.1 — Exact Smooth Moving-Cutoff Identity

**Status:** PARTIAL / NOT_PROVEN  
**Parent:** NS-A6_FREQUENCY_LOCALIZED_BKM.md  
**Date:** 2026-09-10

## 1. Purpose

Derive the exact energy identity for a time-dependent smooth Fourier cutoff. The goal is to replace the previous formal statement in `NS-A6_MOVING_CUTOFF_ATTACK.md` with an identity that exposes every additional term before any estimate is attempted.

Work on `R^3` or the periodic torus, with a smooth divergence-free solution on the time interval under consideration. Let

`P_Λ(t)u = F^{-1}[ χ(|ξ|/Λ(t)) û(ξ,t) ]`,

where `χ` is real, smooth, radial, and compactly supported.

Define

`E_Λ(t) = 1/2 ||P_Λ(t)u(t)||_2^2`.

## 2. Exact differentiation

Since `P_Λ` is self-adjoint,

`dE_Λ/dt = <P_Λ u_t, P_Λ u> + <(∂_t P_Λ)u, P_Λu>`.

For incompressible Navier–Stokes,

`u_t + (u·∇)u = -∇p + νΔu`.

The pressure contribution vanishes after pairing with the divergence-free field `P_Λ^2u`. Since `P_Λ` commutes with `Δ`,

`dE_Λ/dt = -<(u·∇)u, P_Λ^2u> - ν||∇P_Λu||_2^2 + <(∂_tP_Λ)u,P_Λu>`.

This is the exact smooth-cutoff identity.

## 3. Nonlinear term as a commutator

Because `∇·u=0`,

`<u·∇(P_Λu), P_Λu> = 0`.

Therefore

`<(u·∇)u,P_Λu> = <[P_Λ,u·∇]u,P_Λu>`.

For the smooth energy above the exact nonlinear term is instead

`< (u·∇)u,P_Λ^2u >`

and hence the corresponding commutator representation is

`<(u·∇)u,P_Λ^2u> = <[P_Λ^2,u·∇]u,u>`

or, equivalently after pairing with `P_Λu`, it must be handled with the actual multiplier `P_Λ^2`. No projection identity may be imported without checking the multiplier.

Thus the exact balance is

`dE_Λ/dt = -N_Λ - νD_Λ + C_Λ`,

where

`N_Λ = <(u·∇)u,P_Λ^2u>`,

`D_Λ = ||∇P_Λu||_2^2`,

`C_Λ = <(∂_tP_Λ)u,P_Λu>`.

## 4. Exact cutoff-variation term

Set `r=|ξ|/Λ(t)`. Then

`∂_t[χ(r)] = -(Λ'(t)/Λ(t)) r χ'(r)`.

Consequently

`C_Λ(t) = - (Λ'(t)/Λ(t)) ∫ r χ'(r)χ(r) |û(ξ,t)|^2 dξ`,

up to the standard Fourier-normalization factor.

This term is quadratic, supported in the transition region of the cutoff, and has no fixed sign.

## 5. Parabolic scaling test

For a parabolically scaled cutoff law

`Λ(t)=C [ν(T-t)]^{-1/2}`

we obtain

`Λ'(t)/Λ(t) = 1/[2(T-t)]`,

while

`νΛ(t)^2 = C^2/(T-t)`.

Therefore

`|Λ'(t)/Λ(t)| / [νΛ(t)^2] = 1/(2C^2)`.

This is an important result: the moving-cutoff derivative is not automatically supercritical relative to viscosity. With a sufficiently large dimensionless cutoff constant `C`, its characteristic size can be made small compared with the parabolic dissipation scale.

However, this observation is NOT an absorption proof. The dissipation contains the multiplier `|ξ|^2 χ(r)^2`, whereas `C_Λ` contains `rχ'(r)χ(r)`. Near the outer edge where `χ` becomes small, a pointwise ratio argument can fail. A valid estimate must therefore control the transition band as a whole or use a specially designed cutoff/paired cutoffs.

## 6. Scaling covariance

Under the Navier–Stokes scaling

`u_λ(x,t)=λu(λx,λ²t)`,

frequency and time transform as

`Λ_λ(t)=λΛ(λ²t)`.

The parabolic law above satisfies this covariance provided the viscosity is treated with its physical scaling normalization consistently.

## 7. What has been proved here

1. The smooth moving-cutoff identity is exact on a smooth solution.
2. A genuinely new term `C_Λ` appears and cannot be dropped.
3. For a parabolic cutoff, `C_Λ` is of the same dimensional order as viscosity, with relative scale `1/(2C²)` before multiplier-shape effects.
4. Therefore the cutoff-variation term is potentially controllable by choosing the cutoff scale sufficiently separated from the parabolic scale, but this requires a real inequality.

## 8. What remains open

The unresolved term is the nonlinear boundary flux `N_Λ` together with the transition-band estimate for `C_Λ`.

A successful A6 proof still needs a uniform, scaling-compatible bound that converts the exact identity into a continuation criterion without assuming the desired regularity in disguise.

In particular, the following must be attacked explicitly:

- high-high → low triads crossing the boundary;
- low-high → high interactions;
- accumulation over many shells;
- cutoff-edge behavior where `χ→0`;
- constants independent of the chosen cutoff scale;
- pressure/nonlocal effects if the formulation is not fully Leray-projected;
- absence of circular use of a BKM-type bound.

**Classification: PARTIAL / NOT_PROVEN.**

## 9. Next attack

Construct the exact triadic/commutator representation of `N_Λ` and test whether it admits a critical estimate compatible with the frequency-localized continuation criteria already known in the literature. In particular, compare the resulting requirement with Luo's frequency-localized BKM criterion rather than treating the moving cutoff as a new theorem.

## References

- X. Luo, *A Beale–Kato–Majda Criterion with Optimal Frequency and Temporal Localization*, J. Math. Fluid Mech. 21 (2019). The published result gives a BKM-type criterion controlling Fourier modes below an explicit critical frequency. See the literature record associated with the project.
- Z. Bradshaw, Z. Grujić, *Frequency Localized Regularity Criteria for the 3D Navier–Stokes Equations*, Arch. Rational Mech. Anal. 224 (2017). The work identifies frequency windows relevant to possible singularity formation.
