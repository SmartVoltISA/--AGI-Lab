# EXP-0020 — Model Diagnosis

The next level after information-directed testing was executed: the diagnostic agent had to reason over competing causal models rather than only competing causes inside one model.

The result is partial. The agent can represent uncertainty over the causal model and improve model identification in moderate noise, but this did not translate into robust overall causal diagnosis. Under high noise the advantage disappeared and model identification could become worse than the fixed baseline.

This is an important negative result. It shows that `information gain` is insufficient by itself. The next required mechanism is persistent model contradiction: when observations repeatedly violate the current model's predictions, the system must allocate action to testing the model itself and compare alternative explanations.

No canonical changes. The result remains experimental evidence only.
