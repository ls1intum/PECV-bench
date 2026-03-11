import Foundation

/*
 Task 1.1:
 Implement Bookstore
*/

/// A `Bookstore` that stores a large collection of books
class Bookstore {
    /// The books stored in the `Bookstore`
    let books: [Book]
    
    /// - Parameter books: The books stored in the `Bookstore`
    init(books: [Book]) {
        self.books = books
    }
}

/*
 Task 1.2:
 Implement the structure Book
*/
/// A Book that can be stored in the `Bookstore`
struct Book {
    /// The title of a `Book`
    let title: String
    /// The author of a `Book`
    let author: String
    /// A possible list of `Genres`
    ///
    /// For books that are not yet categorized `genres` should be nil
    let genres: [Genre]?
}

/*
 Task 1.3:
 Implement the structure Genre
*/
/// The genre of a `Book`
struct Genre {
    /// The name of the `Genre`
    let name: String
    /// A possible subgenre of the `Genre`
    let subgenre: String?
}
