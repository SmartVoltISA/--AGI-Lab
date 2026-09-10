# NS-A8.1 — Pressure-Hessian Structural Identity

**Status:** PARTIAL / NOT_PROVEN  
**Date:** 2026-09-10

## Exact starting point

Let `A=∇u=S+Ω`, with `S^T=S`, `Ω^T=-Ω`, and `div u=tr S=0`.

The pressure equation is

`-Δp = ∂_i u_j ∂_j u_i = tr(A^2) = |S|^2 + tr(Ω^2)`.

Since `tr(Ω^2)=-|Ω|_F^2`, this is

`-Δp = |S|^2-|Ω|_F^2`.

For vorticity `ω`, `Ω` is the antisymmetric matrix associated with `ω` and `|Ω|_F^2=|ω|^2/2` under the convention `Ω_{ij}=(∂_j u_i-∂_i u_j)/2`.

Therefore

`-Δp = |S|^2-|ω|^2/2`.

## What this gives

The scalar pressure source measures a difference between strain intensity and rotational intensity. It does **not** determine the orientation of `S` relative to `ω`, which is what enters stretching:

`ω·Sω = |ω|^2 ξ·Sξ`, `ξ=ω/|ω|` where `ω≠0`.

Consequently the pressure Poisson equation alone cannot close the enstrophy production.

## Hessian relation

Taking two derivatives gives

`∂_i∂_j p = -∂_i∂_j Δ^{-1} (|S|^2-|ω|^2/2)`.

The pressure Hessian is therefore a nonlocal Calderón–Zygmund transform of the quadratic gradient invariant. It is not pointwise sign-definite.

## Geometric consequence

Any proposed coercive inequality of the form

`∫ω·Sω ≤ C * pressure-Hessian-positive-term + lower-order terms`

must supply an additional mechanism connecting the **orientation** of `ω` to the eigenstructure of the nonlocal pressure Hessian. The Poisson identity alone does not provide that mechanism.

## Adversarial implication

A finite Fourier field can alter the orientation/eigenframe of `S` while preserving scalar quantities such as `|S|^2-|ω|^2/2`. Therefore scalar pressure control cannot by itself control stretching.

## Verdict

H8.1 is **not closed** by the pressure Poisson identity. The exact identity is useful, but it leaves the essential orientation/nonlocality problem untouched.

**Classification: PARTIAL / NOT_PROVEN.**
