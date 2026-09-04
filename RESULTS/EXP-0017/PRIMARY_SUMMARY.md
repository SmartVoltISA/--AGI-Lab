# EXP-0017 — Primary result

## Run

1000 seeds (`0..999`), 120 steps, protocol fixed before execution.

| Metric | B_memory | D_temporal | D − B | Paired p |
|---|---:|---:|---:|---:|
| Reward | 96.020 | **102.872** | **+6.852** | 1.77e-131 |
| False switches | 4.680 | **0.280** | **−4.400** | 3.67e-152 |
| First adaptation delay | 0.542 | 1.160 | +0.618 | 7.27e-132 |
| Second adaptation delay | 0.609 | 1.212 | +0.603 | 1.24e-145 |
| Correct-action rate | 0.90008 | **0.92863** | **+0.02855** | 3.09e-131 |
| Model revisions | 19.182 | **5.221** | **−13.961** | 8.85e-166 |

D reduced false switching by about **94%** while improving total reward by about **7.1%** and correct-action rate by about **2.86 percentage points**. It was slower than immediate revision by about 0.6 steps at each true change, but materially faster than the fixed three-consecutive persistence mechanism tested in EXP-0015.

## Identity control

D_off disables temporal accumulation and uses immediate revision; its decision path is the B path. No hidden state or extra computation was supplied to D.

## Classification

**SUCCESS for the tested hypothesis, with scope boundary.**

The pre-registered temporal-evidence rule reduced transient false switching and improved utility in this environment. This is evidence for a useful metacontrol mechanism, not evidence of general intelligence or general regime-change detection.

## Architectural consequence

No canonical change or promotion. The result supports retaining **temporal evidence accumulation** as a laboratory mechanism for metacontrol. Before any architectural promotion, it should survive an independent stress/generalization test with altered noise structure, change timing and reliability.
