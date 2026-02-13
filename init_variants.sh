#!/bin/bash
EXERCISE="V2/ERA2021/P01-Raycasting_mit_Festkommazahlen"

echo "Initializing variants for $EXERCISE..."

# Category 1: METHOD_RETURN_TYPE_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c METHOD_RETURN_TYPE_MISMATCH -d "Change Bitmap24::save return type from void to int." --V2
pecv-bench variants init -e "$EXERCISE" -c METHOD_RETURN_TYPE_MISMATCH -d "Change ray_sphere_intersect return type from bool to int." --V2
pecv-bench variants init -e "$EXERCISE" -c METHOD_RETURN_TYPE_MISMATCH -d "Change fix_fix2float return type from float to double." --V2

# Category 2: METHOD_PARAMETER_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c METHOD_PARAMETER_MISMATCH -d "Swap x and y parameters in Bitmap24::set." --V2
pecv-bench variants init -e "$EXERCISE" -c METHOD_PARAMETER_MISMATCH -d "Remove radius parameter from ray_sphere_intersect." --V2
pecv-bench variants init -e "$EXERCISE" -c METHOD_PARAMETER_MISMATCH -d "Change width/height parameters to long in resize_buffer." --V2

# Category 3: CONSTRUCTOR_PARAMETER_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c CONSTRUCTOR_PARAMETER_MISMATCH -d "Remove default constructor from Bitmap24." --V2
pecv-bench variants init -e "$EXERCISE" -c CONSTRUCTOR_PARAMETER_MISMATCH -d "Add extra color_depth parameter to Bitmap24 constructor." --V2
pecv-bench variants init -e "$EXERCISE" -c CONSTRUCTOR_PARAMETER_MISMATCH -d "Change Bitmap24 constructor parameters from int to long." --V2

# Category 4: ATTRIBUTE_TYPE_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c ATTRIBUTE_TYPE_MISMATCH -d "Change Bitmap24::width from int to short." --V2
pecv-bench variants init -e "$EXERCISE" -c ATTRIBUTE_TYPE_MISMATCH -d "Change Bitmap24::data from char* to int*." --V2
pecv-bench variants init -e "$EXERCISE" -c ATTRIBUTE_TYPE_MISMATCH -d "Change FIX_LEN macro to 4, altering fix_t type definition." --V2

# Category 5: VISIBILITY_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c VISIBILITY_MISMATCH -d "Change default visibility of Bitmap24 members to private." --V2
pecv-bench variants init -e "$EXERCISE" -c VISIBILITY_MISMATCH -d "Make Bitmap24::save method private." --V2
pecv-bench variants init -e "$EXERCISE" -c VISIBILITY_MISMATCH -d "Make Bitmap24::resize_buffer method protected." --V2

# Category 6: IDENTIFIER_NAMING_INCONSISTENCY
pecv-bench variants init -e "$EXERCISE" -c IDENTIFIER_NAMING_INCONSISTENCY -d "Rename class Bitmap24 to Image24." --V2
pecv-bench variants init -e "$EXERCISE" -c IDENTIFIER_NAMING_INCONSISTENCY -d "Rename Bitmap24::save method to write." --V2
pecv-bench variants init -e "$EXERCISE" -c IDENTIFIER_NAMING_INCONSISTENCY -d "Rename ray_sphere_intersect function to check_sphere_hit." --V2