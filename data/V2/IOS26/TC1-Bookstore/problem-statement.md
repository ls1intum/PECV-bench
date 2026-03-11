### Part 1: Implementing the Bookstore and the necessary structures.

**You have the following tasks:**

In this part, all fields of classes and structs should be `let` constants.

1. [task][Implement Bookstore](testBookstore)
Create a `class Bookstore` that holds an array of `Book`s named `books`.
Also create a `init` method with the following signature:
```swift
init(books: [Book])
```

Create the necessary `struct`s, that will hold all the data to model your `Bookstore`.

2. [task][Implement the structure Book](testStructBook)
A `struct Book` consists of two Strings `title` and `author` as well as an **optional** array of `Genre`s named `genres`.

3. [task][Implement the structure Genre](testStructGenre)
A `struct Genre` consists of a String `name` and an optional String `subgenre`.

**Note: Normally we discourage the use of optional collections (Arrays, Dictionaries, Sets). In this case we want to to use an optional collection to improve your Optionals knowledge.**


### Part 2: Client

We want to test the implemented `Bookstore` and therefore we need a `Client`.

**You have the following tasks:**

1. [task][Assemble your Bookstore](testBookstoreExists,testBookstoreSize)
  Implement `assembleBookstore` which creates a Bookstore fulfilling the following requirements:
    - Your Bookstore must contain at least three books.
    - At least one book must have one Genre defined (Hint: Use inline initialization for the Genres in the corresponding book).
    - At least one book must have more than one Genre defined.
    - At least one book must have no Genre defined at all.
    - For books that are not yet categorized, the genres property should be `nil`.
    - For at least one of the Genre, a subgenre is defined as well.

2. Test your implementation by outputting the Bookstore’s inventory

  Print the Bookstore’s inventory (as created in the last task) in a human readable format to the console. Remember, there can be a variable number of Genres for a book, and Genres might not even be defined. If a Genre is defined, output its name. If a Genre has a subgenre defined, output its name as well in the following form: `- Genre\n-- (Subgenre)`. For books that are not yet categorized, print out a short message.

 Example:

 ```
 Rita Hayworth and Shawshank Redemption by Stephen King:
 - Crime Novel
 Thus Spoke Zarathustra by Friedrich Nietzsche:
 - Novel
 -- (Philosophical novel)
 Modern Operating Systems by Andrew Tannenbaum:
 - Computers & Internet
 -- (Operating Systems)
 - Textbook
 Object-oriented software engineering by Bernd Bruegge:
 🕵: Not yet categorized
```

Note: Do not use any protocols like `CustomStringConvertible` during your output!