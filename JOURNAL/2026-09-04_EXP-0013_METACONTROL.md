# Journal — 2026-09-04 / EXP-0013_METACONTROL

## Scope

EXP-0013 tested whether bounded internal significance/surprise can improve adaptation when used as metacontrol of model verification rather than as a direct action selector. The experiment was isolated to `--AGI-Lab`.

`--AGI` and Space were not modified.

## Protocol revision before execution

B and D received identical observable information, action space, environment, seeds and episode length. B and D use the same action policy whenever model state is identical. D cannot observe hidden state and cannot obtain unbounded computation. Verification is a finite resource with a maximum budget of 18 operations per episode. B uses a fixed schedule. D changes only when it spends verification, based on accumulated surprise. D-off uses B's schedule as an identity control. C is the direct affect-to-action control from EXP-0012.

## Execution

- deterministic discrete environment;
- latent rule change at step 50;
- 15% misleading ordinary feedback;
- verification reliability 90%;
- novel context from step 90;
- 1000 seeds (`0..999`);
- execution completed.

## Results

B: adaptation 6.13 steps mean; reward 412.78; false-switch rate 0.3532; transfer 0.8975.

C: adaptation 1.66 steps mean; reward 350.53; transfer 0.7396. Direct coupling was fast but lower utility and weaker transfer.

D: adaptation 2.63 steps mean (median 1); reward 516.06; false-switch rate 0.3028; transfer 0.9364; 16.71 verifications/episode on average.

D vs B: adaptation −3.50 steps, reward +103.28, false-switch rate −0.0504, post-change false switches −0.110, transfer +0.0389, correct-action rate +0.0855.

D adaptation succeeded in 99.0% of seeds.

D-off matched B exactly on all 1000 decision traces.

## Classification

**SUCCESS for the tested hypothesis.** The causal control supports the interpretation that the gain came from metacontrol of verification timing rather than a changed action policy.

## Interpretation boundary

This is evidence for this implementation and protocol only. It is not a general proof about emotion, consciousness or AGI. An independent environment/protocol is required before architectural promotion.

## Cleanup

Temporary executable experiment machinery was deleted after execution. Results, raw observations, parameters, journal and execution specification remain. Canonical `--AGI` and Space remain unchanged.
