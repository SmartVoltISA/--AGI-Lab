# NS-A9 — Second-Derivative Stretching / Pressure Test

Status: PARTIAL / NOT_PROVEN

## 1. Why A9 exists

A8 showed that the scalar pressure source

`Q = |S|^2 - |omega|^2/2`

cannot determine the sign of the instantaneous vortex stretching

`G = omega^T S omega`.

The next question is narrower and more useful:

> Can the pressure Hessian `H = nabla^2 p` be controlled pointwise by the nonlinear term that appears in the second material derivative of vorticity/enstrophy?

This is an attack on a specific closure, not a claim about Navier–Stokes regularity.

## 2. Exact local identity (Euler part)

For incompressible Euler, write

`A = grad u = S + Omega`,

with `S^T=S`, `tr(S)=0`, and `Omega^T=-Omega`.

The vorticity equation is

`D omega / Dt = S omega`.

The strain equation is

`D S / Dt = -S^2 - Omega^2 - H`.

Because `Omega omega = 0`, differentiating

`G = omega^T S omega`

gives the exact identity

`D G / Dt = |S omega|^2 - omega^T H omega`.

Also

`D |omega|^2 / Dt = 2G`.

Therefore

`D^2 |omega|^2 / Dt^2 = 2|S omega|^2 - 2 omega^T H omega`.

For Navier–Stokes, viscosity adds the corresponding material derivatives/diffusion terms; A9 does not discard them. The Euler identity is used only to isolate the pressure-vs-stretching mechanism.

## 3. Candidate closure attacked

A natural coercive closure would have the schematic form

`omega^T H omega <= c |S omega|^2 + lower_order`

with a universal `c < 1`, or a stronger scale-uniform version sufficient to prevent runaway positive second derivative of enstrophy.

A weaker diagnostic is the dimensionless local ratio

`R = (omega^T H omega) / |S omega|^2`

where the denominator is bounded away from zero.

The test does NOT claim that a large observed `R` disproves every possible inequality. It only checks whether a small universal pointwise coefficient is even plausible.

## 4. Independent periodic spectral experiment

Domain: 3-torus.

Construction:

1. Generate a real divergence-free Fourier velocity field from random complex amplitudes.
2. Use several low-frequency modes.
3. Compute `A`, `S`, and `omega` spectrally.
4. Form
   `Q = |S|^2 - |omega|^2/2`.
5. Recover pressure Hessian from the periodic Poisson relation
   `-Delta p = Q`,
   so for nonzero Fourier mode `k`,
   `H_ij_hat(k) = -(k_i k_j / |k|^2) Q_hat(k)`.
6. Evaluate `omega^T H omega` and `|S omega|^2` at every grid point.
7. Exclude the lowest 10% of denominator values and record the maximum ratio.

Important normalization correction: the pressure inverse transform is applied directly to the FFT of the physical `Q`; no extra `N^3` factor is used on the inverse pressure transform.

## 5. Results

Grid: `24^3`.

Random seeds: 0–199.

For 15 randomly selected divergence-free modes with `|k| <= 3`, the largest observed value of `R` after restricting to the top 10% of `|S omega|^2` was approximately

`R_max = 14.87`

(seed 7).

The most negative value in that same sample was approximately

`R_min = -2.25`.

A frequency-window sweep using 10 random fields per window gave approximate positive maxima:

| k_max | max R |
|---:|---:|
| 1 | 2.92 |
| 2 | 10.26 |
| 3 | 9.86 |
| 4 | 14.44 |

These are exploratory numerical observations, not a theorem. They show that the pressure-Hessian contribution can be substantially larger than `|S omega|^2` pointwise in this test family, with both signs occurring.

## 6. What this actually establishes

Established by exact algebra:

- `D G/Dt = |S omega|^2 - omega^T H omega` for the Euler part.
- The pressure Hessian enters the second derivative of enstrophy through the contraction `omega^T H omega`.

Observed computationally:

- No small universal pointwise coefficient `c < 1` is supported by the tested Fourier family.
- The pressure term is not merely a small perturbation of `|S omega|^2` in these examples.
- The sign can oppose or reinforce the stretching contribution.

Not established:

- No unboundedness theorem for `R`.
- No refutation of all pressure-based regularity criteria.
- No Navier–Stokes singularity result.
- No claim that the tested random fields are dynamically realized near a singularity.

## 7. Next falsification target

The useful next target is no longer an instantaneous pointwise inequality.

Test instead whether a **space-time integrated** pressure-stretching balance can produce a coercive quantity with constants uniform in frequency.

Candidate form:

`Integral omega^T H omega <= theta Integral |S omega|^2 + controlled boundary/viscous terms`

with `theta < 1` and explicit scale dependence.

If a frequency-localized family breaks every such candidate, A9 closes the pressure-Hessian route at the local-to-global transition.

If it survives, that surviving quantity becomes the next mathematical object to attack.

## Verdict

`PARTIAL / NOT_PROVEN`

The pressure-Hessian route is **not closed**. The local pointwise closure is strongly obstructed numerically, but the decisive question is now space-time/frequency integrated control.
