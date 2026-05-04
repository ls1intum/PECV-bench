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
| artemis-feature-hyperion-unified-consistency-check-32471b9a64 | model=azure-openai-gpt-5-mini, reasoning_effort=medium | 1 | 250 | 76 | 81 | 0.767 | 0.755 | 0.761 | 0.604 | 0.491 | 67.421 | 0.0071 |
| pecv-reference | model=openai:gpt-5-mini, reasoning_effort=medium | 1 | 267 | 207 | 64 | 0.563 | 0.807 | 0.663 | 0.630 | 0.519 | 36.701 | 0 |

## Per Exercise Breakdown

### artemis-feature-hyperion-unified-consistency-check-32471b9a64 :: model=azure-openai-gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost (€) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2/ERA2021/H00-Hello_World_ASM | 16 | 2 | 5 | 0.889 | 0.762 | 0.821 | 0.690 | 0.577 | 49.248 | 0.0038 |
| V2/ERA2021/H03-Grafikspeicher | 5 | 9 | 13 | 0.357 | 0.278 | 0.313 | 0.847 | 0.755 | 107.149 | 0.0074 |
| V2/ERA2021/P01-Raycasting_mit_Festkommazahlen | 16 | 1 | 2 | 0.941 | 0.889 | 0.914 | 0.652 | 0.528 | 72.867 | 0.0142 |
| V2/IOS26/TC1-Bookstore | 18 | 0 | 1 | 1 | 0.947 | 0.973 | 0.698 | 0.601 | 41.356 | 0.0041 |
| V2/IOS26/TC2-Developer | 18 | 1 | 0 | 0.947 | 1 | 0.973 | 0.812 | 0.714 | 65.709 | 0.0055 |
| V2/ISE22/H05E01-REST_Architectural_Style | 15 | 0 | 3 | 1 | 0.833 | 0.909 | 0.631 | 0.515 | 69.024 | 0.0095 |
| V2/ISE22/H10E01-Containers | 16 | 2 | 2 | 0.889 | 0.889 | 0.889 | 0.605 | 0.482 | 57.168 | 0.0090 |
| V2/ITP2425/H01E01-Lectures | 29 | 3 | 1 | 0.906 | 0.967 | 0.935 | 0.472 | 0.349 | 47.962 | 0.0044 |
| V2/ITP2425/H02E02-Panic_at_Seal_Saloon | 28 | 7 | 1 | 0.800 | 0.966 | 0.875 | 0.435 | 0.322 | 72.100 | 0.0065 |
| V2/ITP2425/H05E01-Space_Seal_Farm | 33 | 6 | 1 | 0.846 | 0.971 | 0.904 | 0.407 | 0.280 | 50.409 | 0.0056 |
| V2/ITP2425/SE01E01-UML | 18 | 0 | 0 | 1 | 1 | 1 | 0.661 | 0.535 | 56.115 | 0.0052 |
| V2/MTG26/TA1-SQL_Advanced | 1 | 14 | 17 | 0.067 | 0.056 | 0.061 | 0.769 | 0.625 | 64.427 | 0.0050 |
| V2/MTG26/TA2-SQL_Basics | 3 | 15 | 15 | 0.167 | 0.167 | 0.167 | 0.692 | 0.625 | 87.129 | 0.0056 |
| V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks | 11 | 5 | 7 | 0.688 | 0.611 | 0.647 | 0.687 | 0.603 | 91.513 | 0.0111 |
| V2/QCSL25/QC02-Far_Term_Quantum_Algorithms | 14 | 3 | 4 | 0.824 | 0.778 | 0.800 | 0.747 | 0.624 | 77.991 | 0.0102 |
| V2/QCSL25/QC03-Magic_State_Distillation | 9 | 8 | 9 | 0.529 | 0.500 | 0.514 | 0.779 | 0.695 | 91.910 | 0.0096 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*


## Correlation Analysis: Input Tokens vs F1 Score

| Model Name | Correlation | P-Value | N Samples |
| :--- | :--- | :--- | :--- |
| azure-openai-gpt-5-mini |    0.074 |    0.181 | 325 |

*Significance: \*\*\* p<0.001, \*\* p<0.01, \* p<0.05*

## Per-Exercise Correlation Analysis

| Model | Exercise | Correlation | P-Value | N |
| :--- | :--- | :--- | :--- | :--- |
| azure-openai-gpt-5-mini | V2/ERA2021/H00-Hello_World_ASM |    0.040 |    0.875 | 18 |
| azure-openai-gpt-5-mini | V2/ERA2021/H03-Grafikspeicher |    0.102 |    0.688 | 18 |
| azure-openai-gpt-5-mini | V2/ERA2021/P01-Raycasting_mit_Festkommazahlen |   -0.028 |    0.911 | 18 |
| azure-openai-gpt-5-mini | V2/IOS26/TC1-Bookstore |   -0.293 |    0.238 | 18 |
| azure-openai-gpt-5-mini | V2/IOS26/TC2-Developer |   -0.007 |    0.978 | 18 |
| azure-openai-gpt-5-mini | V2/ISE22/H05E01-REST_Architectural_Style |   -0.067 |    0.790 | 18 |
| azure-openai-gpt-5-mini | V2/ISE22/H10E01-Containers |    0.345 |    0.161 | 18 |
| azure-openai-gpt-5-mini | V2/ITP2425/H01E01-Lectures |   -0.055 |    0.774 | 30 |
| azure-openai-gpt-5-mini | V2/ITP2425/H02E02-Panic_at_Seal_Saloon |   -0.032 |    0.869 | 29 |
| azure-openai-gpt-5-mini | V2/ITP2425/H05E01-Space_Seal_Farm |   -0.290 |    0.107 | 32 |
| azure-openai-gpt-5-mini | V2/ITP2425/SE01E01-UML | Invalid | N/A | 18 |
| azure-openai-gpt-5-mini | V2/MTG26/TA1-SQL_Advanced |    0.194 |    0.441 | 18 |
| azure-openai-gpt-5-mini | V2/MTG26/TA2-SQL_Basics |    0.321 |    0.193 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC01-Decision_Diagrams_and_Tensor_Networks |   -0.151 |    0.551 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC02-Far_Term_Quantum_Algorithms |    0.144 |    0.569 | 18 |
| azure-openai-gpt-5-mini | V2/QCSL25/QC03-Magic_State_Distillation |   -0.200 |    0.427 | 18 |


## Visualizations

### Model Performance (Tokens vs F1)
![Per Model Analysis](variants_report_plots/per_model.png)

### Detailed Performance by Exercise
![Per Model Per Exercise](variants_report_plots/per_model_per_exercise.png)
