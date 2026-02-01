// swift-tools-version:5.2
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "DeveloperTests",
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        .package(name: "Developer", path: "assignment/"),
        .package(url: "https://github.com/yanagiba/swift-ast.git", from: "0.19.9"),
    ],
    targets: [
        .testTarget(
            name: "DeveloperTests",
            dependencies: [
                .product(name: "DeveloperLib", package: "Developer"),
                .product(name: "SwiftAST+Tooling", package: "swift-ast")
            ]),
    ]
)
