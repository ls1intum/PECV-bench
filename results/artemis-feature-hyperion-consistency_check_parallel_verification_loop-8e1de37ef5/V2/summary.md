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
| artemis-feature-hyperion-consistency_check_parallel_verification_loop-8e1de37ef5 | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 1 | 262 | 205 | 69 | 0.561 | 0.792 | 0.657 | 0.553 | 0.431 | 36.228 | 0.0219 |

## Per Exercise Breakdown

### artemis-feature-hyperion-consistency_check_parallel_verification_loop-8e1de37ef5 :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 | 10 | 3 | 0.643 | 0.857 | 0.735 | 0.582 | 0.451 | 30.747 | 0.0115 |
| V2/ERA2021/H03-Grafikspeicher | 9 | 12 | 9 | 0.429 | 0.500 | 0.462 | 0.579 | 0.475 | 42.789 | 0.0174 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 16 | 9 | 2 | 0.640 | 0.889 | 0.744 | 0.530 | 0.389 | 40.293 | 0.0507 |
| V2/IOS26/TC1-Bookstore | 19 | 9 | 0 | 0.679 | 1 | 0.809 | 0.411 | 0.282 | 33.073 | 0.0141 |
| V2/IOS26/TC2-Developer | 16 | 11 | 2 | 0.593 | 0.889 | 0.711 | 0.509 | 0.366 | 32.666 | 0.0154 |
| V2/ISE22/H05E01-REST_Architectural_Style | 16 | 7 | 2 | 0.696 | 0.889 | 0.780 | 0.622 | 0.508 | 43.490 | 0.0330 |
| V2/ISE22/H10E01-Containers | 16 | 12 | 2 | 0.571 | 0.889 | 0.696 | 0.510 | 0.413 | 41.928 | 0.0333 |
| V2/ITP2425/H01E01-Lectures | 28 | 15 | 2 | 0.651 | 0.933 | 0.767 | 0.501 | 0.357 | 30.489 | 0.0134 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 27 | 22 | 2 | 0.551 | 0.931 | 0.692 | 0.608 | 0.506 | 36.623 | 0.0190 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 32 | 20 | 2 | 0.615 | 0.941 | 0.744 | 0.534 | 0.399 | 38.640 | 0.0181 |
| V2/ITP2425/SE01E01-UML | 17 | 7 | 1 | 0.708 | 0.944 | 0.810 | 0.579 | 0.453 | 38.789 | 0.0143 |
| V2/MTG26/TA1-SQL_Advanced | 3 | 17 | 15 | 0.150 | 0.167 | 0.158 | 0.656 | 0.521 | 35.930 | 0.0131 |
| V2/MTG26/TA2-SQL_Basics | 7 | 18 | 11 | 0.280 | 0.389 | 0.326 | 0.604 | 0.484 | 32.389 | 0.0152 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 13 | 9 | 5 | 0.591 | 0.722 | 0.650 | 0.565 | 0.464 | 28.810 | 0.0353 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 13 | 13 | 5 | 0.500 | 0.722 | 0.591 | 0.594 | 0.485 | 36.076 | 0.0314 |
| V2/QCSL25/QC03-Magic_State_Distillation | 12 | 14 | 6 | 0.462 | 0.667 | 0.545 | 0.676 | 0.579 | 38.618 | 0.0249 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
