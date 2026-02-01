In this challenge you will apply your newly learned Swift concepts 👩💻👨💻👩💻👨💻👩💻👨💻


### Part 1: Course

1. [task][Create the Course class](testInit)
Create a `public class Course` with two `let` properties: `name` of type `String` and `instructor` of type `String` and a `var` called `ratings` that is an array of type `Int`.
When initializing a new `Course` instance, we want to configure all properties using initializer parameters. Hint: Initializing the class should look like this:
```swift
let course = Course(name: "My Course", instructor: "My Instructor", ratings: [])
```

2. [task][Implement the course rating method](testAddRating)
Other students often have trouble finding the right course to attend. Therefore, we introduce a new rating system that allows students to rate a course ranging from 1 (worst) to 5 (best) stars ⭐️.
Implement an instance method `addRating(stars:)` in the class `Course`, which takes one argument stars of type `Int`.
    * Make sure nobody manipulates the rating by entering an invalid amount of stars.
    * If a rating is valid, add it to the `ratings` array of the `Course` class.

    **Note**: We added an `extension` for the `Course` class here. Declare your instance method there. <!-- You will learn what this means in the next Swift session, but for now, imagine you are continuing to write code in your class! -->


3. [task][Calculate the average rating of a course](testGetAverage,testGetAverageOfNoRatings)
Now that we can rate the course, we want to know the average rating a course has to determine the best course to choose.
Implement an instance method `getAverageRating()` in the class `Course` that returns the average rating of type `Double`.

    **Hint:** To calculate the average rating, calculate `Double(sumOfStars) / Double(totalRatings)`. Also, avoid dividing by zero and return a reasonable average rating instead.

### Part 2: Developer

1. [task][Implement the Developer class](testInitDeveloper)
 Create a class `Developer`. The class should have two properties: `name` of type `String` and `monthsOfSwiftExperience` of type `Int?`.
 When initializing a new `Developer` instance, we want to configure all properties using initializer parameters.

2. [task][Create a Description](testNoExperienceDesc,testExperienceCourse,testExperienceMonths)
 Implement an instance method `swiftExperienceDescription()` with return type `String` to generate a printable
 description of the developer's experience:
    * Use optional binding to check if the property is set. If not, return a description saying `"\(name) has no experience in Swift yet."`.
    * If the property has a value, use a `switch` statement to see whether it's equal to 1. If it is, return a description saying `"\(name) has just finished the intro course."`.
    * The default case of the `switch` statement should return a description using the developer's name and their months of Swift experience (e.g. `Max Mustermann has 12 months of experience in Swift.`).
    * Call this method in the initializer you defined before and make sure its result is printed using a `print` statement
 **Note**: We added an `extension` for the `Developer` class here. Declare your instance method there. <!-- You will learn what this means in the next Swift session, but for now just imagine you are continuing to write code in your class! -->

3. [task][Add a method to attend a course](testAttendNil,testAttendCourse,testAttendNonSwiftCourse)
 Implement an instance method `attend(course:)` in the class `Developer` which takes one argument course of type `Course?`.
    * Use optional binding to check if the property is set.
    * If the property has a value, check if the lowercase name of the course contains `"swift"`. If so, increase the `monthsOfSwiftExperience` of the developer by 1 (or set it to 1 if the developer has no previous experience) and print a successful participation message detailing the developer's name, the name of the course and the course's instructor.


### Part 3: Client

1. **Test your implementation**
Create an instance of `Course`, called `swiftCourse`, with the name `"Swift Intro Course"`, the instructor `"Matthias, Patrick, and Felix"` and no previous ratings.
Give the `swiftCourse` a rating of 4⭐️ and a rating of 5⭐️.
Now calculate the average rating and print it to the console using the `getAverageRating()` method.
Instantiate an instance of `Developer`, called `myself`, with your name and no (`nil`) Swift experience.
Instantiate another instance of `Developer`, called `profKrusche`, with the name `"Prof. Krusche"` and 36 months of Swift experience.
Because the rating convinces you, make yourself (the previously created `Developer` instance) attend the `swiftCourse`. After that, print your and Prof. Krusche's Swift experience to the console using the `swiftExperienceDescription()` method.

2. **Output**
Check the console for the output of your print statements and make sure you understand how the code works.