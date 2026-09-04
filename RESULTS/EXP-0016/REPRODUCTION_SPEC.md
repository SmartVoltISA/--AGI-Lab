# EXP-0016 — Reproduction specification

Executed after the protocol was committed.

- Seeds: `0..999`
- Episode length: `120`
- Initial rule/model: `+1`
- Rule changes: step `50 → -1`; step `90 → +1`
- Observation reliability: `0.95`, except steps `60–74` inclusive: `0.55`
- Reward: `+1` correct, `-1` incorrect
- B: immediate revision on contradiction
- D: pre-registered adaptive threshold using only observable post-revision corroboration; threshold levels `1/2/3` at reliability-score cutoffs `0.85/0.65`; three-observation update window; initial score `0.95`
- Same observation stream per seed for B and D
- No hidden-state access or extra compute
- D_off identity control: adaptive persistence disabled, fixed threshold `1`

Local raw per-seed CSV digest (not uploaded as a repository artifact): `cd9dcb301f28fd6701e4e4d1c1076297784e59f7194ca391d36d6baf085558b4`.

The temporary executable runner and local raw-data file were disposable and were not committed. The digest is retained for evidence provenance.
