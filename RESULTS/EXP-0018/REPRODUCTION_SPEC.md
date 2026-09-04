# EXP-0018 — Reproduction specification

Three scenarios, 1000 seeds each, 140 steps. B immediate revision; D exactly EXP-0017 temporal accumulator (`S+=1` on contradiction, `S*=0.5` on corroboration, revise at `S>=2`). Same RNG seed and observation stream within each B/D pair; no hidden state or extra compute.

Scenario A: changes 35→-1, 105→+1; burst 55–63 at 0.60; otherwise 0.90.
Scenario B: changes 45→-1, 75→+1, 110→-1; bursts 20–34 at 0.70 and 82–101 at 0.55; otherwise 0.95.
Scenario C: changes 28→-1, 67→+1, 119→-1; bursts 40–52 at 0.65 and 88–96 at 0.60; otherwise 0.92.

Raw per-seed stress data was generated locally and removed after hashing. SHA-256: `93b4680a41a288a08fa41696fbe6e2c9b59ac76c8d41b6d05bda792a4cbfb715`.
