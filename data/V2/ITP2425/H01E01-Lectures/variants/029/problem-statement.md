# H01E02 - Lectures

In this exercise we will implement a class that represents a lecture.

### Project Structure
In the template repository folder `src/de/tum/cit/ase` you can find a `Lecture` class where you have to add code and a `Main` class where you can test your implementation.

---

### Part 1: Attributes and Constructor

First, we need to add attributes and a constructor to our `Lecture` class.

**You have the following tasks:**

1. [task][Add Attributes to Lecture Class](testAttributes[Lecture])
Take a look at the UML Diagram below and add the corresponding attributes: `lectureName`, `numberOfInscribedStudents`, `numberOfGuestStudents`, `numberOfLecturers` and `numberOfTutors`.

2. [task][Implement a Constructor for Lecture Class](testConstructors[Lecture])
Create a constructor that initializes every attribute of the `Lecture` class. Pay attention to the order of the attributes in the constructor, and make sure it follows the same order from the UML diagram.

---

### Part 2: Methods

Our next step is to implement getters, setters and a few additional methods.

**You have the following tasks:**

1. [task][Implement Getters](getLectureNameTest(),getNumberOfInscribedStudentsTest(),getNumberOfGuestStudentsTest(),getNumberOfLecturersTest(),getNumberOfTutorsTest())
Implement getters for each attribute of the `Lecture` class.

2. [task][Implement Setters](setLectureNameTest(),setNumberOfInscribedStudentsTest(),setNumberOfGuestStudentsTest(),setNumberOfLecturersTest(),setNumberOfTutorsTest())
Implement setters for each attribute of the `Lecture` class.

3. [task][Implement Custom String](toStringTest())
Implement a custom `toString()` method which describes the lecture in detail. It has to make use of every attribute, but feel free to format it as you like.
The `toString()` method can look like this: <code class="string">Lecture{lectureName='Introduction to Programming', numberOfInscribedStudents='600', numberOfGuestStudents='200', numberOfLecturers='14', numberOfTutors='40'}</code>

4. [task][Implement Total Number of Students](getTotalNumberOfStudentsTest())
Implement a `getTotalNumberOfStudents()` method which returns the total number of students. (Tip: Check the expected return type in the UML diagram.)

5. [task][Implement Lecture Name and Total Number of Students](getNameAndTotalNumberOfStudentsTest())
Implement a `getNameAndTotalNumberOfStudents()` method which returns a String of the following format `LectureName (TotalNumberOfStudents)`

6. [task][Implement Number of Students Per Tutor](getNumberOfStudentsPerTutorTest())
Implement a `getNumberOfStudentsPerTutor()` method which returns the number of students per tutor calculated using the total number of students.

7. [task][Implement Add Guest Students](addGuestStudentsTest())
Implement a `addGuestStudents(int)` method which adds a new number of guest students to the lecture.

---

### Part 3: Test your implementation (optional)

In the Main class you can find the main function in which you can test your implementation of the *Lecture* class. Initialize a Lecture by calling the constructor and test your methods.


@startuml
hide circles
hide empty members

class Lecture {
    <color:testsColor(testAttributes[Lecture])>-lectureName: String</color>
    <color:testsColor(testAttributes[Lecture])>-numberOfInscribedStudents: int</color>
    <color:testsColor(testAttributes[Lecture])>-numberOfGuestStudents: int</color>
    <color:testsColor(testAttributes[Lecture])>-numberOfLecturers: int</color>
    <color:testsColor(testAttributes[Lecture])>-numberOfTutors: int</color>
    
      <color:testsColor(getTotalNumberOfStudentsTest())>+getTotalNumberOfStudents(): int</color>
      <color:testsColor(getNameAndTotalNumberOfStudentsTest())>+getNameAndTotalNumberOfStudents(): String</color>
      <color:testsColor(getNumberOfStudentsPerTutorTest())>+getNumberOfStudentsPerTutor(): int</color>
      <color:testsColor(addGuestStudentsTest())>+addGuestStudents(int): void</color>
}

@enduml

<style>
code.string {
    background-color: rgba(var(--bs-body-color-rgb), 0.10);;
    border: 2px;
    border-radius: 3px;
    padding: 2px;
}
</style>