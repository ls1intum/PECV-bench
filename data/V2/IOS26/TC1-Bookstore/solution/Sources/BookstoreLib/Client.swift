import Foundation

public class Client {
    public static func main() {
        let bookstore = assembleBookstore()
        /*
         Task 2.2:
         Output the Bookstore’s inventory
        */
        for book in bookstore.books {
            print("\(book.title) by \(book.author):")
            
            guard let genres = book.genres else {
                print("🕵️: Not yet categorized")
                continue
            }
            
            for genre in genres {
                print("- \(genre.name)")
                if let subgenre = genre.subgenre {
                    print("-- (\(subgenre))")
                }
            }
        }
    }
    
    /*
     Task 2.1:
     Assemble your Bookstore
    */
    private static func assembleBookstore() -> Bookstore {
        var books: [Book] = []

        let ritaHayworth = Book(title: "Rita Hayworth and Shawshank Redemption",
                                author: "Stephen King",
                                genres: [Genre(name: "Crime Novel", subgenre: nil)])
        books.append(ritaHayworth)

        let zarathustra = Book(title: "Thus Spoke Zarathustra",
                               author: "Friedrich Nietzsche",
                               genres: [Genre(name: "Novel", subgenre: "Philosophical novel")])
        books.append(zarathustra)

        let modernOS = Book(title: "Modern Operating Systems",
                            author: "Andrew Tannenbaum",
                            genres: [
                                Genre(name: "Computers & Internet", subgenre: "Operating Systems"),
                                Genre(name: "Textbook", subgenre: nil)
                            ])
        books.append(modernOS)

        let bruegge = Book(title: "Object-oriented software engineering",
                           author: "Bernd Bruegge",
                           genres: nil)
        books.append(bruegge)

        return Bookstore(books: books)
    }
}
