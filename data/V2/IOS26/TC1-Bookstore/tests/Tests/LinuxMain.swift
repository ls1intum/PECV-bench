import XCTest
import SwiftTestReporter
import BookstoreTests

_ = TestObserver()

var tests = [XCTestCaseEntry]()
tests += BookstoreTests.__allTests()

XCTMain(tests)
