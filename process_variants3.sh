#!/bin/bash

EXERCISE="V2/ERA2021/P01-Raycasting_mit_Festkommazahlen"
#pecv-bench variants generate-annotation -e newData/ERA2021-H00-Hello-World-ASM -v 007 --V1

# for i in {1..18}; do
#     # Format number with leading zeros (e.g., 1 -> 001)
#     VAR_ID=$(printf "%03d" $i)
#     echo "------------------------------------------------"
#     echo "Processing Variant $VAR_ID..."
#     # 1. Create the patch (Saves your edits)
#     pecv-bench variants create-patch -e "$EXERCISE" -v "$VAR_ID" --V2
#     #Check if patch creation succeeded
#     if [ $? -eq 0 ]; then
#         # 2. Clean up (Deletes full project files to save space)
#         echo "Cleaning up artifacts..."
#         pecv-bench variants clean -e "$EXERCISE" -v "$VAR_ID" --V2
#     else
#         echo "Error creating patch for $VAR_ID. Skipping clean."
#         exit 1
#     fi
# done
# echo "------------------------------------------------"
# echo "All variants finalized successfully."




for i in {1..18}; do
#for i in 8 9; do
    VAR_ID=$(printf "%03d" $i)

    echo "------------------------------------------------"
    echo "Processing Variant $VAR_ID..."

    #pecv-bench variants clean -e "$EXERCISE" -v "$VAR_ID" --V2
    # materialize the variant (applies the patch to create the variant)
    pecv-bench variants materialize -e "$EXERCISE" -v "$VAR_ID" --V2

    # calls AI to generate ground truth fix annotation
    pecv-bench variants generate-annotation -e "$EXERCISE" -v "$VAR_ID" --V2

#    echo "Cleaning up artifacts..."
done
echo "------------------------------------------------"
echo "All variants materialized and annotated successfully."
