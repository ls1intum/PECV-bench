# Variants Analysis Report

## Dataset Summary

- Total annotated variants: 91
- Total gold issues: 93

| Exercise | Variants |
| --- | --- |
| V1/ITP2425/H01E01-Lectures | 30 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 29 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 32 |

| Issue Category | Count |
| --- | --- |
| ATTRIBUTE_TYPE_MISMATCH | 17 |
| CONSTRUCTOR_PARAMETER_MISMATCH | 10 |
| IDENTIFIER_NAMING_INCONSISTENCY | 23 |
| METHOD_PARAMETER_MISMATCH | 12 |
| METHOD_RETURN_TYPE_MISMATCH | 19 |
| VISIBILITY_MISMATCH | 12 |

| Artifact Type | Count |
| --- | --- |
| PROBLEM_STATEMENT | 89 |
| SOLUTION_REPOSITORY | 90 |
| TEMPLATE_REPOSITORY | 40 |

## Aggregate Results
| Benchmark | Config Key | N runs | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| artemis-feature-hyperion-unified-consistency-check-32471b9a64 | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 3 | 265 | 34 | 14 | 0.886 | 0.950 | 0.917 | 0.445 | 0.320 | 65.087 | 0.0055 |
| pecv-reference | model=openai:gpt-5-mini, reasoning_effort=medium | 3 | 262 | 197 | 17 | 0.571 | 0.939 | 0.710 | 0.433 | 0.308 | 31.634 | 0 |

## Per Exercise Breakdown

### artemis-feature-hyperion-unified-consistency-check-32471b9a64 :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 84 | 10 | 6 | 0.894 | 0.933 | 0.913 | 0.487 | 0.358 | 55.792 | 0.0044 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 86 | 14 | 1 | 0.860 | 0.989 | 0.920 | 0.438 | 0.324 | 79.784 | 0.0064 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 95 | 10 | 7 | 0.905 | 0.931 | 0.918 | 0.415 | 0.284 | 60.482 | 0.0056 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*


## Correlation Analysis: Input Tokens vs F1 Score

| Model Name | Correlation | P-Value | N Samples |
| :--- | :--- | :--- | :--- |
| azure-openai-gpt-5-mini |    0.063 |    0.301 | 273 |

*Significance: \*\*\* p<0.001, \*\* p<0.01, \* p<0.05*

## Per-Exercise Correlation Analysis

| Model | Exercise | Correlation | P-Value | N |
| :--- | :--- | :--- | :--- | :--- |
| azure-openai-gpt-5-mini | V1/ITP2425/H01E01-Lectures |   -0.041 |    0.703 | 90 |
| azure-openai-gpt-5-mini | V1/ITP2425/H02E02-Panic_at_Seal_Saloon |   -0.043 |    0.695 | 87 |
| azure-openai-gpt-5-mini | V1/ITP2425/H05E01-Space_Seal_Farm |   -0.139 |    0.178 | 96 |


## Visualizations

### Model Performance (Tokens vs F1)
![Per Model Analysis](variants_report_plots/per_model.png)

### Detailed Performance by Exercise
![Per Model Per Exercise](variants_report_plots/per_model_per_exercise.png)
