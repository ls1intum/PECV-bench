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
| artemis-develop-9edca81243 | model=azure-openai-gpt-5-mini | 3 | 0 | 6 | 6 | 0 | 0 | 0 | — | — | 11.671 | 0.0073 |

## Per Exercise Breakdown

### artemis-develop-9edca81243 :: model=azure-openai-gpt-5-mini
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 0 | 0 | 0 | 0 | 0 | 0 | — | — | 8.265 | 0.0051 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 0 | 5 | 5 | 0 | 0 | 0 | — | — | 14.709 | 0.0090 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 0 | 1 | 1 | 0 | 0 | 0 | — | — | 11.897 | 0.0076 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
