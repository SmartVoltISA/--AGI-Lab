# EXP-0012 — Emotional / Motivation Loop

**Status:** PROPOSED / NOT YET EXECUTED
**Date:** 2026-09-04
**Phase:** Organism foundation

## Question

Даёт ли внутренняя значимость и мотивационно-аффективная петля измеримое преимущество в адаптации, исследовании, переключении стратегии и переносе после изменения среды?

## Hypothesis

Агент с persistent internal state, memory и bounded affective-motivational feedback может адаптироваться эффективнее реактивного агента и memory-only baseline, если внутренние переменные реально влияют на выбор действий.

Это гипотеза о механизме, а не утверждение о сознании или субъективных чувствах.

## Comparison

### A — Reactive baseline

`perception → state → action → result`

Без постоянной памяти и мотивационного состояния.

### B — Memory baseline

`perception → state → memory → action → result → memory update`

Опыт доступен следующим решениям.

### C — Organism candidate

`perception → state → memory → significance → affective state → action → result → feedback → memory/model update`

Аффективные переменные должны быть наблюдаемыми и причинно участвовать в выборе действия.

## Minimal environment

Детерминированная дискретная среда под фиксированным seed:

- ресурсы с меняющейся ценностью;
- нейтральные наблюдения;
- предотвратимые отрицательные исходы;
- несколько действий;
- изменение правила после фазы обучения;
- новый контекст для проверки переноса.

## Candidate internal variables

Все значения ограничены, например, диапазоном `[-1,+1]`:

- `interest` — ценность новизны / информации;
- `tension` — нерешённое расхождение прогноза и цели;
- `satisfaction` — результат относительно ожидания;
- `uncertainty` — штраф за слабую уверенность;
- `significance` — оценка важности текущего состояния.

Это вычислительные конструкции, а не доказательство субъективной эмоции.

## Controls

1. Одинаковая среда и seed для A/B/C.
2. Одинаковые observation/action spaces.
3. Сопоставимый вычислительный бюджет.
4. Ablation affective variables после первого полного запуска.
5. Несколько независимых seed.
6. Метрики фиксируются до просмотра финальных результатов.

## Primary metrics

- adaptation time;
- cumulative reward / task utility;
- error rate;
- strategy-switch latency;
- exploration efficiency;
- transfer performance;
- memory retention;
- recovery after repeated negative feedback.

## Critical test

После начального обучения изменить среду так, чтобы старая стратегия стала невыгодной. Проверить, обнаруживает ли C mismatch через feedback dynamics и меняет ли поведение быстрее или надёжнее B.

## Falsification

Гипотеза ослабляется или отвергается, если:

- C не превосходит B по заранее определённым primary metrics;
- эффект исчезает при повторении на независимых seed;
- преимущество объясняется дополнительной информацией или вычислениями;
- affective variables не влияют причинно на action selection;
- система становится менее стабильной без выигрыша в адаптации.

## Evidence policy

`PROPOSED ≠ EXECUTED`

`EXECUTED ≠ SUCCESSFUL`

`UNKNOWN ≠ TRUE`

Неудачный опыт сохраняется как evidence. Архитектурное утверждение должно ссылаться на воспроизводимый результат.

## Next step

Реализовать минимальную среду и A/B/C без LLM. Сначала получить baseline, затем выполнить основной тест, ablation и повторение на независимых seed.
