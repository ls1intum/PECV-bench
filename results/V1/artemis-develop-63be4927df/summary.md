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
| artemis-develop-63be4927df | model=azure-openai-gpt-5-mini | 3 | 2 | 7 | 277 | 0.222 | 0.007 | 0.014 | 0.486 | 0.348 | 11.932 | 0.0074 |

## Per Exercise Breakdown

### artemis-develop-63be4927df :: model=azure-openai-gpt-5-mini
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 2 | 3 | 88 | 0.400 | 0.022 | 0.042 | 0.486 | 0.348 | 9.262 | 0.0053 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 0 | 3 | 87 | 0 | 0 | 0 | — | — | 14.766 | 0.0091 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 0 | 1 | 102 | 0 | 0 | 0 | — | — | 11.867 | 0.0078 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
