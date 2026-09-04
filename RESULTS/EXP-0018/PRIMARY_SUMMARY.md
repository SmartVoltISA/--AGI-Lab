# EXP-0018 — Primary stress result

## Aggregate (3000 paired episodes)

| Metric | B_memory | D_temporal | D − B |
|---|---:|---:|---:|
| Reward | 104.567 | **118.074** | **+13.507** |
| False switches | 27.251 | **7.075** | **−20.176** |
| Correct-action rate | 0.87346 | **0.92169** | **+0.04824** |
| Model revisions | 29.558 | **7.242** | **−22.316** |

Paired Wilcoxon tests for reward, false switches, correct-action rate and revisions all returned p-values below numerical reporting precision (`p < 1e-300`).

## Scenario breakdown

| Scenario | B reward | D reward | Reward Δ | B false | D false | False Δ |
|---|---:|---:|---:|---:|---:|---:|
| A | 106.226 | **124.070** | +17.844 | 27.802 | **5.533** | −22.269 |
| B | 102.602 | **111.460** | +8.858 | 26.393 | **8.437** | −17.956 |
| C | 104.874 | **118.692** | +13.818 | 27.559 | **7.256** | −20.303 |

D improved reward and reduced false switching in **all three pre-registered scenarios**.

## Classification

**SUCCESS — independent stress/generalization support.**

The EXP-0017 temporal-evidence mechanism retained its advantage when rule-change timing and noise structure were altered. This is stronger evidence than EXP-0017 alone, but it remains bounded to these three deterministic stress families.

## Architectural consequence

No canonical change or promotion. Temporal evidence accumulation is now a replicated laboratory result and a candidate metacontrol primitive. Promotion still requires an independent implementation/validation path and broader behavioural testing.
