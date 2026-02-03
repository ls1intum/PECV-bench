// swift-tools-version:5.2
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "BookstoreTests",
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        .package(name: "Bookstore", path: "assignment/"),
        .package(url: "https://github.com/yanagiba/swift-ast.git", from: "0.19.9"),
    ],
    targets: [
        // Targets are the basic building blocks of a package. A target can define a module or a test suite.
        // Targets can depend on other targets in this package, and on products in packages which this package depends on.
        .testTarget(
            name: "BookstoreTests",
            dependencies: [
                .product(name: "BookstoreLib", package: "Bookstore"),
                .product(name: "SwiftAST+Tooling", package: "swift-ast")
            ]),
    ]
)
