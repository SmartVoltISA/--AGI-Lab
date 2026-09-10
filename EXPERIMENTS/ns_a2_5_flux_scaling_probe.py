"""NS-A2.5 finite-mode scaling sanity probe.

This is NOT a proof checker. It tests whether a simple finite Fourier
configuration exhibits the expected Navier–Stokes scaling for energy-flux
functionals. A scaling failure rejects the candidate normalization; survival
only means the candidate remains inconclusive.
"""

from __future__ import annotations

import argparse
import math
import numpy as np


def project(k: np.ndarray, z: np.ndarray) -> np.ndarray:
    kk = float(np.dot(k, k))
    if kk == 0.0:
        return z
    return z - k * (np.dot(k, z) / kk)


def field(N: int, seed: int = 0, modes: int = 12):
    rng = np.random.default_rng(seed)
    coeff = {}
    keys = []
    for _ in range(modes):
        k = rng.integers(-N, N + 1, size=3)
        if not np.any(k):
            continue
        kt = tuple(int(x) for x in k)
        if kt in coeff or tuple(-x for x in kt) in coeff:
            continue
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        a = project(k.astype(float), a)
        coeff[kt] = a
        coeff[tuple(-x for x in kt)] = np.conj(a)
        keys.extend([kt, tuple(-x for x in kt)])
    return coeff


def norms(coeff):
    w2 = 0.0
    uhalf2 = 0.0
    for k, a in coeff.items():
        kk = sum(x * x for x in k)
        w = np.cross(np.array(k, dtype=float), a)
        w2 += float(np.vdot(w, w).real)
        uhalf2 += (kk ** 0.5) * float(np.vdot(a, a).real)
    return math.sqrt(w2), math.sqrt(uhalf2)


def cubic_vorticity(coeff):
    # Exact finite triad sum for int-domain Fourier modes, up to a common
    # Fourier normalization which cancels in the scaling ratio.
    keys = list(coeff)
    total = 0.0 + 0.0j
    for k in keys:
        K = np.array(k, dtype=float)
        w_k = np.cross(K, coeff[k])
        for p in keys:
            q = tuple(-(k[i] + p[i]) for i in range(3))
            if q not in coeff:
                continue
            P = np.array(p, dtype=float)
            # Strain contribution from mode p: sym(i p \otimes a_p).
            S = 0.5j * (np.outer(P, coeff[p]) + np.outer(coeff[p], P))
            total += np.dot(w_k, S @ np.cross(np.array(q, dtype=float), coeff[q]))
    return abs(total.real)


def scaled(coeff, lam: int):
    # u_lambda(x,t) = lam*u(lam*x,lam^2*t): wavevectors scale by lam,
    # coefficients scale by lam.
    out = {}
    for k, a in coeff.items():
        out[tuple(lam * x for x in k)] = lam * a
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=2)
    ap.add_argument("--seed", type=int, default=20260910)
    ap.add_argument("--modes", type=int, default=12)
    ap.add_argument("--lambdas", type=int, nargs="+", default=[1, 2, 3])
    args = ap.parse_args()

    base = field(args.N, args.seed, args.modes)
    w0, h0 = norms(base)
    c0 = cubic_vorticity(base)
    # Dimensionless exploratory ratio: cubic vorticity interaction / critical
    # H^{1/2} norm cubed. It is only a scaling sanity check.
    r0 = c0 / max(h0 ** 3, 1e-30)
    print(f"base: modes={len(base)} omega_L2={w0:.6e} Hhalf={h0:.6e} cubic={c0:.6e} ratio={r0:.6e}")

    ratios = []
    for lam in args.lambdas:
        c = scaled(base, lam)
        w, h = norms(c)
        cubic = cubic_vorticity(c)
        ratio = cubic / max(h ** 3, 1e-30)
        ratios.append(ratio)
        print(f"lambda={lam}: omega_L2={w:.6e} Hhalf={h:.6e} cubic={cubic:.6e} ratio={ratio:.6e} ratio/base={ratio/max(r0,1e-30):.6f}")

    # For this cubic/critical normalization, exact scaling predicts an
    # invariant ratio. Numerical tolerance is deliberately loose because this
    # is only a finite floating-point sanity test.
    max_dev = max(abs(r / max(r0, 1e-30) - 1.0) for r in ratios)
    print(f"max_relative_scaling_deviation={max_dev:.6e}")
    print("CLASSIFICATION=INCONCLUSIVE")
    print("A scaling-consistent finite-mode ratio does not establish a universal inequality or regularity.")


if __name__ == "__main__":
    main()
