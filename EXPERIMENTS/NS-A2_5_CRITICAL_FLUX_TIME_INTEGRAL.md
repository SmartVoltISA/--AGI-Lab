# NS-A2.5 — Critical Time-Integrated Flux Attack

**Status:** OPEN / NOT_PROVEN  
**Parent:** NS-A2  
**Date:** 2026-09-10

## 1. Goal

Attack the unresolved Navier–Stokes bottleneck through a genuinely scale-critical, time-integrated estimate rather than a pointwise cubic enstrophy bound.

The target is not to assume regularity, but to identify whether the nonlinear transport can be controlled over time by a critical quantity whose scaling matches the 3D incompressible Navier–Stokes scaling.

## 2. Starting point

For smooth divergence-free solutions,

`∂_t u + (u·∇)u = -∇p + νΔu`,  `∇·u = 0`.

The dyadic energy balance gives

`dE_j/dt = Π_j - ν||∇u_j||_2²`,

with conservative transfer

`Σ_j Π_j = 0`.

Thus the nonlinear term redistributes kinetic energy between scales. The unresolved issue is whether this transfer can drive an uncontrolled high-frequency cascade strongly enough to destroy regularity.

## 3. Critical scaling

Under

`u_λ(x,t) = λ u(λx, λ²t)`,

critical velocity norms include `Ḣ^(1/2)` and related critical Besov spaces.

A viable estimate must remain uniform under this scaling. Any hidden factor equivalent to a supercritical norm is a failure of the proposed closure.

## 4. Candidate target

For a low-pass cutoff `S_J`, define cumulative nonlinear flux

`Φ_J(t) = <(u·∇)u, S_J u>`.

The exact low-pass balance is

`d/dt E_{≤J} = -Φ_J - ν||∇S_Ju||_2²`.

Candidate critical estimate:

`∫_0^T |Φ_J(t)| dt ≤ C * K_T(u)`,

where `K_T` is scale-critical and sufficient to control the high-frequency tail uniformly in `J`.

A stronger candidate is a shellwise estimate of the form

`Σ_J 2^{-θJ} ∫_0^T |Π_J(t)| dt ≤ C K_T(u)`

for a scaling-compatible `θ`, with constants independent of the ultraviolet cutoff.

These are hypotheses, not established inequalities.

## 5. Required closure

A successful route must establish all of the following:

1. exact Navier–Stokes scaling;
2. no hidden supercritical norm;
3. uniformity in the shell/cutoff index;
4. a bound strong enough to prevent unbounded high-frequency concentration;
5. compatibility with the viscous dissipation term;
6. a continuation criterion connecting the bound to smoothness;
7. no circular use of the desired regularity;
8. validity for arbitrary smooth divergence-free initial data in the stated domain.

Failure of any one item means the route is not a proof.

## 6. Adversarial attacks

### A. Narrow-band concentration
Put essentially all critical norm into a narrow high-frequency shell and test whether the proposed bound deteriorates with frequency.

### B. Low–high interaction
Keep low-frequency velocity large while concentrating vorticity at high frequency. Check whether the estimate acquires an uncontrolled frequency factor.

### C. High–high → low transfer
Test whether two high-frequency modes can create a low-frequency contribution that defeats a shellwise absolute-value estimate.

### D. Nonlocal triads
Use separated frequencies `|k| << |p| ≈ |q|` and test uniformity.

### E. Time concentration
Concentrate flux into short intervals while preserving the same critical spacetime norm. A valid estimate must survive temporal concentration.

### F. Rescaling
Apply several Navier–Stokes rescalings to the same configuration. The dimensionless ratio of both sides must remain invariant.

### G. Endpoint accumulation
Test `q=∞`-type Besov accumulation, where each shell can be individually bounded but the sum may diverge.

## 7. Important distinction

The previously tested finite-dimensional inequality

`|∫ω·Sω| ≤ C||ω||_2³`

is not sufficient. Even if such a cubic estimate were universally true, its induced enstrophy growth is superlinear and does not provide the missing global regularity closure.

Therefore NS-A2.5 explicitly targets **time-integrated critical control**, not another pointwise cubic inequality.

## 8. Current result

No critical time-integrated flux inequality has been proved here.

**Classification: NOT_PROVEN.**

## 9. Next executable test

Build a finite-mode Fourier generator with controlled critical norm and numerically search for frequency-growing violations of candidate scale-invariant spacetime-flux ratios. Numerical survival cannot prove the inequality, but an explicit scaling violation can reject a candidate immediately.

Then derive the corresponding paraproduct estimate symbolically and compare every frequency factor against the critical scaling.

## 10. Safety / provenance

Offline mathematical research only. No external systems, no canonical SPACE writes, no automatic promotion. All numerical results are exploratory evidence and require independent mathematical verification.
