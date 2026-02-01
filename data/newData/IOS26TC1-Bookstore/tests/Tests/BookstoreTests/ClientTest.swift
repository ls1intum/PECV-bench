import XCTest

class ClientTest: XCTestCase {
    var topLevelDeclarationTextDescription: String = ""
    
    static var allTests = [
        ("testBookstoreExists", testBookstoreExists),
        ("testBookstoreSize", testBookstoreSize),
    ]
    
    override func setUp() {
        super.setUp()
        continueAfterFailure = false
        getTopLevelDeclaration()
    }
    
    func testBookstoreExists() {
        if !topLevelDeclarationTextDescription.contains("Bookstore(") {
            XCTFail("You do not have a bookstore!")
        }
    }
    
    func testBookstoreSize() {
        if (topLevelDeclarationTextDescription.components(separatedBy: "Book(").count - 1) < 3 {
            XCTFail("The bookstore was not assembled correctly! You need at least 3 books!")
        }
    }
    
    private func getTopLevelDeclaration() {
        guard let topLevelDecl = getTopLevelDeclarationFor("Client") else {
            XCTFail("Client.swift is not implemented!")
            return
        }
        self.topLevelDeclarationTextDescription = topLevelDecl.textDescription
    }
}
