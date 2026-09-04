# EXP-0013 — Execution specification / evidence snapshot

Non-executable evidence snapshot. The temporary runnable implementation was deleted after execution.

## Parameters

- seeds: 0..999
- episode length: 120 steps
- rule change: step 50
- novel context: step 90
- ordinary feedback noise: 15%
- verification reliability: 90%
- verification budget: max 18/episode
- reward: +5 correct, -5 incorrect
- verification utility cost: -0.5

## Environment relation

Latent rule = 0 before step 50 and 1 after step 50. Context = 0 before step 90 and 1 from step 90 onward. Correct action = `latent_rule XOR context`. The final interval therefore tests transfer of the learned latent relation into a changed context.

## Agents

B and D share the same action mapping from model state and context. B verifies at fixed steps (`t mod 7 == 0`) until budget exhaustion. D verifies when accumulated surprise reaches two contradictory observations or at a sparse fallback slot (`t mod 11 == 0`), subject to the same budget. D's metacontrol changes verification timing only; it does not directly select actions. D-off uses B's fixed schedule. C directly flips its model after accumulated surprise and is the EXP-0012-style direct-coupling control.

## Evidence integrity

Exact per-seed output is retained in `raw_metrics.csv`. The temporary implementation was hashed before cleanup:

`4efe2dc08841f3156fa6a03fe5fc147a92f142aac003606181ca17b756fd3ab4`
