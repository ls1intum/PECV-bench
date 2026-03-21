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
| artemis-feature-hyperion-consistency_check_independent_verification_loop-4dee35a34f | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 1 | 246 | 61 | 85 | 0.801 | 0.743 | 0.771 | 0.512 | 0.386 | 35.043 | 0.0177 |

## Per Exercise Breakdown

### artemis-feature-hyperion-consistency_check_independent_verification_loop-4dee35a34f :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 17 | 2 | 4 | 0.895 | 0.810 | 0.850 | 0.490 | 0.349 | 31.493 | 0.0097 |
| V2/ERA2021/H03-Grafikspeicher | 7 | 6 | 11 | 0.538 | 0.389 | 0.452 | 0.762 | 0.659 | 42.224 | 0.0145 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 14 | 3 | 4 | 0.824 | 0.778 | 0.800 | 0.473 | 0.344 | 39.821 | 0.0396 |
| V2/IOS26/TC1-Bookstore | 18 | 0 | 1 | 1 | 0.947 | 0.973 | 0.424 | 0.277 | 31.430 | 0.0113 |
| V2/IOS26/TC2-Developer | 16 | 1 | 2 | 0.941 | 0.889 | 0.914 | 0.462 | 0.320 | 37.619 | 0.0132 |
| V2/ISE22/H05E01-REST_Architectural_Style | 14 | 1 | 4 | 0.933 | 0.778 | 0.848 | 0.411 | 0.277 | 35.717 | 0.0255 |
| V2/ISE22/H10E01-Containers | 15 | 2 | 3 | 0.882 | 0.833 | 0.857 | 0.542 | 0.436 | 36.062 | 0.0253 |
| V2/ITP2425/H01E01-Lectures | 28 | 3 | 2 | 0.903 | 0.933 | 0.918 | 0.521 | 0.400 | 30.451 | 0.0112 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 28 | 5 | 1 | 0.848 | 0.966 | 0.903 | 0.626 | 0.514 | 35.262 | 0.0158 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 32 | 4 | 2 | 0.889 | 0.941 | 0.914 | 0.518 | 0.384 | 36.766 | 0.0150 |
| V2/ITP2425/SE01E01-UML | 16 | 0 | 2 | 1 | 0.889 | 0.941 | 0.532 | 0.393 | 35.588 | 0.0116 |
| V2/MTG26/TA1-SQL_Advanced | 1 | 12 | 17 | 0.077 | 0.056 | 0.065 | 0.909 | 0.833 | 29.592 | 0.0112 |
| V2/MTG26/TA2-SQL_Basics | 7 | 11 | 11 | 0.389 | 0.389 | 0.389 | 0.650 | 0.537 | 33.961 | 0.0128 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 10 | 3 | 8 | 0.769 | 0.556 | 0.645 | 0.376 | 0.293 | 30.341 | 0.0280 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 13 | 3 | 5 | 0.812 | 0.722 | 0.765 | 0.581 | 0.432 | 34.979 | 0.0253 |
| V2/QCSL25/QC03-Magic_State_Distillation | 10 | 5 | 8 | 0.667 | 0.556 | 0.606 | 0.278 | 0.171 | 40.967 | 0.0209 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
