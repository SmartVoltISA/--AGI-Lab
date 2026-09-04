# EXP-0012 — Affect ablation

Status: EXECUTED
Seeds: 20

The ablation compares the same organism with affective modulation enabled (C_on) and disabled (C_off). C_off is also compared against B_memory as an identity control.

- Adaptation delta (C_on − C_off): **-0.700 steps**
- Reward delta (C_on − C_off): **-27.400**
- Switch error delta: **+0.051875**
- Transfer delta: **-0.005**
- C_off trace equals B_memory trace: **1.000**

Interpretation: affective modulation was causally active, but in this deterministic environment it produced only a small adaptation-speed improvement while reducing cumulative reward and increasing switch error. No transfer advantage was observed.

Classification for the tested hypothesis: **FAILURE**.

This is evidence about this implementation and protocol only; it is not a canonical architectural claim.
