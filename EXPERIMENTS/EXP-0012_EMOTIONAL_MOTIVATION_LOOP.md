# EXP-0012 — Emotional / Motivation Loop

**Status:** EXECUTED / FAILURE FOR TESTED HYPOTHESIS
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

- два действия;
- два типа отношения;
- правило меняется после 80 шагов обучения;
- после изменения старая стратегия становится неверной;
- последние 40 шагов используют новые context IDs для проверки переноса;
- reward: `+1` за правильное действие, `-1` за неправильное.

## Candidate internal variables

Все значения ограничены диапазоном `[-1,+1]`:

- `interest`;
- `tension`;
- `satisfaction`;
- `uncertainty`;
- `significance`.

Это вычислительные конструкции, а не доказательство субъективной эмоции.

## Controls

1. Одинаковая среда и seed для A/B/C.
2. Одинаковые observation/action spaces.
3. Сопоставимый вычислительный бюджет.
4. Ablation affective variables после первого полного запуска.
5. 20 независимых seed (`0..19`).
6. Метрики фиксированы до финальной интерпретации.
7. Для ablation C_off дополнительно проверен против B как identity control.

## Primary metrics

- adaptation time;
- cumulative reward / task utility;
- switch error rate;
- transfer performance;
- exploration after switch.

## Execution

GitHub Actions выполнил тесты и основной прогон. Все тесты прошли. Основной прогон выполнен на 20 seed.

### Primary result

| Agent | Adaptation mean | Success rate | Reward mean | Switch error | Transfer |
|---|---:|---:|---:|---:|---:|
| A_reactive | — | 0.000 | -40.00 | 1.000 | 0.000 |
| B_memory | 15.5 | 1.000 | 142.60 | 0.218 | 0.985 |
| C_organism | 14.8 | 1.000 | 115.20 | 0.270 | 0.980 |

### Affect ablation

C_on compared with the same C organism with affective modulation disabled:

- adaptation delta `(C_on − C_off)`: **-0.700 steps**;
- reward delta: **-27.400**;
- switch error delta: **+0.051875**;
- transfer delta: **-0.005**;
- C_off trace equals B trace: **1.000**.

## Interpretation

Аффективная модуляция **действительно причинно участвовала** в выборе действий: ablation воспроизводимо меняет поведение, а C_off совпадает с B по полному trace на всех 20 seed.

Но в данном протоколе она **не дала общего преимущества**. C стал немного быстрее достигать критерия адаптации, однако заплатил за это заметным снижением cumulative reward и ростом ошибки после смены правила. Перенос также не улучшился.

Следовательно, конкретная гипотеза «bounded affective-motivational loop повышает эффективность адаптации» в этом эксперименте **не подтверждена**.

## Classification

**FAILURE — для проверенной гипотезы и данной реализации.**

Это не означает, что мотивация/аффективное состояние бесполезны вообще. Эксперимент показывает только, что выбранный механизм и параметры не дали требуемого преимущества в данной контролируемой среде.

## Evidence

- `RESULTS/EXP-0012/primary_results.json` — машинные результаты и raw observations;
- `RESULTS/EXP-0012/PRIMARY_SUMMARY.md` — компактный итог;
- `RESULTS/EXP-0012/ablation_results.json` — paired ablation;
- `RESULTS/EXP-0012/ABLATION_SUMMARY.md` — итог ablation.

## Architectural consequence

**Никакого автоматического переноса в `--AGI` или Space.**

Результат остаётся лабораторным evidence. Если гипотеза будет возвращена в будущем, следующий тест должен изменить сам механизм/контрольную среду, а не подгонять параметры под полученный результат.

## Cleanup requirement

Экспериментальный организм, тестовый код, временные trigger-файлы и workflow должны быть удалены после фиксации evidence. Результаты и журнал сохраняются.
