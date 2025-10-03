# H02E02 - Panic at Seal Saloon

Seals have established their delivery business, and it's now time for the seals to scale up to a new Wild West saloon business. They have excellent management and cooking skills and even found a way to serve meals immediately when all the needed ingredients are in stock. Unfortunately, they need your help to make this dream a reality.

Every hour, the Seal Saloon gets a delivery of fresh Ingredients from the city, which are stored in the stock.

### Project Structure

We start with the following classes:

- Meal (Fully implemented, represents a meal with ingredients)
- StockIngredient (An ingredient that can be in the stock)
- Stock (Needs some changes, The stock inventory with ingredients of the Seal Saloon)
- Main (For testing)
- ArrayHelpers (Helper methods to help you modify arrays)

Files to be created:

- SealSaloon (The most important class representing a saloon selling meals having a stock and producing meals)

### Your tasks:
The seals found an external software architect who prepared a class diagram. Implement all classes according to the diagram below. Additionally, add getters for all the private fields. <!-- You can read [this article](https://www.w3schools.com/java/java_encapsulation.asp) to learn more about getters and setters. -->
<br>

@startuml

class SealSaloon {
<color:testsColor(testAttributes[SealSaloon])>-totalOrders: int</color>
<color:testsColor(testMethods[SealSaloon])>+calculateTotalPrice(Meal): int</color>
<color:testsColor(testMethods[SealSaloon])>+acceptSupplyDelivery(String, int, int): void</color>
<color:testsColor(testMethods[SealSaloon])>+orderMeal(Meal): void</color>
<color:testsColor(testMethods[SealSaloon])>+checkOrderReady(): void</color>
<color:testsColor(testMethods[SealSaloon])>+calculateRemainingOrderNumber(): void</color>
}

class Meal {
-name: String
-ingredients: String[]
+Meal(String, String[])
}

class StockIngredient {
-name: String
-price: int
-quantity: int
+StockIngredient(String, int, int)
}

class Stock {
+add(String): int
+take(String): int
+findStockIngredient(String): StockIngredient
+addToStockIngredients(StockIngredient): void
+emptyStock(): void
}

Stock -right-> "*" StockIngredient :stockIngredients
SealSaloon -down-> Stock #testsColor(testAttributes[SealSaloon]);line.bold;text:testsColor(testAttributes[SealSaloon]) : stock
SealSaloon -left-> "*" Meal #testsColor(testAttributes[SealSaloon]);line.bold;text:testsColor(testAttributes[SealSaloon]) : orders

hide empty fields
hide empty methods
hide circle

@enduml

We store all the needed ingredients for a Meal as an array with the names of ingredients. For example, a `Cowboy Stew` might have 2 x `"beans"`, 1 x `"bacon"`, and 2 x `"potatoes"`.

1.  [task][Part 1: SealSaloon](testAcceptSupplyDelivery(),Calculate Price of Meal,testAttributes[SealSaloon],testMethods[SealSaloon])
The SealSaloon needs two attributes: a modifiable `Meal[]` attribute called `orders` and a `final Stock` stock (meaning that it is read-only after construction). These should be initialized to default values (e.g., an empty array or a new object of the class Stock) in the constructor of `SealSaloon`. Hereby, the constructor takes no parameters.

Now, let's implement all the logic of the new Seal Saloon. We will need `calculateTotalPrice` to calculate the net cost of the meal. `acceptSupplyDelivery` is invoked when our supply chain partner delivers fresh Ingredients for our meals. It takes the name, its price, and the delivered quantity as parameters.
It increases the quantity of its corresponding `StockIngredient` object by the given value. Also, handle the case if no ingredient with the given name exists yet: Create a new object and add it to the stock.

Tip: It is recommended to make use of the methods in `ArrayHelpers`.

Note that the following methods and attributes must be **static**:
- `stock` attribute: This is shared across all instances of the SealSaloon.
- `acceptSupplyDelivery` method: This method is related to managing the shared `stock`.
- `calculateTotalPrice` method: This method uses the shared `stock` to calculate the cost of a meal.

The attribute `totalOrders` should **not** be static, as it is meant to track the number of orders placed for each specific saloon instance.

2.  [task][Part 2: SealSaloon](testOrderMealWithoutEnoughIngredientsInStock(IOTester),testOrderMealWithEnoughIngredientsInStock(IOTester),testOrderMealAndThenOrderSecondMeal(IOTester),testOrderMealWithMissingIngredients(IOTester),testOrderSeveralDifferentTypesOfMeals(),Calculate Remaining Order Number with Orders,Calculate Remaining Order Number with Empty Orders)
The `orderMeal` is used when a customer places a new order. Due to the expected high demand, each order can consist of only one meal. Additionally, to avoid unfair waiting times, all customers are served according to **FIFO (First In, First Out)**, i.e., one cannot get their meal if there is a customer in front of them waiting for their order. The `orderMeal` method should add the meal to the array of orders and then adjust the totalOrders attribute accordingly (Decrementing this attribute is not necessary). After that make a call to the `checkOrderReady()` method, where you will implement the following logic: <br>
If all necessary ingredients are in stock, we can instantly cook a Meal and notify the customer that the meal is ready. Write <code class="string">"The order is ready: [Meal name]"</code>
e.g.:
```txt
The order is ready: Cowboy Stew
```
If we successfully cooked a meal, the ingredients are taken from the stock; otherwise, the stock is not changed.

`checkOrderReady()` serves as many meals as possible until either:
 - the order queue is empty or
 - one order cannot be served due to missing ingredients.

In this case, exit the method. When another customer places an order, `checkOrderReady()` gets called again and tries to serve the orders.
Remember to remove successful orders from the queue.

Additionally, implement a method `calculateRemainingOrderNumber()` because seal chefs want to know how long they are going to work. This method should use a **do-while loop** to print the remaining order number. In any case, you should print `Order number: 0`. And after that you should keep printing `Order number: 1`,`Order number: 2` until `Order number: n` where n is the remaining order number.
e.g.:
```txt
Order number: 0
Order number: 1
Order number: 2
Order number: 3
```


You can use the `Main` class to test your implementation, it will not be graded.

<style>
code.string {
    background-color: rgba(var(--bs-body-color-rgb), 0.10);;
    border: 2px;
    border-radius: 3px;
    padding: 2px;
}
</style>