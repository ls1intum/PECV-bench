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
| artemis-feature-hyperion-consistency_check_independent_verification_loop-4f1475cd54 | default | 1 | 50 | 10 | 41 | 0.833 | 0.549 | 0.662 | 0.555 | 0.423 | 30.281 | 0.0122 |

## Per Exercise Breakdown

### artemis-feature-hyperion-consistency_check_independent_verification_loop-4f1475cd54 :: default
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 4 | 2 | 24 | 0.667 | 0.143 | 0.235 | 0.729 | 0.608 | 15.905 | 0.0072 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 14 | 6 | 15 | 0.700 | 0.483 | 0.571 | 0.526 | 0.398 | 33.209 | 0.0140 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 32 | 2 | 2 | 0.941 | 0.941 | 0.941 | 0.546 | 0.410 | 40.205 | 0.0149 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
