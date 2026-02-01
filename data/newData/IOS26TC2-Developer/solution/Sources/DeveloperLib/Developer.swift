import Foundation

/*
 Task 2.1:
 Implement the Developer class
*/

public class Developer {
    let name: String
    var monthsOfSwiftExperience: Int?
    
    init(name: String, monthsOfSwiftExperience: Int?) {
        self.name = name
        self.monthsOfSwiftExperience = monthsOfSwiftExperience
        print(self.swiftExperienceDescription())
    }
}

/*
 Task 2.2:
 Create a Description
*/
extension Developer {
    func swiftExperienceDescription() -> String {
        if let experience = monthsOfSwiftExperience {
            switch experience {
            case 1:
                return "\(name) has just finished the intro course."
            default:
                return "\(name) has \(experience) months of experience in Swift."
            }
        }
        return "\(name) has no experience in Swift yet."
    }
}

/*
 Task 2.3:
 Add a method to attend a course
*/
extension Developer {
    func attend(course: Course?) {
        if let course = course, course.name.lowercased().contains("swift") {
            if let monthsSwiftExperience = monthsOfSwiftExperience {
                self.monthsOfSwiftExperience = monthsSwiftExperience + 1
            } else {
                monthsOfSwiftExperience = 1
            }
            print("\(name) has successfully participated in the course \(course.name) taught by \(course.instructor).")
        }
    }
}
