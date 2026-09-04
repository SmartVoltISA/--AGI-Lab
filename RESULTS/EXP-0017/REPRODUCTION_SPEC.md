# EXP-0017 — Reproduction specification

- Seeds: `0..999`
- Episode length: `120`
- Initial rule/model: `+1`
- Rule changes: step `50 → -1`; step `90 → +1`
- Observation reliability: `0.95`, except steps `60–74`: `0.55`
- Reward: `+1/-1`
- B: immediate revision on contradiction
- D: `S=0`; contradiction `S+=1`; corroboration `S*=0.5`; revise when `S>=2`; reset `S=0` after revision
- Same observation stream per seed
- No hidden state or extra computation
- D_off identity control follows B

Local raw per-seed CSV was generated from the executed run and removed from the disposable runtime after hashing. SHA-256: `b71f740d241417323babcd2fba865ef40c137f7b898b7cb0ea4f4a34ea641881`.

Aggregate results are retained in `PRIMARY_SUMMARY.md`; protocol and journal are the authoritative experiment record.
