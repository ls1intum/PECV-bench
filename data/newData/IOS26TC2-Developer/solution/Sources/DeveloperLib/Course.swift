import Foundation

/*
 Task 1.1:
 Create the Course class
*/

public class Course {
    let name: String
    let instructor: String
    var ratings: [Int]

    init(name: String, instructor: String, ratings: [Int]) {
        self.name = name
        self.instructor = instructor
        self.ratings = ratings
    }
}

/*
 Task 1.2:
 Add method to rate the course
*/
extension Course {
    func addRating(stars: Int) {
        if stars >= 1 && stars <= 5 {
            ratings.append(stars)
        }
    }
}

/*
 Task 1.3:
 Get the average rating of the course
*/
extension Course {
    func getAverageRating() -> Double {
        var starSum = 0
        for rating in ratings {
            starSum += rating
        }
        let totalRatings = ratings.count
        if totalRatings > 0 {
            return Double(starSum) / Double(totalRatings)
        } else {
            return 0.0
        }
    }
}
