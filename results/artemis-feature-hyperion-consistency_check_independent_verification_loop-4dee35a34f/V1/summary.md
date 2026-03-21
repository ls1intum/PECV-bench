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
| artemis-feature-hyperion-consistency_check_independent_verification_loop-4dee35a34f | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 3 | 258 | 29 | 21 | 0.899 | 0.925 | 0.912 | 0.518 | 0.386 | 34.604 | 0.0140 |

## Per Exercise Breakdown

### artemis-feature-hyperion-consistency_check_independent_verification_loop-4dee35a34f :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 85 | 5 | 5 | 0.944 | 0.944 | 0.944 | 0.482 | 0.344 | 30.155 | 0.0113 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 81 | 17 | 6 | 0.827 | 0.931 | 0.876 | 0.584 | 0.463 | 36.895 | 0.0158 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 92 | 7 | 10 | 0.929 | 0.902 | 0.915 | 0.494 | 0.357 | 36.698 | 0.0150 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
