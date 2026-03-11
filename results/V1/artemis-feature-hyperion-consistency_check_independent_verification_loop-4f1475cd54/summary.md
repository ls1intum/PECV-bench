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
| artemis-feature-hyperion-consistency_check_independent_verification_loop-4f1475cd54 | model=azure:azure-openai-gpt-5-mini | 3 | 22 | 8 | 251 | 0.733 | 0.081 | 0.145 | 0.506 | 0.373 | 16.591 | 0.0095 |

## Per Exercise Breakdown

### artemis-feature-hyperion-consistency_check_independent_verification_loop-4f1475cd54 :: model=azure:azure-openai-gpt-5-mini
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 8 | 1 | 76 | 0.889 | 0.095 | 0.172 | 0.398 | 0.264 | 14.042 | 0.0070 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 4 | 5 | 83 | 0.444 | 0.046 | 0.083 | 0.521 | 0.381 | 18.202 | 0.0113 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 10 | 2 | 92 | 0.833 | 0.098 | 0.175 | 0.586 | 0.457 | 17.361 | 0.0100 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
