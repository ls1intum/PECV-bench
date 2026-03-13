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
| artemis-feature-hyperion-consistency_check_independent_verification_loop-12d8f2a6bd | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 1 | 254 | 56 | 77 | 0.819 | 0.767 | 0.793 | 0.501 | 0.373 | 44.298 | 0.0180 |
| pecv-reference | model=openai:gpt-5-mini, reasoning_effort=medium | 3 | 262 | 197 | 17 | 0.571 | 0.939 | 0.710 | 0.433 | 0.308 | 31.634 | 0 |

## Per Exercise Breakdown

### artemis-feature-hyperion-consistency_check_independent_verification_loop-12d8f2a6bd :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 18 | 2 | 3 | 0.900 | 0.857 | 0.878 | 0.481 | 0.356 | 38.930 | 0.0101 |
| V2/ERA2021/H03-Grafikspeicher | 9 | 5 | 9 | 0.643 | 0.500 | 0.563 | 0.707 | 0.598 | 59.397 | 0.0151 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 14 | 2 | 4 | 0.875 | 0.778 | 0.824 | 0.480 | 0.357 | 46.191 | 0.0398 |
| V2/IOS26/TC1-Bookstore | 18 | 0 | 1 | 1 | 0.947 | 0.973 | 0.416 | 0.273 | 40.102 | 0.0113 |
| V2/IOS26/TC2-Developer | 15 | 0 | 3 | 1 | 0.833 | 0.909 | 0.520 | 0.369 | 40.316 | 0.0127 |
| V2/ISE22/H05E01-REST_Architectural_Style | 15 | 0 | 3 | 1 | 0.833 | 0.909 | 0.417 | 0.297 | 46.328 | 0.0262 |
| V2/ISE22/H10E01-Containers | 16 | 0 | 2 | 1 | 0.889 | 0.941 | 0.504 | 0.377 | 49.601 | 0.0253 |
| V2/ITP2425/H01E01-Lectures | 29 | 2 | 1 | 0.935 | 0.967 | 0.951 | 0.513 | 0.364 | 37.443 | 0.0113 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 27 | 9 | 2 | 0.750 | 0.931 | 0.831 | 0.484 | 0.352 | 50.185 | 0.0163 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 31 | 0 | 3 | 1 | 0.912 | 0.954 | 0.515 | 0.370 | 45.042 | 0.0150 |
| V2/ITP2425/SE01E01-UML | 18 | 0 | 0 | 1 | 1 | 1 | 0.528 | 0.399 | 40.886 | 0.0125 |
| V2/MTG26/TA1-SQL_Advanced | 1 | 13 | 17 | 0.071 | 0.056 | 0.062 | 0.667 | 0.500 | 37.866 | 0.0112 |
| V2/MTG26/TA2-SQL_Basics | 6 | 12 | 12 | 0.333 | 0.333 | 0.333 | 0.719 | 0.655 | 43.581 | 0.0128 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 12 | 4 | 6 | 0.750 | 0.667 | 0.706 | 0.506 | 0.431 | 43.624 | 0.0290 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 13 | 4 | 5 | 0.765 | 0.722 | 0.743 | 0.465 | 0.349 | 44.868 | 0.0259 |
| V2/QCSL25/QC03-Magic_State_Distillation | 12 | 3 | 6 | 0.800 | 0.667 | 0.727 | 0.442 | 0.349 | 44.808 | 0.0203 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*


## Correlation Analysis: Input Tokens vs F1 Score

| Model Name | Correlation | P-Value | N Samples |
| :--- | :--- | :--- | :--- |
| azure-openai-gpt-5-mini |    0.018 |    0.746 | 325 |

*Significance: \*\*\* p<0.001, \*\* p<0.01, \* p<0.05*

## Per-Exercise Correlation Analysis

| Model | Exercise | Correlation | P-Value | N |
| :--- | :--- | :--- | :--- | :--- |
| azure-openai-gpt-5-mini | V2/ERA2021/H00-Hello_World_ASM |   -0.314 |    0.205 | 18 |
| azure-openai-gpt-5-mini | V2/ERA2021/H03-Grafikspeicher |    0.296 |    0.233 | 18 |
| azure-openai-gpt-5-mini | V2/ERA2021/P01-Raycasting_mit_Festkommazahlen |    0.361 |    0.141 | 18 |
| azure-openai-gpt-5-mini | V2/IOS26/TC1-Bookstore |   -0.215 |    0.392 | 18 |
| azure-openai-gpt-5-mini | V2/IOS26/TC2-Developer |    0.764*** |    0.000 | 18 |
| azure-openai-gpt-5-mini | V2/ISE22/H05E01-REST_Architectural_Style |    0.536* |    0.022 | 18 |
| azure-openai-gpt-5-mini | V2/ISE22/H10E01-Containers |    0.633** |    0.005 | 18 |
| azure-openai-gpt-5-mini | V2/ITP2425/H01E01-Lectures |   -0.073 |    0.702 | 30 |
| azure-openai-gpt-5-mini | V2/ITP2425/H02E02-Panic_at_Seal_Saloon |    0.195 |    0.311 | 29 |
| azure-openai-gpt-5-mini | V2/ITP2425/H05E01-Space_Seal_Farm |    0.260 |    0.150 | 32 |
| azure-openai-gpt-5-mini | V2/ITP2425/SE01E01-UML | Invalid | N/A | 18 |
| azure-openai-gpt-5-mini | V2/MTG26/TA1-SQL_Advanced |    0.335 |    0.174 | 18 |
| azure-openai-gpt-5-mini | V2/MTG26/TA2-SQL_Basics |    0.124 |    0.625 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks |    0.359 |    0.143 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC02-Far_Term_Quantum_Algorithms |    0.246 |    0.325 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC03-Magic_State_Distillation |    0.312 |    0.208 | 18 |


## Visualizations

### Model Performance (Tokens vs F1)
![Per Model Analysis](variants_report_plots/per_model.png)

### Detailed Performance by Exercise
![Per Model Per Exercise](variants_report_plots/per_model_per_exercise.png)
