# Variants Analysis Report

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
| artemis-HEAD-66c9e6b98d | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 1 | 260 | 230 | 71 | 0.531 | 0.785 | 0.633 | 0.625 | 0.511 | 27.328 | 0.0117 |
| pecv-reference | model=openai:gpt-5-mini, reasoning_effort=medium | 1 | 267 | 207 | 64 | 0.563 | 0.807 | 0.663 | 0.630 | 0.519 | 36.701 | 0 |

## Per Exercise Breakdown

### artemis-HEAD-66c9e6b98d :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 | 16 | 3 | 0.529 | 0.857 | 0.655 | 0.687 | 0.564 | 15.011 | 0.0064 |
| V2/ERA2021/H03-Grafikspeicher | 11 | 11 | 7 | 0.500 | 0.611 | 0.550 | 0.731 | 0.628 | 28.008 | 0.0098 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 16 | 8 | 2 | 0.667 | 0.889 | 0.762 | 0.703 | 0.578 | 23.885 | 0.0262 |
| V2/IOS26/TC1-Bookstore | 19 | 9 | 0 | 0.679 | 1 | 0.809 | 0.745 | 0.648 | 16.805 | 0.0080 |
| V2/IOS26/TC2-Developer | 17 | 13 | 1 | 0.567 | 0.944 | 0.708 | 0.888 | 0.810 | 21.464 | 0.0100 |
| V2/ISE22/H05E01-REST_Architectural_Style | 15 | 11 | 3 | 0.577 | 0.833 | 0.682 | 0.593 | 0.473 | 21.278 | 0.0170 |
| V2/ISE22/H10E01-Containers | 16 | 9 | 2 | 0.640 | 0.889 | 0.744 | 0.675 | 0.561 | 20.081 | 0.0140 |
| V2/ITP2425/H01E01-Lectures | 28 | 18 | 2 | 0.609 | 0.933 | 0.737 | 0.445 | 0.318 | 15.453 | 0.0066 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 26 | 32 | 3 | 0.448 | 0.897 | 0.598 | 0.456 | 0.331 | 22.245 | 0.0105 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 32 | 31 | 2 | 0.508 | 0.941 | 0.660 | 0.443 | 0.308 | 19.585 | 0.0097 |
| V2/ITP2425/SE01E01-UML | 17 | 12 | 1 | 0.586 | 0.944 | 0.723 | 0.625 | 0.490 | 21.689 | 0.0074 |
| V2/MTG26/TA1-SQL_Advanced | 0 | 0 | 18 | 0 | 0 | 0 | — | — | 137.659 | 0 |
| V2/MTG26/TA2-SQL_Basics | 8 | 14 | 10 | 0.364 | 0.444 | 0.400 | 0.796 | 0.712 | 19.439 | 0.0080 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 11 | 13 | 7 | 0.458 | 0.611 | 0.524 | 0.815 | 0.720 | 20.625 | 0.0216 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 13 | 16 | 5 | 0.448 | 0.722 | 0.553 | 0.640 | 0.540 | 21.958 | 0.0199 |
| V2/QCSL25/QC03-Magic_State_Distillation | 13 | 17 | 5 | 0.433 | 0.722 | 0.542 | 0.711 | 0.617 | 29.103 | 0.0171 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*


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
| artemis-HEAD-66c9e6b98d | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 1 | 260 | 230 | 71 | 0.531 | 0.785 | 0.633 | 0.625 | 0.511 | 27.328 | 0.0117 |
| pecv-reference | model=openai:gpt-5-mini, reasoning_effort=medium | 3 | 262 | 197 | 17 | 0.571 | 0.939 | 0.710 | 0.433 | 0.308 | 31.634 | 0 |

## Per Exercise Breakdown

### artemis-HEAD-66c9e6b98d :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 | 16 | 3 | 0.529 | 0.857 | 0.655 | 0.687 | 0.564 | 15.011 | 0.0064 |
| V2/ERA2021/H03-Grafikspeicher | 11 | 11 | 7 | 0.500 | 0.611 | 0.550 | 0.731 | 0.628 | 28.008 | 0.0098 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 16 | 8 | 2 | 0.667 | 0.889 | 0.762 | 0.703 | 0.578 | 23.885 | 0.0262 |
| V2/IOS26/TC1-Bookstore | 19 | 9 | 0 | 0.679 | 1 | 0.809 | 0.745 | 0.648 | 16.805 | 0.0080 |
| V2/IOS26/TC2-Developer | 17 | 13 | 1 | 0.567 | 0.944 | 0.708 | 0.888 | 0.810 | 21.464 | 0.0100 |
| V2/ISE22/H05E01-REST_Architectural_Style | 15 | 11 | 3 | 0.577 | 0.833 | 0.682 | 0.593 | 0.473 | 21.278 | 0.0170 |
| V2/ISE22/H10E01-Containers | 16 | 9 | 2 | 0.640 | 0.889 | 0.744 | 0.675 | 0.561 | 20.081 | 0.0140 |
| V2/ITP2425/H01E01-Lectures | 28 | 18 | 2 | 0.609 | 0.933 | 0.737 | 0.445 | 0.318 | 15.453 | 0.0066 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 26 | 32 | 3 | 0.448 | 0.897 | 0.598 | 0.456 | 0.331 | 22.245 | 0.0105 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 32 | 31 | 2 | 0.508 | 0.941 | 0.660 | 0.443 | 0.308 | 19.585 | 0.0097 |
| V2/ITP2425/SE01E01-UML | 17 | 12 | 1 | 0.586 | 0.944 | 0.723 | 0.625 | 0.490 | 21.689 | 0.0074 |
| V2/MTG26/TA1-SQL_Advanced | 0 | 0 | 18 | 0 | 0 | 0 | — | — | 137.659 | 0 |
| V2/MTG26/TA2-SQL_Basics | 8 | 14 | 10 | 0.364 | 0.444 | 0.400 | 0.796 | 0.712 | 19.439 | 0.0080 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 11 | 13 | 7 | 0.458 | 0.611 | 0.524 | 0.815 | 0.720 | 20.625 | 0.0216 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 13 | 16 | 5 | 0.448 | 0.722 | 0.553 | 0.640 | 0.540 | 21.958 | 0.0199 |
| V2/QCSL25/QC03-Magic_State_Distillation | 13 | 17 | 5 | 0.433 | 0.722 | 0.542 | 0.711 | 0.617 | 29.103 | 0.0171 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*


## Correlation Analysis: Input Tokens vs F1 Score

| Model Name | Correlation | P-Value | N Samples |
| :--- | :--- | :--- | :--- |
| azure-openai-gpt-5-mini |    0.046 |    0.406 | 325 |

*Significance: \*\*\* p<0.001, \*\* p<0.01, \* p<0.05*

## Per-Exercise Correlation Analysis

| Model | Exercise | Correlation | P-Value | N |
| :--- | :--- | :--- | :--- | :--- |
| azure-openai-gpt-5-mini | V2/ERA2021/H00-Hello_World_ASM |   -0.261 |    0.296 | 18 |
| azure-openai-gpt-5-mini | V2/ERA2021/H03-Grafikspeicher |    0.242 |    0.334 | 18 |
| azure-openai-gpt-5-mini | V2/ERA2021/P01-Raycasting_mit_Festkommazahlen |   -0.221 |    0.379 | 18 |
| azure-openai-gpt-5-mini | V2/IOS26/TC1-Bookstore |    0.036 |    0.887 | 18 |
| azure-openai-gpt-5-mini | V2/IOS26/TC2-Developer |    0.126 |    0.619 | 18 |
| azure-openai-gpt-5-mini | V2/ISE22/H05E01-REST_Architectural_Style |   -0.008 |    0.976 | 18 |
| azure-openai-gpt-5-mini | V2/ISE22/H10E01-Containers |    0.337 |    0.171 | 18 |
| azure-openai-gpt-5-mini | V2/ITP2425/H01E01-Lectures |   -0.155 |    0.415 | 30 |
| azure-openai-gpt-5-mini | V2/ITP2425/H02E02-Panic_at_Seal_Saloon |   -0.189 |    0.326 | 29 |
| azure-openai-gpt-5-mini | V2/ITP2425/H05E01-Space_Seal_Farm |   -0.281 |    0.120 | 32 |
| azure-openai-gpt-5-mini | V2/ITP2425/SE01E01-UML |    0.686** |    0.002 | 18 |
| azure-openai-gpt-5-mini | V2/MTG26/TA1-SQL_Advanced | Invalid | N/A | 18 |
| azure-openai-gpt-5-mini | V2/MTG26/TA2-SQL_Basics |    0.012 |    0.964 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks |   -0.077 |    0.762 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC02-Far_Term_Quantum_Algorithms |    0.260 |    0.298 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC03-Magic_State_Distillation |    0.195 |    0.439 | 18 |


## Visualizations

### Model Performance (Tokens vs F1)
![Per Model Analysis](variants_report_plots/per_model.png)

### Detailed Performance by Exercise
![Per Model Per Exercise](variants_report_plots/per_model_per_exercise.png)
