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
| artemis-HEAD-66c9e6b98d | model=azure-openai-gpt-5-mini | 3 | 267 | 204 | 12 | 0.567 | 0.957 | 0.712 | 0.429 | 0.305 | 21.596 | 0.0088 |

## Per Exercise Breakdown

### artemis-HEAD-66c9e6b98d :: model=azure-openai-gpt-5-mini
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 84 | 48 | 6 | 0.636 | 0.933 | 0.757 | 0.473 | 0.342 | 19.081 | 0.0065 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 85 | 80 | 2 | 0.515 | 0.977 | 0.675 | 0.423 | 0.312 | 25.303 | 0.0105 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 98 | 76 | 4 | 0.563 | 0.961 | 0.710 | 0.395 | 0.267 | 20.596 | 0.0094 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
