#!/usr/bin/env python3
"""Offline adversarial search for a cubic vorticity/strain inequality.

No network, no canonical writes. Numerical evidence can REJECT a universal
inequality but cannot prove one.
"""
import argparse, itertools, math
import numpy as np

def project(k, z):
    k = np.asarray(k, float)
    return z - k * (np.dot(k, z) / np.dot(k, k))

def evaluate(A):
    W = {k: 1j*np.cross(np.asarray(k,float), a) for k,a in A.items()}
    S = {(k,i,j): 0.5j*(k[j]*a[i] + k[i]*a[j])
         for k,a in A.items() for i in range(3) for j in range(3)}
    keys=list(W)
    cubic=0j
    for k in keys:
        for p in keys:
            q=tuple(-np.asarray(k)-np.asarray(p))
            if q not in W: continue
            Sm=np.array([[S[(p,i,j)] for j in range(3)] for i in range(3)])
            cubic += W[k] @ (Sm @ W[q])
    norm2=sum(np.vdot(w,w).real for w in W.values())
    return abs(cubic.real)/(norm2**1.5 + 1e-30)

def random_field(N, rng, modes):
    allk=[k for k in itertools.product(range(-N,N+1), repeat=3) if k!=(0,0,0)]
    base=rng.choice(len(allk), size=min(modes,len(allk)), replace=False)
    A={}
    for idx in base:
        k=tuple(allk[idx]); z=rng.normal(size=3)+1j*rng.normal(size=3)
        A[k]=project(k,z)
        A[tuple(-np.asarray(k))]=np.conj(A[k])
    return A

def optimize(N, steps, seed, modes, sigma):
    rng=np.random.default_rng(seed)
    A=random_field(N,rng,modes)
    score=evaluate(A); best=score
    keys=list(A)
    for _ in range(steps):
        k=keys[rng.integers(len(keys))]
        old=A[k].copy()
        z=old + sigma*(rng.normal(size=3)+1j*rng.normal(size=3))
        A[k]=project(k,z)
        if tuple(-np.asarray(k)) in A:
            A[tuple(-np.asarray(k))]=np.conj(A[k])
        new=evaluate(A)
        # maximize; simulated annealing is intentionally omitted: this is an
        # adversarial hill-climb whose reproducibility is easy to audit.
        if new >= score:
            score=new
            best=max(best,new)
        else:
            A[k]=old
            A[tuple(-np.asarray(k))]=np.conj(old)
    return best

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--N', type=int, nargs='+', default=[1,2,3,4])
    ap.add_argument('--steps', type=int, default=3000)
    ap.add_argument('--modes', type=int, default=12)
    ap.add_argument('--repeats', type=int, default=4)
    ap.add_argument('--seed', type=int, default=20260910)
    args=ap.parse_args()
    print('NS-A2.4 Fourier optimizer | offline | numerical rejection tool')
    for N in args.N:
        vals=[optimize(N,args.steps,args.seed+r,args.modes,0.15) for r in range(args.repeats)]
        print(f'N={N}: max={max(vals):.10g} mean={np.mean(vals):.10g} values='+','.join(f'{x:.6g}' for x in vals))
    print('CLASSIFICATION=INCONCLUSIVE unless an explicit candidate inequality is falsified.')

if __name__ == '__main__': main()
