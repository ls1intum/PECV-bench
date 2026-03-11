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
| artemis-develop-9edca81243 | model=azure-openai-gpt-5-mini | 1 | 0 | 2 | 3 | 0 | 0 | 0 | — | — | 11.051 | 0.0072 |
| artemis-develop-9edca81243 | model=azure:azure-openai-gpt-5-mini | 2 | 1 | 9 | 9 | 0.100 | 0.100 | 0.100 | 0.077 | 0.040 | 11.255 | 0.0072 |

## Per Exercise Breakdown

### artemis-develop-9edca81243 :: model=azure-openai-gpt-5-mini
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 0 | 0 | 0 | 0 | 0 | 0 | — | — | 7.808 | 0.0050 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 0 | 1 | 1 | 0 | 0 | 0 | — | — | 13.452 | 0.0088 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 0 | 1 | 2 | 0 | 0 | 0 | — | — | 11.713 | 0.0076 |

### artemis-develop-9edca81243 :: model=azure:azure-openai-gpt-5-mini
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 0 | 0 | 0 | 0 | 0 | 0 | — | — | 8.402 | 0.0051 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 0 | 3 | 3 | 0 | 0 | 0 | — | — | 13.247 | 0.0088 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 1 | 6 | 6 | 0.143 | 0.143 | 0.143 | 0.077 | 0.040 | 11.947 | 0.0076 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
