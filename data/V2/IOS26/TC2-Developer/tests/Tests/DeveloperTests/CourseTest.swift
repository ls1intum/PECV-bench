import XCTest
@testable import DeveloperLib

class CourseTest: XCTestCase {
    var topLevelDeclarationTextDescriptionLines: [String] = []
    
    var allTests = [
        ("testInit", testInit),
    ]

    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.
        super.setUp()
        getTopLevelDeclaration()
        print(self.topLevelDeclarationTextDescriptionLines)
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }

    func testInit() {
        let course = Course(name: "iPraktikum", instructor: "Instructor", ratings: [1, 2, 3, 4, 5])
        XCTAssertEqual(course.name, "iPraktikum")
        XCTAssertEqual(course.instructor, "Instructor")
        XCTAssertEqual(course.ratings, [1, 2, 3, 4, 5])
    }

    func testAddRating() {
        let course = Course(name: "iPraktikum", instructor: "Instructor", ratings: [])
        for stars in -10...10 {
            course.addRating(stars: stars)
        }
        XCTAssertEqual(course.ratings, [1, 2, 3, 4, 5])
    }

    func testGetAverageOfNoRatings() {
        let course = Course(name: "iPraktikum", instructor: "Instructor", ratings: [])
        XCTAssertEqual(course.getAverageRating(), 0.0)
    }

    func testGetAverage() {
        let course = Course(name: "iPraktikum", instructor: "Instructor", ratings: [1, 2, 3, 4, 5])
        XCTAssertEqual(course.getAverageRating(), 3.0)
    }

    private func getTopLevelDeclaration() {
        guard let topLevelDecl = getTopLevelDeclarationFor("Course") else {
            XCTFail("Course.swift is not implemented!")
            return
        }
        self.topLevelDeclarationTextDescriptionLines = topLevelDecl.textDescription.components(separatedBy: "\n")
    }
}
