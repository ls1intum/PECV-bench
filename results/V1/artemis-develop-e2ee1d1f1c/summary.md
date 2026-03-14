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
| artemis-develop-e2ee1d1f1c | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 3 | 260 | 169 | 19 | 0.606 | 0.932 | 0.734 | 0.427 | 0.306 | 19.412 | 0.0093 |

## Per Exercise Breakdown

### artemis-develop-e2ee1d1f1c :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 85 | 35 | 5 | 0.708 | 0.944 | 0.810 | 0.474 | 0.345 | 16.644 | 0.0070 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 84 | 71 | 3 | 0.542 | 0.966 | 0.694 | 0.422 | 0.313 | 22.369 | 0.0109 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 91 | 63 | 11 | 0.591 | 0.892 | 0.711 | 0.389 | 0.265 | 19.327 | 0.0099 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
