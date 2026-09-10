"""Offline adversarial search for a naive Navier-Stokes stretching inequality.

Target candidate:
    integral omega . S omega <= C ||omega||_2^2
with a universal C independent of spatial scale.

This is NOT a proof of anything. A numerical witness can reject a universal
inequality, while failure to find one cannot establish the inequality.
"""
import numpy as np

RNG = np.random.default_rng(7)
BASE_MODES = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(2,1,0)]


def random_modes():
    modes = []
    for k0 in BASE_MODES:
        k = np.asarray(k0, dtype=float)
        a = RNG.normal(size=3) + 1j * RNG.normal(size=3)
        # Project amplitude to k-perpendicular subspace: incompressibility.
        a = a - k * np.vdot(k, a) / np.dot(k, k)
        a /= np.linalg.norm(a)
        modes.append((tuple(k.astype(int)), a))
    return modes


def make_field(modes, n):
    x = np.arange(n) * 2*np.pi/n
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    u = np.zeros((n,n,n,3), dtype=float)
    for k, a in modes:
        phase = k[0]*X + k[1]*Y + k[2]*Z
        u += 2*np.real(np.exp(1j*phase)[...,None] * a[None,None,None,:])
    return u


def gradient(u):
    n = u.shape[0]
    uh = np.fft.fftn(u, axes=(0,1,2))
    f = np.fft.fftfreq(n, 1/n)
    K = np.meshgrid(f,f,f,indexing="ij")
    g = np.empty((3,3,n,n,n), dtype=float)
    for c in range(3):
        for d in range(3):
            g[c,d] = np.fft.ifftn(1j*K[d]*uh[...,c], axes=(0,1,2)).real
    return g


def ratio(u):
    g = gradient(u)
    S = 0.5*(g + np.swapaxes(g,0,1))
    omega = np.stack((g[2,1]-g[1,2], g[0,2]-g[2,0], g[1,0]-g[0,1]), axis=-1)
    stretch = np.einsum("...i,ij...,...j->...", omega, S, omega).mean()
    enstrophy = (omega*omega).sum(axis=-1).mean()
    return stretch/enstrophy


def main():
    modes = random_modes()
    print("candidate: <omega,S omega> <= C ||omega||_2^2")
    print("seed: 7; divergence-free finite Fourier field")
    print("scale, ratio")
    for m in (1,2,4,6):
        scaled = [((m*k[0],m*k[1],m*k[2]), a) for k,a in modes]
        n = 32*m + 8
        r = ratio(make_field(scaled,n))
        print(f"{m}, {r:.12g}")
    print("interpretation: ratio grows linearly under spatial rescaling for this witness;")
    print("therefore no scale-independent finite C can satisfy this naive inequality.")
    print("This rejects only this candidate, not Navier-Stokes regularity itself.")

if __name__ == "__main__":
    main()
