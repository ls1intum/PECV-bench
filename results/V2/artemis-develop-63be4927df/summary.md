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
| artemis-develop-63be4927df | model=azure-openai-gpt-5-mini | 1 | 262 | 185 | 69 | 0.586 | 0.792 | 0.674 | 0.629 | 0.514 | 24.090 | 0.0120 |

## Per Exercise Breakdown

### artemis-develop-63be4927df :: model=azure-openai-gpt-5-mini
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 | 8 | 3 | 0.692 | 0.857 | 0.766 | 0.610 | 0.480 | 19.195 | 0.0063 |
| V2/ERA2021/H03-Grafikspeicher | 10 | 11 | 8 | 0.476 | 0.556 | 0.513 | 0.741 | 0.628 | 35.050 | 0.0107 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 15 | 8 | 3 | 0.652 | 0.833 | 0.732 | 0.711 | 0.586 | 28.111 | 0.0269 |
| V2/IOS26/TC1-Bookstore | 19 | 7 | 0 | 0.731 | 1 | 0.844 | 0.764 | 0.661 | 20.561 | 0.0072 |
| V2/IOS26/TC2-Developer | 17 | 9 | 1 | 0.654 | 0.944 | 0.773 | 0.893 | 0.814 | 22.486 | 0.0089 |
| V2/ISE22/H05E01-REST_Architectural_Style | 14 | 9 | 4 | 0.609 | 0.778 | 0.683 | 0.582 | 0.468 | 23.601 | 0.0171 |
| V2/ISE22/H10E01-Containers | 15 | 9 | 3 | 0.625 | 0.833 | 0.714 | 0.691 | 0.568 | 25.156 | 0.0166 |
| V2/ITP2425/H01E01-Lectures | 28 | 15 | 2 | 0.651 | 0.933 | 0.767 | 0.472 | 0.346 | 19.837 | 0.0071 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 27 | 22 | 2 | 0.551 | 0.931 | 0.692 | 0.428 | 0.307 | 24.867 | 0.0109 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 31 | 18 | 3 | 0.633 | 0.912 | 0.747 | 0.412 | 0.284 | 20.547 | 0.0095 |
| V2/ITP2425/SE01E01-UML | 18 | 6 | 0 | 0.750 | 1 | 0.857 | 0.678 | 0.540 | 21.632 | 0.0079 |
| V2/MTG26/TA1-SQL_Advanced | 3 | 16 | 15 | 0.158 | 0.167 | 0.162 | 0.867 | 0.792 | 24.192 | 0.0082 |
| V2/MTG26/TA2-SQL_Basics | 9 | 13 | 9 | 0.409 | 0.500 | 0.450 | 0.866 | 0.784 | 26.366 | 0.0085 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 13 | 9 | 5 | 0.591 | 0.722 | 0.650 | 0.748 | 0.665 | 21.640 | 0.0189 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 12 | 12 | 6 | 0.500 | 0.667 | 0.571 | 0.746 | 0.632 | 22.943 | 0.0175 |
| V2/QCSL25/QC03-Magic_State_Distillation | 13 | 13 | 5 | 0.500 | 0.722 | 0.591 | 0.679 | 0.563 | 34.368 | 0.0150 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
