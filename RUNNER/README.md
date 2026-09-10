# EXP-0013 Local Runner

Safe local execution harness for `EXP-0013_MILLENNIUM_ORGANISM`.

The runner is deliberately dependency-free Python 3. It does **not** claim to solve a Millennium Problem. It executes the research lifecycle, records candidate branches, falsification checks, verification status, provenance, and security-gate results.

## Safety model

- Offline by default.
- No network calls.
- No writes to canonical SPACE or `--AGI`.
- Results are written only below the selected local run directory.
- External model/solver integrations are adapters; their output is untrusted evidence until independently verified.
- `VERIFIED_SOLUTION` can never be emitted by the fixture runner.

## Quick start

```bash
cd --AGI-Lab
python3 RUNNER/runner.py --fixture
```

For a real local research provider, implement the JSON contract described in `RUNNER/provider_contract.json` and invoke the runner with `--provider path/to/provider.py`.

## Outputs

Each run creates:

```text
<run-dir>/
  manifest.json
  candidates.jsonl
  falsification.jsonl
  verification.jsonl
  security.jsonl
  evidence-ledger.jsonl
  conclusion.md
```

The fixture mode intentionally includes a false lemma and a circular argument so the rejection path can be tested before connecting any expensive research model.
