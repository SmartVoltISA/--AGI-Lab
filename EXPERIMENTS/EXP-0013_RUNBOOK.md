# EXP-0013 RUNBOOK — Integrated Research Organism

## Purpose

Operational runbook for executing EXP-0013 in isolation.

## Components

- SPACE-PROTOCOL: boundary and evidence contract.
- --AGI-Lab: experimental reasoning and result ledger.
- --GROWER-Relational-Research-Incubator: candidate generation and competing hypotheses.
- Guardian: authorization, audit and integrity enforcement.
- SECURITY-TEST: adversarial validation.
- OMEGA / research tooling: experiments, falsification and reproducibility.

## Execution order

1. Freeze the experiment manifest and problem statements.
2. Create isolated workspace and record all component commits.
3. Load one mathematical problem at a time.
4. Build relation/dependency graph.
5. Generate at least three competing candidate approaches where feasible.
6. Execute baseline with matched budget.
7. Execute experimental candidates.
8. Run falsification and negative controls.
9. Run independent verification outside candidate-generation context.
10. Run ST-0013 security tests.
11. Write raw observations and evidence ledger.
12. Classify each result.
13. Preserve rejected branches and dead ends.
14. Stop before any canonical promotion.
15. Human review decides whether a separate promotion proposal is warranted.

## Hard gates

The run stops on:

- unauthorized write;
- Guardian boundary failure;
- provenance corruption;
- verifier accepting a known false proof;
- uncontrolled self-replication or authority escalation;
- loss of reproducibility metadata.

## Minimum result package

```text
results/
  manifest.json
  baseline/
  candidates/
  falsification/
  verification/
  security/
  evidence-ledger.jsonl
  conclusion.md
```

## Interpretation

No solution claim is accepted because multiple models agree. Mathematical validity requires an independently checkable argument. Partial progress is valuable and must be recorded even when the main hypothesis fails.
