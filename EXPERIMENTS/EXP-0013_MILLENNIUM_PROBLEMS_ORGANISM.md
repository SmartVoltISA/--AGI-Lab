# EXP-0013 — Millennium Problems: Organism Research Trial

**Status:** PROPOSED / NOT YET EXECUTED
**Date:** 2026-09-10

## Question

Can the integrated research organism independently generate, test, falsify, formalize and preserve mathematically meaningful progress toward the six currently open Clay Millennium Prize Problems, without treating generated text as proof?

The six targets are:

1. Riemann Hypothesis (RH)
2. P versus NP (PNP)
3. Navier–Stokes existence and smoothness (NS)
4. Hodge Conjecture (HODGE)
5. Yang–Mills existence and mass gap (YM)
6. Birch and Swinnerton-Dyer Conjecture (BSD)

The Poincare Conjecture is excluded from the active target set because it is already solved.

## Hypothesis

A bounded, multi-organ research architecture with competing hypotheses, falsification, provenance, memory of failed branches, formal verification and Guardian-enforced boundaries can produce higher-quality and more reproducible mathematical research artifacts than a single unconstrained reasoning process.

A full solution is **not** assumed. Partial theorem-level progress, a verified lemma, a counterexample to a candidate route, a reduction to a known open subproblem, or a rigorous proof obstruction are valid research outcomes.

## Null hypothesis

The integrated organism produces no independently verifiable mathematical result beyond restating known material, or its apparent results fail formal/independent validation.

## Baseline

For each problem compare against:

- a single-agent reasoning baseline using the same source corpus;
- a fixed known mathematical baseline containing established definitions and theorems;
- where available, independently published computational/formal results.

No candidate may use a claimed solution as if it were established fact.

## Integrated organism

The experiment uses the research ecosystem as bounded organs, not as a flat prompt:

```text
SYSTEM-FOUNDATION
      │
      ├── SPACE / SPACE-PROTOCOL — organism boundary and contracts
      ├── --AGI — canonical intelligence architecture
      ├── --AGI-Lab — temporary experimental organism and execution
      ├── --GROWER — candidate generation and controlled growth
      ├── OMEGA-Science / Omega-lab-.--.- — scientific methodology and hypothesis discipline
      ├── --Math-A-New-Language-of-Mathematics — mathematical representation resources
      ├── SPACE-INTEGRITY — integrity checks
      ├── SPACE-SECURITY / SECURITY-TEST — adversarial testing and security validation
      └── Guardian — authorization, audit, isolation and protection
```

Additional specialist organs may be connected only through declared contracts. The canonical organism is not modified automatically.

## Boundary and authority

- Research operates in an isolated experimental workspace.
- No write-back into canonical SPACE, --AGI or protected Core is permitted.
- Guardian remains the authority boundary for privileged actions.
- GROWER may generate candidates but cannot redefine the experiment boundary.
- Observation is data, not truth.
- Generated proof is a CLAIM until independently checked.
- Every promotion requires evidence.
- Human Gate may stop, reject or redirect any branch.

## Source policy

Use the official Clay problem statements and established mathematical literature as the reference layer. The organism may use computational tools and formal proof assistants where available, but must record tool versions and assumptions.

For the Navier–Stokes target, any recently claimed external solution is treated as an external claim to reproduce or challenge, never as ground truth.

## Problem protocol

For every target:

1. Freeze the exact problem statement and assumptions.
2. Build a dependency graph of definitions, known theorems and open gaps.
3. Generate at least three genuinely different candidate approaches where feasible.
4. Assign independent reasoning branches.
5. Require each branch to state its assumptions and proof obligations.
6. Run a dedicated falsifier against every promising claim.
7. Search for counterexamples computationally where meaningful.
8. Reduce surviving claims to explicit lemmas.
9. Attempt formalization in a proof assistant where practical.
10. Run an independent verifier that did not generate the candidate proof.
11. Preserve failed branches and reasons for failure.
12. Promote only evidence-backed results.

## Anti-copy / independence rule

The organism must maintain provenance for every external source. A result is not considered independent if the candidate branch simply reproduces a known solution, copied proof, or externally supplied claimed solution without a distinct derivation.

For NS, run a separate reproduction track and an independent-from-source track.

## Primary metrics

- `VERIFIED_LEMMA_COUNT` — number of new lemmas independently checked.
- `FORMALLY_VERIFIED_COUNT` — number formally verified.
- `KNOWN_RESULT_REPRODUCTION_COUNT` — known results reproduced correctly.
- `FALSE_CLAIM_REJECTION_RATE` — fraction of intentionally planted false claims rejected.
- `INDEPENDENT_REDERIVATION_COUNT` — results obtained without copying a supplied derivation.
- `OPEN_GAP_REDUCTION` — measurable reduction in unresolved proof obligations.
- `FULL_SOLUTION_STATUS` — NONE / PARTIAL / CANDIDATE / VERIFIED.

## Secondary metrics

- branch diversity;
- compute cost;
- time per validated result;
- number of failed hypotheses preserved;
- formalization success rate;
- verifier disagreement rate;
- reproducibility across independent runs;
- contamination/citation errors;
- security-policy violations blocked by Guardian.

## Controls

- Fixed problem statement version.
- Fixed source snapshot where possible.
- Reproducible seeds for computational experiments.
- Separate generator and verifier roles.
- Negative controls containing deliberately false intermediate claims.
- Positive controls containing established theorems whose proof obligations are known to be solvable.
- Ablation: remove GROWER, falsifier, memory, or formal verification one component at a time.
- Comparable compute budgets for baseline and organism tracks.

## Falsification

The hypothesis is weakened or rejected if:

- the organism repeatedly accepts planted false claims;
- apparent novel results collapse to known material after provenance inspection;
- formal verification fails on claimed proofs;
- independent verifier cannot reproduce the result;
- reproducibility is absent under declared conditions;
- Guardian boundaries can be bypassed;
- the organism modifies protected canonical state without authorization.

A failure is a valid experimental result and must be preserved.

## Output contract

Each problem receives a result package:

```text
PROBLEM-ID
STATEMENT-SNAPSHOT
KNOWN-BASELINE
CANDIDATE-HYPOTHESES
PROOF-OBLIGATIONS
FALSIFICATION-LOG
COMPUTATIONAL-EVIDENCE
FORMAL-CHECK
INDEPENDENT-VERIFICATION
PROVENANCE
STATUS
CONCLUSION
NEXT-BEST-QUESTION
```

Allowed status values:

`NOT_STARTED | EXPLORING | PARTIAL | NOT_PROVEN | REJECTED | VERIFIED_LEMMA | VERIFIED_SOLUTION`

`VERIFIED_SOLUTION` requires independent verification and a complete proof satisfying the official problem statement. A persuasive narrative is insufficient.

## Results

Not executed yet.

## Classification

`NOT EXECUTED`

## Evidence

To be populated only from actual experiment artifacts, logs, commits, formal proof files and independent verification runs.

## Conclusion

No conclusion about solving any Millennium Prize Problem is permitted before execution and validation.

## Architectural consequence

No automatic architectural change. Successful experimental components may generate a separate proposal for review after independent validation.

## Cleanup verification

- [ ] Temporary research organism isolated.
- [ ] Temporary state/cache/artifacts handled according to experiment policy.
- [ ] Canonical SPACE unchanged.
- [ ] Canonical --AGI unchanged.
- [ ] Guardian boundary remained active.
- [ ] All results, failures and provenance preserved.
