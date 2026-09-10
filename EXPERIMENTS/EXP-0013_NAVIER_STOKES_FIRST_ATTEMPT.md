# EXP-0013 — Navier–Stokes First Independent Attempt

**Status:** NOT_PROVEN  
**Attempt:** NS-A1  
**Date:** 2026-09-10  
**Scope:** 3D incompressible Navier–Stokes, smooth data, unforced case for the first reduction.

## 1. Goal

Try to obtain a new a-priori estimate strong enough to exclude finite-time blow-up. The attempt starts from the standard energy and vorticity balances and asks whether a scale-sensitive quantity can close the estimate.

## 2. Equations

For viscosity `ν > 0`:

`∂_t u + (u·∇)u = -∇p + νΔu`,  `∇·u = 0`.

Vorticity `ω = ∇×u` satisfies

`∂_t ω + (u·∇)ω = (ω·∇)u + νΔω`.

The enstrophy identity has the schematic form

`(1/2)d||ω||_2^2/dt = ∫ ω·(∇u)ω dx - ν||∇ω||_2^2`.

The first term is vortex stretching.

## 3. Candidate route A — close enstrophy by energy

A tempting chain is:

`energy bound → gradient bound → enstrophy bound → regularity`.

### Falsification

This chain does not close. The energy estimate controls `||u||_2`, while the regularity obstruction is carried by higher derivatives/vorticity. The stretching term is not controlled with the required sign by the energy inequality alone.

**Result:** REJECTED.

## 4. Candidate route B — exploit vortex-stretching geometry

The nonlinear term can be decomposed using the strain tensor `S = (∇u + ∇u^T)/2`:

`ω·(∇u)ω = ω·Sω`.

If one could prove a universal estimate of the form

`∫ ω·Sω dx ≤ C ||ω||_2^2` 

with a constant strong enough to be absorbed by viscosity for all smooth solutions, then a global bound would follow.

### Falsification

No such estimate has been established here. Standard inequalities introduce stronger norms, and the resulting differential inequality is compatible with superlinear growth. The desired estimate is therefore the unresolved step, not a consequence of the preceding identities.

**Result:** PARTIAL / NOT_PROVEN.

## 5. Candidate route C — search for a critical quantity

The failed routes suggest that the missing control must respect the scaling of Navier–Stokes rather than merely bound an arbitrary higher norm. The next candidate is therefore a scale-critical or near-critical functional `F[u]` satisfying:

1. `F[u]` is finite for smooth initial data;
2. `F[u]` controls the continuation criterion;
3. its evolution contains viscosity with a coercive term;
4. the nonlinear contribution can be bounded by a function of `F` alone without supercritical loss.

No explicit `F` satisfying all four conditions has been derived in this attempt.

**Result:** NOT_PROVEN.

## 6. Independent self-attack

Potential hidden assumptions checked:

- Energy control was not treated as higher-norm control.
- Vortex stretching was not assigned a false sign.
- A regularity criterion was not used as if it were its own proof.
- Model agreement would not count as verification.
- No numerical experiment is treated as a proof of a universal statement.

## 7. Current mathematical obstruction

The attempt reaches a precise obstruction rather than a solution:

> To turn the conditional enstrophy/regularity route into a proof, derive a global estimate preventing the nonlinear vortex-stretching term from producing the concentration required for blow-up, while retaining the correct Navier–Stokes scaling.

That estimate is the central unresolved target for the next branch.

## 8. Status

**NOT_PROVEN.** No Millennium Problem solution is claimed.

The branch is preserved because the failure identifies the exact point at which naive energy closure breaks. It is a seed for GROWER to generate competing estimates rather than an accepted theorem.

## 9. Next branches

- NS-A2: Littlewood–Paley / dyadic decomposition of vortex stretching.
- NS-A3: strain-eigenvalue geometry and alignment estimates.
- NS-A4: search for a scale-critical Lyapunov functional.
- NS-A5: adversarial search for explicit counterexamples to each proposed inequality.
- NS-A6: formal verification of every surviving elementary lemma.
