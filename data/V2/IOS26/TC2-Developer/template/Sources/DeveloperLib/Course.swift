import Foundation

/*
 Task 1.1:
 Implement the Course class
*/
public class Course {
    let name: String
    let instructor: String
    var ratings: [Int]

    init(name: String, instructor: String, ratings: [Int]) {
        self.name = ""
        self.instructor = ""
        self.ratings = []
    }
}

/*
 Task 1.2:
 Add method to rate the course
*/
extension Course {
    func addRating(stars: Int) {
        return
    }
}

/*
 Task 1.3:
 Get the average rating of the course
*/
extension Course {
    func getAverageRating() -> Double {
        return 5.0
    }
}
