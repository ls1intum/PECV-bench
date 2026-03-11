import Foundation

/*
 Task 2.1:
 Implement the Developer class
 */

public class Developer {
    let name: String
    var monthsOfSwiftExperience: Int?
    
    init(name: String, monthsOfSwiftExperience: Int?) {
        self.name = ""
        self.monthsOfSwiftExperience = nil
        // TODO: Task 2.2 - Call swiftExperienceDescription()
    }
}

/*
 Task 2.2:
 Create a Description
 */
extension Developer {
    func swiftExperienceDescription() -> String {
        return ""
    }
}

/*
 Task 2.3:
 Add a method to attend a course
 */
extension Developer {
    func attend(course: Course?) {
    }
}
