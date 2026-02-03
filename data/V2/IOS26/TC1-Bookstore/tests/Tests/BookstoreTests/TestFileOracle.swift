struct ClassFile {
    var name: String
    var structs: [String]?
}

/// Defines test structure
let classFileOracle = [
    ClassFile(
        name: "Bookstore",
        structs: ["Book", "Genre"]),
    ClassFile(name: "Client")
]
