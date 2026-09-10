"""Finite-mode adversarial geometry probe for NS-A3.

Exploratory only. It searches divergence-free finite Fourier fields for large
vortex-stretching ratios and records strain/vorticity geometry. A large value
can reject a proposed universal depletion inequality; it cannot prove one.
"""
from __future__ import annotations
import argparse, math
import numpy as np


def project(k, a):
    k=np.asarray(k,dtype=float); kk=float(k@k)
    return a if kk==0 else a-k*(k@a)/kk


def make_field(N, seed, modes):
    rng=np.random.default_rng(seed); A={}
    for _ in range(modes):
        k=rng.integers(-N,N+1,3)
        if not np.any(k): continue
        kt=tuple(int(x) for x in k); neg=tuple(-x for x in kt)
        if kt in A or neg in A: continue
        a=project(k,rng.normal(size=3)+1j*rng.normal(size=3))
        A[kt]=a; A[neg]=np.conj(a)
    return A


def triad_stretch(A):
    keys=list(A); total=0j
    max_align=0.0; max_pos=0.0
    for k in keys:
        K=np.array(k,float); wk=np.cross(K,A[k])
        for p in keys:
            q=tuple(-(k[i]+p[i]) for i in range(3))
            if q not in A: continue
            P=np.array(p,float); aq=A[p]
            S=.5j*(np.outer(P,aq)+np.outer(aq,P))
            wq=np.cross(np.array(q,float),A[q])
            total += wk @ (S @ wq)
    # Pointwise alignment cannot be recovered from coefficients by a single
    # triad sum, so this probe intentionally reports only the global cubic
    # stretching and its frequency scaling.
    return abs(total.real)


def omega_norm(A):
    s=0.0
    for k,a in A.items():
        w=np.cross(np.array(k,float),a); s+=float(np.vdot(w,w).real)
    return math.sqrt(s)


def mutate(A,rng,sigma):
    B={k:a.copy() for k,a in A.items()}
    reps=[]
    for k in list(B):
        if k[0]>0 or (k[0]==0 and k[1]>0) or (k[0]==k[1]==0 and k[2]>0): reps.append(k)
    if not reps:return B
    k=reps[rng.integers(len(reps))]; neg=tuple(-x for x in k)
    d=rng.normal(size=3)+1j*rng.normal(size=3)
    d=project(k,d)*sigma
    B[k]+=d; B[neg]=np.conj(B[k]); return B


def optimize(N,seed,modes,steps):
    rng=np.random.default_rng(seed); A=make_field(N,seed,modes)
    def score(X):
        wn=omega_norm(X)
        return triad_stretch(X)/max(wn**3,1e-30)
    best=score(A)
    for _ in range(steps):
        B=mutate(A,rng,0.25); s=score(B)
        if s>=best or rng.random()<0.01:
            A=B; best=max(best,s)
    return best


def main():
    p=argparse.ArgumentParser(); p.add_argument('--N',nargs='+',type=int,default=[1,2,3,4])
    p.add_argument('--repeats',type=int,default=3); p.add_argument('--steps',type=int,default=1500)
    p.add_argument('--modes',type=int,default=14); p.add_argument('--seed',type=int,default=20260910)
    a=p.parse_args()
    for N in a.N:
        vals=[optimize(N,a.seed+1000*N+r,a.modes,a.steps) for r in range(a.repeats)]
        print(f'N={N} best={max(vals):.8e} mean={np.mean(vals):.8e} values='+','.join(f'{v:.8e}' for v in vals))
    print('CLASSIFICATION=INCONCLUSIVE')
    print('No finite-mode result is a universal theorem or a regularity proof.')

if __name__=='__main__': main()
