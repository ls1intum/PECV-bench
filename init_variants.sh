#!/bin/bash
EXERCISE="IOS26/TC2-Developer"

echo "Initializing variants for $EXERCISE..."

# Category 1: METHOD_RETURN_TYPE_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c METHOD_RETURN_TYPE_MISMATCH -d "Course.getAverageRating returns Int instead of Double in the Solution." --V2
pecv-bench variants init -e "$EXERCISE" -c METHOD_RETURN_TYPE_MISMATCH -d "Developer.swiftExperienceDescription returns Void in Template, conflicting with String return type in Problem Statement." --V2
pecv-bench variants init -e "$EXERCISE" -c METHOD_RETURN_TYPE_MISMATCH -d "Problem Statement claims addRating returns a Bool indicating success, but Code returns Void." --V2

# Category 2: METHOD_PARAMETER_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c METHOD_PARAMETER_MISMATCH -d "Course.addRating parameter renamed to 'value' in Solution, conflicting with 'stars' in Problem Statement." --V2
pecv-bench variants init -e "$EXERCISE" -c METHOD_PARAMETER_MISMATCH -d "Problem Statement claims Developer.attend takes a String (courseName), but Code takes a Course object." --V2
pecv-bench variants init -e "$EXERCISE" -c METHOD_PARAMETER_MISMATCH -d "Problem Statement claims addRating takes a Double, but Code expects an Int." --V2

# Category 3: CONSTRUCTOR_PARAMETER_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c CONSTRUCTOR_PARAMETER_MISMATCH -d "Problem Statement snippet swaps the order of 'name' and 'instructor' parameters for Course init." --V2
pecv-bench variants init -e "$EXERCISE" -c CONSTRUCTOR_PARAMETER_MISMATCH -d "Developer initializer in Solution requires non-optional Int for experience, conflicting with optional Int? in requirements." --V2
pecv-bench variants init -e "$EXERCISE" -c CONSTRUCTOR_PARAMETER_MISMATCH -d "Template Course initializer is missing the 'ratings' parameter which is required by the Problem Statement." --V2

# Category 4: ATTRIBUTE_TYPE_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c ATTRIBUTE_TYPE_MISMATCH -d "Course.ratings defined as [Double] in Solution, conflicting with [Int] in Problem Statement." --V2
pecv-bench variants init -e "$EXERCISE" -c ATTRIBUTE_TYPE_MISMATCH -d "Problem Statement defines monthsOfSwiftExperience as String, but Code uses Int?." --V2
pecv-bench variants init -e "$EXERCISE" -c ATTRIBUTE_TYPE_MISMATCH -d "Course.instructor defined as [String] (array) in Solution, conflicting with String in Problem Statement." --V2

# Category 5: VISIBILITY_MISMATCH
pecv-bench variants init -e "$EXERCISE" -c VISIBILITY_MISMATCH -d "Course.ratings is private in Solution, but Problem Statement implies it is accessible." --V2
pecv-bench variants init -e "$EXERCISE" -c VISIBILITY_MISMATCH -d "Developer.attend is private in Solution, making it inaccessible despite Problem Statement requirements." --V2
pecv-bench variants init -e "$EXERCISE" -c VISIBILITY_MISMATCH -d "Problem Statement requires 'public class Course', but Solution defines it as internal (no modifier)." --V2

# Category 6: IDENTIFIER_NAMING_INCONSISTENCY
pecv-bench variants init -e "$EXERCISE" -c IDENTIFIER_NAMING_INCONSISTENCY -d "Problem Statement refers to the class as 'Lecture' instead of 'Course'." --V2
pecv-bench variants init -e "$EXERCISE" -c IDENTIFIER_NAMING_INCONSISTENCY -d "Course.addRating renamed to 'rate' in Solution, conflicting with Problem Statement." --V2
pecv-bench variants init -e "$EXERCISE" -c IDENTIFIER_NAMING_INCONSISTENCY -d "Developer.swiftExperienceDescription renamed to 'getExperienceDescription' in Template." --V2