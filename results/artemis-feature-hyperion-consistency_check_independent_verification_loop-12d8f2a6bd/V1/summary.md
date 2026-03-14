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
| artemis-feature-hyperion-consistency_check_independent_verification_loop-12d8f2a6bd | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 3 | 259 | 31 | 20 | 0.893 | 0.928 | 0.910 | 0.564 | 0.433 | 35.947 | 0.0141 |

## Per Exercise Breakdown

### artemis-feature-hyperion-consistency_check_independent_verification_loop-12d8f2a6bd :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1/ITP2425/H01E01-Lectures | 84 | 8 | 6 | 0.913 | 0.933 | 0.923 | 0.534 | 0.400 | 30.199 | 0.0113 |
| V1/ITP2425/H02E02-Panic_at_Seal_Saloon | 79 | 14 | 8 | 0.849 | 0.908 | 0.878 | 0.599 | 0.480 | 37.608 | 0.0158 |
| V1/ITP2425/H05E01-Space_Seal_Farm | 96 | 9 | 6 | 0.914 | 0.941 | 0.928 | 0.561 | 0.424 | 39.831 | 0.0152 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
