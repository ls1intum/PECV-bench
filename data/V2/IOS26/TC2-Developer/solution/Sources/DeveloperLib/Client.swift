import Foundation

public class Client {
    public static func main() {
        /*
         Task 3.1:
         Test your implementaion
        */
        let swiftCourse = Course(
            name: "Swift Intro Course",
            instructor: "Matthias, Patrick, and Felix",
            ratings: []
        )
        swiftCourse.addRating(stars: 4)
        swiftCourse.addRating(stars: 5)

        let myself = Developer(name: "Your Name", monthsOfSwiftExperience: nil)
        let profKrusche = Developer(name: "Prof. Krusche", monthsOfSwiftExperience: 36)
        myself.attend(course: swiftCourse)
        /*
         Task 3.2:
         Output
        */
        print(swiftCourse.getAverageRating())

        print(myself.swiftExperienceDescription())
        print(profKrusche.swiftExperienceDescription())
    }
}
