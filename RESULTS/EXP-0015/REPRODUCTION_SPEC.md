# EXP-0015 — Reproduction specification

The executed run used the following deterministic specification.

- Seeds: `0..999`
- Episode length: 120 steps
- Initial rule: `+1`
- Rule changes: step 50 → `-1`; step 90 → `+1`
- Observation reliability: `0.95`, except steps 60–74 inclusive: `0.55`
- Reward: `+1` if action equals current rule, otherwise `-1`
- Initial model: `+1`
- B_memory revision: if observation differs from model, immediately set model = observation
- D_persistence revision: maintain contradiction streak; increment on surprising observation, reset to zero on corroboration; set model = observation only when streak reaches 3
- B and D receive the same observation stream for each seed
- No hidden state is exposed to either agent
- No additional computation is granted to D

Raw result digest (SHA-256): `504ca6e6209370f4598ee1304a61f9caa3850d0455357a50f941bbbd7449e053`

This specification is retained because the temporary executable runner is disposable by experiment policy.
