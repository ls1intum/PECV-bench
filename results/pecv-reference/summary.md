## Dataset Summary

- Total annotated variants: 91
- Total gold issues: 93

| Exercise | Variants |
| --- | --- |
| ITP2425/H01E01-Lectures | 30 |
| ITP2425/H02E02-Panic_at_Seal_Saloon | 29 |
| ITP2425/H05E01-Space_Seal_Farm | 32 |

| Issue Category | Count |
| --- | --- |
| ATTRIBUTE_TYPE_MISMATCH | 17 |
| CONSTRUCTOR_PARAMETER_MISMATCH | 10 |
| IDENTIFIER_NAMING_INCONSISTENCY | 23 |
| METHOD_PARAMETER_MISMATCH | 12 |
| METHOD_RETURN_TYPE_MISMATCH | 19 |
| VISIBILITY_MISMATCH | 12 |

| Artifact Type | Count |
| --- | --- |
| PROBLEM_STATEMENT | 89 |
| SOLUTION_REPOSITORY | 90 |
| TEMPLATE_REPOSITORY | 40 |

## Aggregate Results
| Benchmark | Config Key | N runs | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pecv-reference | model=openai:gpt-5-mini, reasoning_effort=medium | 3 | 262 | 197 | 17 | 0.571 | 0.939 | 0.710 | 0.433 | 0.308 | 31.634 | — |
| pecv-reference | model=openai:o4-mini, reasoning_effort=medium | 3 | 254 | 148 | 25 | 0.632 | 0.910 | 0.746 | 0.676 | 0.565 | 32.958 | 0.0338 |
| pecv-reference | model=openrouter:google/gemini-2.5-flash, reasoning_effort=medium | 3 | 263 | 623 | 15 | 0.297 | 0.946 | 0.452 | 0.597 | 0.474 | 26.380 | 0.0244 |
| pecv-reference | model=openrouter:google/gemini-2.5-flash-lite-preview-06-17, reasoning_effort=medium | 3 | 216 | 288 | 21 | 0.429 | 0.911 | 0.583 | 0.594 | 0.485 | 16.975 | 0.0063 |
| pecv-reference | model=openrouter:x-ai/grok-3-mini, reasoning_effort=medium | 3 | 233 | 222 | 46 | 0.512 | 0.835 | 0.635 | 0.640 | 0.534 | 14.306 | 0.0061 |

## Per Exercise Breakdown

### pecv-reference :: model=openai:gpt-5-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITP2425/H01E01-Lectures | 82 | 44 | 8 | 0.651 | 0.911 | 0.759 | 0.487 | 0.357 | 23.466 | — |
| ITP2425/H02E02-Panic_at_Seal_Saloon | 82 | 82 | 5 | 0.500 | 0.943 | 0.653 | 0.413 | 0.299 | 35.530 | — |
| ITP2425/H05E01-Space_Seal_Farm | 98 | 71 | 4 | 0.580 | 0.961 | 0.723 | 0.405 | 0.274 | 35.761 | — |

### pecv-reference :: model=openai:o4-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITP2425/H01E01-Lectures | 80 | 32 | 10 | 0.714 | 0.889 | 0.792 | 0.706 | 0.589 | 27.805 | 0.0251 |
| ITP2425/H02E02-Panic_at_Seal_Saloon | 80 | 46 | 7 | 0.635 | 0.920 | 0.751 | 0.665 | 0.574 | 32.698 | 0.0398 |
| ITP2425/H05E01-Space_Seal_Farm | 94 | 70 | 8 | 0.573 | 0.922 | 0.707 | 0.659 | 0.538 | 38.024 | 0.0367 |

### pecv-reference :: model=openrouter:google/gemini-2.5-flash, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITP2425/H01E01-Lectures | 87 | 123 | 3 | 0.414 | 0.967 | 0.580 | 0.655 | 0.527 | 20.256 | 0.0176 |
| ITP2425/H02E02-Panic_at_Seal_Saloon | 86 | 104 | 0 | 0.453 | 1 | 0.623 | 0.578 | 0.467 | 25.327 | 0.0260 |
| ITP2425/H05E01-Space_Seal_Farm | 90 | 396 | 12 | 0.185 | 0.882 | 0.306 | 0.558 | 0.429 | 33.066 | 0.0293 |

### pecv-reference :: model=openrouter:google/gemini-2.5-flash-lite-preview-06-17, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITP2425/H01E01-Lectures | 72 | 81 | 6 | 0.471 | 0.923 | 0.623 | 0.604 | 0.467 | 15.180 | 0.0049 |
| ITP2425/H02E02-Panic_at_Seal_Saloon | 66 | 54 | 6 | 0.550 | 0.917 | 0.687 | 0.692 | 0.604 | 18.681 | 0.0077 |
| ITP2425/H05E01-Space_Seal_Farm | 78 | 153 | 9 | 0.338 | 0.897 | 0.491 | 0.502 | 0.402 | 17.187 | 0.0065 |

### pecv-reference :: model=openrouter:x-ai/grok-3-mini, reasoning_effort=medium
| Exercise | TP | FP | FN | Precision | Recall | F1 | Span F1 | IoU | Avg Time (s) | Avg Cost ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITP2425/H01E01-Lectures | 78 | 38 | 12 | 0.672 | 0.867 | 0.757 | 0.629 | 0.504 | 11.940 | 0.0047 |
| ITP2425/H02E02-Panic_at_Seal_Saloon | 71 | 58 | 16 | 0.550 | 0.816 | 0.657 | 0.629 | 0.542 | 17.109 | 0.0074 |
| ITP2425/H05E01-Space_Seal_Farm | 84 | 126 | 18 | 0.400 | 0.824 | 0.538 | 0.659 | 0.555 | 13.983 | 0.0062 |

*Benchmark results are provided under CC-BY-4.0; please attribute PECV Bench when reusing.*
