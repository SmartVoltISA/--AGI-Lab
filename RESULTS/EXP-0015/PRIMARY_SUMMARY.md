# EXP-0015 — Primary result

**Status:** EXECUTED  
**Seeds:** 1000

| Metric | B_memory | D_persistence | D − B |
|---|---:|---:|---:|
| First adaptation | 0.508 | 2.276 | +1.768 |
| Second adaptation | 1.699 | 2.392 | +0.693 |
| Cumulative reward | 92.424 | **98.726** | **+6.302** |
| False switches | 8.825 | **0.596** | **−8.229** |

Paired tests:
- first adaptation: p = `1.858e-90`
- second adaptation: p = `1.051e-01`
- reward: p = `3.073e-103`
- false switches: p < `1e-300` (reported by the numerical test as 0.0)

## Classification

**INCONCLUSIVE / PARTIAL SUPPORT.** Persistence strongly reduced false switching and increased cumulative reward, but it also slowed first adaptation and did not produce a statistically significant second-adaptation advantage.

The result supports a narrower mechanism-level claim: temporal persistence can improve robustness to intermittent misleading evidence. It does not establish a general metacontrol law and does not justify canonical promotion.
