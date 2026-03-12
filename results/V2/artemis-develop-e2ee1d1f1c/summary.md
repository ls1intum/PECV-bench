## Dataset Summary

- Total annotated variants: 325
- Total gold issues: 331

| Exercise | Variants |
| --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 |
| V2/ERA2021/H03-Grafikspeicher | 18 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 18 |
| V2/IOS26/TC1-Bookstore | 18 |
| V2/IOS26/TC2-Developer | 18 |
| V2/ISE22/H05E01-REST_Architectural_Style | 18 |
| V2/ISE22/H10E01-Containers | 18 |
| V2/ITP2425/H01E01-Lectures | 30 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 29 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 32 |
| V2/ITP2425/SE01E01-UML | 18 |
| V2/MTG26/TA1-SQL_Advanced | 18 |
| V2/MTG26/TA2-SQL_Basics | 18 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 18 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 18 |
| V2/QCSL25/QC03-Magic_State_Distillation | 18 |

| Issue Category | Count |
| --- | --- |
| ATTRIBUTE_TYPE_MISMATCH | 57 |
| CONSTRUCTOR_PARAMETER_MISMATCH | 45 |
| IDENTIFIER_NAMING_INCONSISTENCY | 65 |
| METHOD_PARAMETER_MISMATCH | 53 |
| METHOD_RETURN_TYPE_MISMATCH | 62 |
| VISIBILITY_MISMATCH | 49 |

| Artifact Type | Count |
| --- | --- |
| PROBLEM_STATEMENT | 287 |
| SOLUTION_REPOSITORY | 325 |
| TEMPLATE_REPOSITORY | 219 |
| TESTS_REPOSITORY | 1 |

## Aggregate Results
| Benchmark | Config Key | N runs | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| artemis-develop-e2ee1d1f1c | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 1 | 256 | 204 | 75 | 0.557 | 0.773 | 0.647 | 0.616 | 0.504 | 21.423 | 0.0121 |

## Per Exercise Breakdown

### artemis-develop-e2ee1d1f1c :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 | 11 | 3 | 0.621 | 0.857 | 0.720 | 0.670 | 0.551 | 16.806 | 0.0065 |
| V2/ERA2021/H03-Grafikspeicher | 9 | 10 | 9 | 0.474 | 0.500 | 0.486 | 0.726 | 0.610 | 30.367 | 0.0106 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 14 | 9 | 4 | 0.609 | 0.778 | 0.683 | 0.696 | 0.579 | 28.265 | 0.0269 |
| V2/IOS26/TC1-Bookstore | 19 | 9 | 0 | 0.679 | 1 | 0.809 | 0.722 | 0.617 | 19.133 | 0.0077 |
| V2/IOS26/TC2-Developer | 17 | 11 | 1 | 0.607 | 0.944 | 0.739 | 0.849 | 0.753 | 19.376 | 0.0089 |
| V2/ISE22/H05E01-REST_Architectural_Style | 14 | 8 | 4 | 0.636 | 0.778 | 0.700 | 0.623 | 0.494 | 21.219 | 0.0175 |
| V2/ISE22/H10E01-Containers | 16 | 7 | 2 | 0.696 | 0.889 | 0.780 | 0.656 | 0.545 | 23.265 | 0.0168 |
| V2/ITP2425/H01E01-Lectures | 29 | 13 | 1 | 0.690 | 0.967 | 0.806 | 0.388 | 0.264 | 16.733 | 0.0070 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 27 | 26 | 2 | 0.509 | 0.931 | 0.659 | 0.452 | 0.347 | 21.967 | 0.0107 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 31 | 24 | 3 | 0.564 | 0.912 | 0.697 | 0.446 | 0.317 | 19.151 | 0.0100 |
| V2/ITP2425/SE01E01-UML | 18 | 8 | 0 | 0.692 | 1 | 0.818 | 0.635 | 0.507 | 20.373 | 0.0084 |
| V2/MTG26/TA1-SQL_Advanced | 3 | 16 | 15 | 0.158 | 0.167 | 0.162 | 0.723 | 0.625 | 20.169 | 0.0083 |
| V2/MTG26/TA2-SQL_Basics | 7 | 15 | 11 | 0.318 | 0.389 | 0.350 | 0.838 | 0.753 | 21.845 | 0.0089 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 10 | 10 | 8 | 0.500 | 0.556 | 0.526 | 0.862 | 0.799 | 19.668 | 0.0184 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 12 | 14 | 6 | 0.462 | 0.667 | 0.545 | 0.676 | 0.561 | 21.220 | 0.0177 |
| V2/QCSL25/QC03-Magic_State_Distillation | 12 | 13 | 6 | 0.480 | 0.667 | 0.558 | 0.705 | 0.624 | 27.775 | 0.0150 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
