# Journal — 2026-09-04 / EXP-0014_METACONTROL_STRESS

## Result

An independent stress protocol was executed locally over 1000 seeds. It retained the core fairness constraint from EXP-0013 but introduced repeated rule changes, two high-noise evidence bursts and 80% verification reliability.

D_metacontrol retained a reward advantage over B (`478.35` vs `416.82`) but failed the broader robustness test: adaptation was slower (`4.503` vs `3.981`), false switches appeared (`0.506` per episode vs `0`), and transfer fell (`0.7136` vs `0.8100`). The paired tests support these differences.

## Classification

**FAILURE for robustness/generalization.** This is a useful negative result, not evidence that metacontrol is useless. It identifies sensitivity to evidence quality and temporal structure.

## Decision

Do not promote EXP-0013's mechanism to canonical `--AGI`.

Next experiment should make evidence reliability/persistence itself part of the metacontrol state and test whether this restores robustness without extra information or compute.

## Cleanup

No executable experiment machinery was committed. Canonical `--AGI` and Space were not modified. The stress-test result is retained as evidence.
