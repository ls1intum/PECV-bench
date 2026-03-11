import XCTest
@testable import BookstoreLib

class BookstoreTest: XCTestCase {
    var topLevelDeclarationTextDescription: String = ""
    var valids: (bookstoreValid: Bool, bookValid: Bool, genreValid: Bool) = (false, false, false)
    
    static var allTests = [
        ("testStructBook", testStructBook),
        ("testStructGenre", testStructGenre),
        ("testBookstore", testBookstore),
    ]
    
    override func setUp() {
        super.setUp()
        continueAfterFailure = false
        getTopLevelDeclaration()
        valids = checkValidity()
    }
    
    func testBookstore() {
        if !valids.bookstoreValid {
            XCTFail("The class `Bookstore` is not implemented correctly!")
        }
    }
    
    func testStructBook() {
        if !valids.bookValid {
            XCTFail("Struct 'Book' of Bookstore.swift is not implemented correctly!")
        }
    }
    
    func testStructGenre() {
        if !valids.genreValid {
            XCTFail("Struct 'Genre' of Bookstore.swift is not implemented correctly!")
        }
    }
    
    private func getTopLevelDeclaration() {
        guard let topLevelDecl = getTopLevelDeclarationFor("Bookstore") else {
            XCTFail("Bookstore.swift is not implemented!")
            return
        }
        self.topLevelDeclarationTextDescription = topLevelDecl.textDescription
    }
    
    private func checkValidity() -> (Bool, Bool, Bool) {
        let st: [String] = topLevelDeclarationTextDescription.components(separatedBy: "struct")
        var bookstoreValid  = false
        var bookValid = false
        var genreValid = false
        
        for s in st {
            if s.contains("Bookstore") {
                if ((s.contains("var books: Array<Book>") || s.contains("let books: Array<Book>") || s.contains("var books: [Book]") || s.contains("let books: [Book]")) && (s.contains("init(books: Array<Book>) {\nself.books = books\n}"))) {
                    bookstoreValid = true
                }
            }
            if s.contains("Book {") {
                if (s.contains("let title: String") && s.contains("let author: String") && (s.contains("let genres: Optional<Array<Genre>>")) || s.contains("let genres: [Genre]?")) || s.contains("var title: String") && s.contains("var author: String") && (s.contains("var genres: Optional<Array<Genre>>") || s.contains("var genres: [Genre]?")) {
                    bookValid = true
                }
            }
            if s.contains("Genre {") {
                if (s.contains("let name: String") && s.contains("let subgenre: Optional<String>")) || (s.contains("var name: String") && s.contains("var subgenre: Optional<String>")) {
                    genreValid = true
                }
            }
        }

        return (bookstoreValid, bookValid, genreValid)
    }
}
