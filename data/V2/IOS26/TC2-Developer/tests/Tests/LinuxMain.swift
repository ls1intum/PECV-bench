import XCTest
import SwiftTestReporter
import DeveloperTests

_ = TestObserver()

var tests = [XCTestCaseEntry]()
tests += DeveloperTests.__allTests()

XCTMain(tests)
