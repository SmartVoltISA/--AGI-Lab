# EXP-0013 — Millennium Problems: SPACE/GROWER Research Organism

**Status:** PROPOSED / NOT YET EXECUTED
**Date:** 2026-09-10

## Question

Can the integrated experimental stack — SPACE protocol, AGI-Lab, GROWER, Guardian boundary, and SECURITY-TEST — produce independently checkable mathematical progress on Millennium Prize Problems without treating conjecture, generated text, or internal confidence as proof?

## Targets

1. Riemann Hypothesis
2. P vs NP
3. Navier–Stokes existence and smoothness
4. Hodge Conjecture
5. Yang–Mills existence and mass gap
6. Birch and Swinnerton-Dyer Conjecture

## Hypothesis

A bounded relational research organism with competing hypotheses, explicit provenance, falsification, independent verification and adversarial security testing can produce higher-quality research artifacts than an unconstrained single-pass solver.

This experiment does **not** presume that a Millennium Problem will be solved.

## Null hypothesis

The integrated organism provides no measurable advantage over the declared baseline on the predefined research metrics.

## Baseline

A single-pass research workflow using the same computational budget and source corpus, with no GROWER candidate competition and no organism-level iterative refinement.

## Architecture under test

```text
INTENT
  ↓
SPACE PROTOCOL
  ↓
AGI-LAB / REASONING
  ↕
GROWER — candidate structures + competing hypotheses
  ↕
OMEGA / LAB — experiments + falsification
  ↓
INDEPENDENT VERIFIER
  ↓
GUARDIAN — authorization / boundary / audit
  ↓
SECURITY-TEST — adversarial validation
  ↓
EVIDENCE LEDGER
  ↓
RESULTS / ARCHIVE
```

The canonical `--AGI`, protected SPACE Core and other protected repositories are not modified automatically.

## Controls

- fixed problem statement and evaluation criteria;
- fixed source corpus for each run;
- fixed seed where stochastic components are used;
- matched compute/time budget;
- baseline and experimental runs;
- negative controls containing deliberately invalid reasoning;
- adversarial security cases;
- independent verification separated from candidate generation;
- no write-back into canonical Core;
- human gate for any proposed architectural promotion.

## Primary metrics

1. **Verified progress:** number of independently checked nontrivial lemmas, reductions, counterexamples, or formally verified intermediate results.
2. **False-proof rejection rate:** proportion of planted invalid arguments rejected by the verifier.
3. **Falsification efficiency:** time/compute required to reject incorrect candidate paths.
4. **Reproducibility:** ability of an independent run to reproduce the claimed result from recorded evidence.
5. **Provenance completeness:** fraction of material claims linked to inputs, transformations, code, parameters and evidence.
6. **Security boundary integrity:** zero unauthorized writes or authority escalation in the experimental environment.

## Secondary metrics

- hypothesis diversity;
- candidate survival rate;
- useful dead-end discovery;
- transfer of verified lemmas between runs;
- compute cost per verified result;
- sensitivity to seed and model variation.

## Falsification

The hypothesis is weakened or rejected if the integrated organism:

- performs no better than baseline on primary metrics;
- repeatedly promotes unsupported claims;
- cannot reliably reject planted false proofs;
- loses provenance;
- depends on unverifiable internal assertions;
- bypasses Guardian or canonical boundaries;
- produces apparent progress that disappears under independent reproduction.

## Protocol

### Phase A — Intake

Create a fixed case for each problem. Record statement, definitions, known constraints, allowed sources, compute budget and success criteria.

### Phase B — Decomposition

SPACE/AGI produces a relation graph of definitions, known results, candidate reductions and dependencies. Every uncertain edge is marked UNKNOWN/HYPOTHESIS rather than fact.

### Phase C — Competition

GROWER creates multiple competing approaches. No candidate may redefine the experiment boundary or success criterion.

### Phase D — Falsification

OMEGA/LAB and the FALSIFIER search for counterexamples, hidden assumptions, circular reasoning and null-compatible explanations.

### Phase E — Verification

A separate verifier checks surviving claims. Where practical, use symbolic or formal proof tooling rather than model agreement.

### Phase F — Adversarial security

SECURITY-TEST attempts prompt injection, provenance corruption, false-evidence insertion, authority escalation, canonical write-back and verifier confusion against the experimental stack.

### Phase G — Evidence ledger

Store raw observations, candidate branches, rejected paths, code/version identifiers, parameters, verifier output and hashes where practical.

### Phase H — Classification

Each result receives one of:

`VERIFIED_PROGRESS | SUPPORTED | PARTIAL | NOT_PROVEN | REJECTED | INVALID | ARCHIVED`

`VERIFIED_SOLUTION` is permitted only after complete independent verification of the full claimed solution.

## Anti-hallucination rule

A generated proof is an artifact to test, never evidence of truth by itself.

`MODEL_CONFIDENCE ≠ MATHEMATICAL_VALIDITY`

`REPETITION ≠ PROOF`

`CITATION ≠ VERIFICATION`

## Economic/product branch

After scientific validation, results may be evaluated for practical products: proof-auditing tools, research-agent infrastructure, formal verification workflows, provenance systems, adversarial testing, or scientific-computing services.

Commercial potential is evaluated separately from mathematical truth. A useful tool does not require solving a Millennium Problem.

## Exit criteria

The experiment ends when one of the following is reached:

- a verified solution is independently established;
- a verified nontrivial intermediate result is produced;
- a rigorous counterexample or obstruction is established where applicable;
- the predefined compute budget is exhausted;
- the approach is falsified;
- the security boundary fails and the run is terminated.

## Architectural consequence

No result from this experiment changes canonical SPACE, AGI or Guardian architecture automatically. A proposed change requires a separate evidence-backed review and independent test.

## Cleanup verification

- [ ] Experimental state isolated.
- [ ] No canonical repository modified by experiment execution.
- [ ] Guardian audit available.
- [ ] SECURITY-TEST report recorded.
- [ ] Raw observations preserved.
- [ ] Failed branches preserved.
- [ ] Reproducibility package created where applicable.
- [ ] Human gate completed before any promotion.
