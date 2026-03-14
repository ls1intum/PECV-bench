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
| pecv-reference | model=openai:gpt-5-mini, reasoning_effort=medium | 1 | 267 | 207 | 64 | 0.563 | 0.807 | 0.663 | 0.630 | 0.519 | 36.701 | 0 |

## Per Exercise Breakdown

### pecv-reference :: model=openai:gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 | 8 | 3 | 0.692 | 0.857 | 0.766 | 0.614 | 0.489 | 23.449 | 0 |
| V2/ERA2021/H03-Grafikspeicher | 11 | 10 | 7 | 0.524 | 0.611 | 0.564 | 0.871 | 0.786 | 56.273 | 0 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 15 | 10 | 3 | 0.600 | 0.833 | 0.698 | 0.699 | 0.590 | 43.637 | 0 |
| V2/IOS26/TC1-Bookstore | 18 | 6 | 1 | 0.750 | 0.947 | 0.837 | 0.758 | 0.670 | 25.992 | 0 |
| V2/IOS26/TC2-Developer | 16 | 9 | 2 | 0.640 | 0.889 | 0.744 | 0.857 | 0.762 | 38.458 | 0 |
| V2/ISE22/H05E01-REST_Architectural_Style | 15 | 11 | 3 | 0.577 | 0.833 | 0.682 | 0.621 | 0.495 | 37.940 | 0 |
| V2/ISE22/H10E01-Containers | 17 | 7 | 1 | 0.708 | 0.944 | 0.810 | 0.685 | 0.587 | 31.396 | 0 |
| V2/ITP2425/H01E01-Lectures | 27 | 15 | 3 | 0.643 | 0.900 | 0.750 | 0.494 | 0.363 | 23.637 | 0 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 27 | 27 | 2 | 0.500 | 0.931 | 0.651 | 0.394 | 0.271 | 37.583 | 0 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 34 | 22 | 0 | 0.607 | 1 | 0.756 | 0.397 | 0.274 | 38.222 | 0 |
| V2/ITP2425/SE01E01-UML | 18 | 8 | 0 | 0.692 | 1 | 0.818 | 0.725 | 0.601 | 37.503 | 0 |
| V2/MTG26/TA1-SQL_Advanced | 4 | 14 | 14 | 0.222 | 0.222 | 0.222 | 0.869 | 0.785 | 36.673 | 0 |
| V2/MTG26/TA2-SQL_Basics | 9 | 14 | 9 | 0.391 | 0.500 | 0.439 | 0.798 | 0.719 | 31.462 | 0 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 11 | 11 | 7 | 0.500 | 0.611 | 0.550 | 0.755 | 0.647 | 34.118 | 0 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 12 | 18 | 6 | 0.400 | 0.667 | 0.500 | 0.780 | 0.658 | 37.680 | 0 |
| V2/QCSL25/QC03-Magic_State_Distillation | 15 | 17 | 3 | 0.469 | 0.833 | 0.600 | 0.666 | 0.583 | 60.189 | 0 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
