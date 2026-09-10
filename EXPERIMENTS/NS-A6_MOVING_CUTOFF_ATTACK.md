# NS-A6.1 — Moving Cutoff Analytical Attack

**Status:** PARTIAL / NOT_PROVEN  
**Parent:** NS-A6_FREQUENCY_LOCALIZED_BKM.md  
**Date:** 2026-09-10

## Target

Test H6.3: whether a time-dependent dyadic cutoff can convert the low-frequency continuation mechanism into a boundary-flux identity compatible with NS-A2.

## Exact smooth-cutoff result

Let

`P_Λ(t)u = F^{-1}[χ(|ξ|/Λ(t)) û(ξ,t)]`,

with `χ` real, smooth and compactly supported, and define

`E_Λ(t)=1/2||P_Λu||_2²`.

For a smooth divergence-free Navier–Stokes solution,

`dE_Λ/dt = -<(u·∇)u,P_Λ²u> - ν||∇P_Λu||_2² + <(∂_tP_Λ)u,P_Λu>`.

The last term is unavoidable. With `r=|ξ|/Λ(t)`,

`∂_tχ(r)=-(Λ'(t)/Λ(t))rχ'(r)`,

so

`C_Λ(t)=< (∂_tP_Λ)u,P_Λu >`

is an explicit quadratic transition-band term with no fixed sign.

This exact identity is recorded in `NS-A6_1_SMOOTH_CUTOFF_IDENTITY.md`.

## Important scaling result

For

`Λ(t)=C[ν(T-t)]^{-1/2}`,

one gets

`|Λ'/Λ|/[νΛ²]=1/(2C²)`.

Therefore the moving-cutoff term is of the same dimensional order as parabolic dissipation, but its characteristic coefficient can be made small by taking a sufficiently large dimensionless cutoff constant `C`.

This is **not** yet an absorption proof: the dissipation carries `|ξ|²χ²`, while the cutoff derivative carries `rχ'χ`. Near the cutoff edge, a pointwise ratio may fail. A genuine transition-band estimate or paired-cutoff argument is still required.

## Nonlinear term

The nonlinear contribution is

`N_Λ=<(u·∇)u,P_Λ²u>`.

It cannot be identified with one-way high-frequency creation. Crossing triads include high-high → low and low-high → high interactions. Any estimate must retain their signs and multiplicities.

## Literature cross-check

Frequency-localized BKM criteria already exist. Luo's 2019 result gives a BKM-type criterion requiring control only below an explicit critical frequency, and Bradshaw–Grujić established frequency-localized regularity criteria with relevant high-frequency windows. citeturn0search2turn0search9

Therefore A6 is not allowed to claim novelty merely from introducing a moving cutoff. The research target is narrower: determine whether the exact moving-cutoff/flux formulation yields an independently checkable reduction or obstruction when coupled to the existing NS-A2 dyadic transfer machinery.

## Current result

The first formal obstruction has been resolved into an exact identity. The cutoff-variation term is real, scaling-compatible, and potentially controllable at the dimensional level, but no uniform critical estimate has been established.

**Classification: PARTIAL / NOT_PROVEN.**

## Next attack

Derive the exact triadic/commutator representation of `N_Λ` and test it against the critical frequency-localized continuation mechanism. Specifically attack:

- high-high → low boundary crossing;
- low-high → high transfer;
- many-shell accumulation;
- transition-band cutoff-edge behavior;
- uniform scaling-compatible constants;
- circular use of the desired continuation/BKM bound.
