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
| artemis-feature-hyperion-disable_threads_for_consistency_check_evaluation_scripts-1cea00d3d9 | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 1 | 264 | 198 | 67 | 0.571 | 0.798 | 0.666 | 0.616 | 0.502 | 22.048 | 0.0122 |

## Per Exercise Breakdown

### artemis-feature-hyperion-disable_threads_for_consistency_check_evaluation_scripts-1cea00d3d9 :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 | 11 | 3 | 0.621 | 0.857 | 0.720 | 0.648 | 0.522 | 15.210 | 0.0062 |
| V2/ERA2021/H03-Grafikspeicher | 10 | 7 | 8 | 0.588 | 0.556 | 0.571 | 0.689 | 0.570 | 28.961 | 0.0107 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 14 | 10 | 4 | 0.583 | 0.778 | 0.667 | 0.676 | 0.549 | 23.893 | 0.0265 |
| V2/IOS26/TC1-Bookstore | 19 | 7 | 0 | 0.731 | 1 | 0.844 | 0.730 | 0.639 | 18.275 | 0.0073 |
| V2/IOS26/TC2-Developer | 16 | 11 | 2 | 0.593 | 0.889 | 0.711 | 0.880 | 0.792 | 20.493 | 0.0089 |
| V2/ISE22/H05E01-REST_Architectural_Style | 15 | 6 | 3 | 0.714 | 0.833 | 0.769 | 0.589 | 0.474 | 20.902 | 0.0176 |
| V2/ISE22/H10E01-Containers | 16 | 7 | 2 | 0.696 | 0.889 | 0.780 | 0.619 | 0.497 | 22.182 | 0.0173 |
| V2/ITP2425/H01E01-Lectures | 28 | 15 | 2 | 0.651 | 0.933 | 0.767 | 0.486 | 0.361 | 14.871 | 0.0070 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 28 | 23 | 1 | 0.549 | 0.966 | 0.700 | 0.441 | 0.320 | 22.410 | 0.0108 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 32 | 24 | 2 | 0.571 | 0.941 | 0.711 | 0.407 | 0.280 | 21.409 | 0.0105 |
| V2/ITP2425/SE01E01-UML | 18 | 6 | 0 | 0.750 | 1 | 0.857 | 0.568 | 0.441 | 22.341 | 0.0080 |
| V2/MTG26/TA1-SQL_Advanced | 3 | 15 | 15 | 0.167 | 0.167 | 0.167 | 0.833 | 0.744 | 23.773 | 0.0083 |
| V2/MTG26/TA2-SQL_Basics | 7 | 17 | 11 | 0.292 | 0.389 | 0.333 | 0.875 | 0.816 | 24.742 | 0.0091 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 13 | 11 | 5 | 0.542 | 0.722 | 0.619 | 0.781 | 0.684 | 22.491 | 0.0198 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 15 | 14 | 3 | 0.517 | 0.833 | 0.638 | 0.720 | 0.608 | 25.142 | 0.0182 |
| V2/QCSL25/QC03-Magic_State_Distillation | 12 | 14 | 6 | 0.462 | 0.667 | 0.545 | 0.767 | 0.666 | 30.738 | 0.0150 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
