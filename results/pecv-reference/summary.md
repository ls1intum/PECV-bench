## Dataset Summary

- Total annotated variants: 149
- Total gold issues: 179

| Exercise | Variants |
| --- | --- |
| ISE22/H05E01-REST_Architectural_Style | 22 |
| ISE22/H10E01-Containers | 18 |
| ITP2425/H01E01-Lectures | 30 |
| ITP2425/H02E02-Panic_at_Seal_Saloon | 29 |
| ITP2425/H05E01-Space_Seal_Farm | 32 |
| ITP2425/SE01E01-UML | 18 |

| Issue Category | Count |
| --- | --- |
| ATTRIBUTE_TYPE_MISMATCH | 30 |
| CONSTRUCTOR_PARAMETER_MISMATCH | 18 |
| IDENTIFIER_NAMING_INCONSISTENCY | 51 |
| METHOD_PARAMETER_MISMATCH | 30 |
| METHOD_RETURN_TYPE_MISMATCH | 29 |
| VISIBILITY_MISMATCH | 21 |

| Artifact Type | Count |
| --- | --- |
| PROBLEM_STATEMENT | 155 |
| SOLUTION_REPOSITORY | 158 |
| TEMPLATE_REPOSITORY | 95 |

## Aggregate Results
| Benchmark | Config Key | N runs | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pecv-reference | default | 15 | 1228 | 1478 | 124 | 0.454 | 0.908 | 0.605 | 0.586 | 0.471 | 24.687 | 0.0181 |

## Per Exercise Breakdown

### pecv-reference :: default
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITP2425/H01E01-Lectures | 399 | 318 | 39 | 0.556 | 0.911 | 0.691 | 0.616 | 0.489 | 19.854 | 0.0134 |
| ITP2425/H02E02-Panic_at_Seal_Saloon | 385 | 344 | 34 | 0.528 | 0.919 | 0.671 | 0.590 | 0.491 | 26.128 | 0.0208 |
| ITP2425/H05E01-Space_Seal_Farm | 444 | 816 | 51 | 0.352 | 0.897 | 0.506 | 0.555 | 0.437 | 27.940 | 0.0202 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
