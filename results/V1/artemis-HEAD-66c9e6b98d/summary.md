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
| artemis-HEAD-66c9e6b98d | model=azure-openai-gpt-5-mini | 3 | 259 | 201 | 14 | 0.563 | 0.949 | 0.707 | 0.453 | 0.329 | 20.417 | 0.0088 |

## Per Exercise Breakdown

### artemis-HEAD-66c9e6b98d :: model=azure-openai-gpt-5-mini
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 79 | 46 | 5 | 0.632 | 0.940 | 0.756 | 0.495 | 0.362 | 17.494 | 0.0065 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 82 | 86 | 5 | 0.488 | 0.943 | 0.643 | 0.429 | 0.324 | 22.654 | 0.0105 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 98 | 69 | 4 | 0.587 | 0.961 | 0.729 | 0.439 | 0.306 | 20.946 | 0.0092 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
