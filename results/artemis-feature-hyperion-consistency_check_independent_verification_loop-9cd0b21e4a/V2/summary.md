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
| artemis-feature-hyperion-consistency_check_independent_verification_loop-9cd0b21e4a | model=azure-openai-gpt-5.2, reasoning_effort=medium | 1 | 255 | 226 | 76 | 0.530 | 0.770 | 0.628 | 0.509 | 0.378 | 45.480 | 0 |

## Per Exercise Breakdown

### artemis-feature-hyperion-consistency_check_independent_verification_loop-9cd0b21e4a :: model=azure-openai-gpt-5.2, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 15 | 4 | 6 | 0.789 | 0.714 | 0.750 | 0.473 | 0.341 | 11.465 | 0 |
| V2/ERA2021/H03-Grafikspeicher | 9 | 10 | 9 | 0.474 | 0.500 | 0.486 | 0.735 | 0.596 | 26.160 | 0 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 12 | 6 | 6 | 0.667 | 0.667 | 0.667 | 0.529 | 0.399 | 78.288 | 0 |
| V2/IOS26/TC1-Bookstore | 18 | 1 | 1 | 0.947 | 0.947 | 0.947 | 0.547 | 0.408 | 24.176 | 0 |
| V2/IOS26/TC2-Developer | 18 | 19 | 0 | 0.486 | 1 | 0.655 | 0.612 | 0.456 | 24.418 | 0 |
| V2/ISE22/H05E01-REST_Architectural_Style | 16 | 7 | 2 | 0.696 | 0.889 | 0.780 | 0.496 | 0.370 | 97.647 | 0 |
| V2/ISE22/H10E01-Containers | 16 | 13 | 2 | 0.552 | 0.889 | 0.681 | 0.684 | 0.563 | 90.718 | 0 |
| V2/ITP2425/H01E01-Lectures | 30 | 6 | 0 | 0.833 | 1 | 0.909 | 0.486 | 0.351 | 29.216 | 0 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 28 | 31 | 1 | 0.475 | 0.966 | 0.636 | 0.381 | 0.254 | 37.271 | 0 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 32 | 20 | 2 | 0.615 | 0.941 | 0.744 | 0.441 | 0.304 | 30.640 | 0 |
| V2/ITP2425/SE01E01-UML | 17 | 1 | 1 | 0.944 | 0.944 | 0.944 | 0.617 | 0.467 | 24.915 | 0 |
| V2/MTG26/TA1-SQL_Advanced | 2 | 20 | 16 | 0.091 | 0.111 | 0.100 | 0.690 | 0.528 | 22.359 | 0 |
| V2/MTG26/TA2-SQL_Basics | 4 | 15 | 14 | 0.211 | 0.222 | 0.216 | 0.712 | 0.598 | 23.483 | 0 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 10 | 17 | 8 | 0.370 | 0.556 | 0.444 | 0.288 | 0.195 | 89.861 | 0 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 15 | 24 | 3 | 0.385 | 0.833 | 0.526 | 0.455 | 0.339 | 90.318 | 0 |
| V2/QCSL25/QC03-Magic_State_Distillation | 13 | 32 | 5 | 0.289 | 0.722 | 0.413 | 0.480 | 0.369 | 54.151 | 0 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
