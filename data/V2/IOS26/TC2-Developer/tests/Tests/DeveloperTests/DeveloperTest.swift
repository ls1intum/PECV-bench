import XCTest
@testable import DeveloperLib

class DeveloperTest: XCTestCase {
    var topLevelDeclarationTextDescriptionBlocks: [[String]] = []
    
    var allTests = [
        ("testInitDeveloper", testInitDeveloper),
        ("testNoExperienceDesc", testNoExperienceDesc),
        ("testExperienceCourse", testExperienceCourse),
        ("testExperienceMonths", testExperienceMonths),
        ("testAttendNil", testAttendNil),
        ("testAttendCourse", testAttendCourse),
        ("testAttendNonSwiftCourse", testAttendNonSwiftCourse),
    ]

    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.
        super.setUp()
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }
    
    func testInitDeveloper() {
        let developer = Developer(name: "Name", monthsOfSwiftExperience: nil)
        XCTAssertEqual(developer.name, "Name")
        XCTAssertNil(developer.monthsOfSwiftExperience)
        
        let developer2 = Developer(name: "Name2", monthsOfSwiftExperience: 1)
        XCTAssertEqual(developer2.name, "Name2")
        XCTAssertEqual(developer2.monthsOfSwiftExperience, 1)
    }
    
    func testNoExperienceDesc() {
        let developer = Developer(name: "Max Mustermann", monthsOfSwiftExperience: nil)
        XCTAssertEqual(developer.swiftExperienceDescription(), "Max Mustermann has no experience in Swift yet.")
    }

    func testExperienceCourse() {
        let developer = Developer(name: "Max Mustermann", monthsOfSwiftExperience: 1)
        XCTAssertEqual(developer.swiftExperienceDescription(), "Max Mustermann has just finished the intro course.")
    }

    func testExperienceMonths() {
        let developer = Developer(name: "Max Mustermann", monthsOfSwiftExperience: 12)
        XCTAssertEqual(developer.swiftExperienceDescription(), "Max Mustermann has 12 months of experience in Swift.")
    }
    
    func testAttendNil() {
        let developer = Developer(name: "Max Mustermann", monthsOfSwiftExperience: nil)
        developer.attend(course: Course(name: "swift 123", instructor: "Instructor", ratings: []))
        XCTAssertEqual(developer.monthsOfSwiftExperience, 1)
    }

    func testAttendCourse() {
        let developer = Developer(name: "Max Mustermann", monthsOfSwiftExperience: 12)
        developer.attend(course: Course(name: "swift 123", instructor: "Instructor", ratings: []))
        XCTAssertEqual(developer.monthsOfSwiftExperience, 13)
    }

    func testAttendNonSwiftCourse() {
        let developer = Developer(name: "Max Mustermann", monthsOfSwiftExperience: 12)
        developer.attend(course: Course(name: "java 123", instructor: "Instructor", ratings: []))
        XCTAssertEqual(developer.monthsOfSwiftExperience, 12)
    }
}
