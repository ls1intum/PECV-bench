package de.tum.cit.ase;
import de.tum.in.test.api.io.IOTester;
import de.tum.in.test.api.jupiter.PublicTest;
import de.tum.in.test.api.util.ReflectionTestUtils;
import org.junit.jupiter.api.DisplayName;
import static de.tum.cit.ase.TestConstants.*;

import java.lang.reflect.Array;
import java.lang.reflect.Method;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

@H02E02
public class SealSaloonTest extends BehaviorTest {

	@PublicTest
	@DisplayName("Calculate Price of Meal")
	void testOrderCheeseMealWithIngredientsInStock() {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		Object[] ingredients = this.initializeIngredients();
		Object[] meals = this.initializeMeals();
		Object stock = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_STOCK_ATTRIBUTE_NAME, sealSaloon, ReflectionTestUtils.getClazz(STOCK_CLASS));

		if (sealSaloon == null) {
			fail("Cannot initialize the SealSaloon class, make sure you implemented it properly");
		}

		if (stock == null) {
			fail("Cannot initialize the Stock class, make sure you implemented it properly");
		}
		ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_EMPTY_METHOD));
		for (int i = 0; i < 6; i++) {
			ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_ADD_METHOD, ReflectionTestUtils.getClazz(STOCK_INGREDIENT_CLASS)), ingredients[i]);
		}
		if ((int) ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_CALCULATE_TOTAL_PRICE_METHOD_NAME, meals[0]) != 15) {
			fail("Your calculateTotalPrice method does not return the correct price for a Meal");
		}
	}

	@PublicTest
	void testAcceptSupplyDelivery() {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		Object[] ingredients = this.initializeIngredients();
		Object stock = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_STOCK_ATTRIBUTE_NAME, sealSaloon, ReflectionTestUtils.getClazz(STOCK_CLASS));

		if (sealSaloon == null) {
			fail("Cannot initialize the SealSaloon class, make sure you implemented it properly");
		}

		if (stock == null) {
			fail("Cannot initialize the Stock class, make sure you implemented it properly");
		}
		for (int i = 0; i < 6; i++) {
			ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_ADD_METHOD, ReflectionTestUtils.getClazz(STOCK_INGREDIENT_CLASS)), ingredients[i]);
		}
		Method accept = ReflectionTestUtils.getMethod(sealSaloon, SEAL_SALOON_ACCEPT_SUPPLY_DELIVERY_METHOD_NAME, String.class, int.class, int.class);
		ReflectionTestUtils.invokeMethod(sealSaloon, accept, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, 3, 2);

		Object[] actualIngredients = (Object[]) ReflectionTestUtils.valueForNonPublicAttribute(stock, STOCK_STOCK_INGREDIENT_ATTRIBUTE);
		int oldSize = actualIngredients.length;
		ReflectionTestUtils.invokeMethod(sealSaloon, accept, "TestItem", 5, 2);

		actualIngredients = (StockIngredient[]) ReflectionTestUtils.valueForNonPublicAttribute(stock, STOCK_STOCK_INGREDIENT_ATTRIBUTE);
		if (actualIngredients.length != oldSize + 1) {
			fail("The stock-size did not increase after calling acceptSupplyDelivery with a new StockIngredient that was not previously in the list");
		}
	}

	@PublicTest
	void testOrderMealWithoutEnoughIngredientsInStock(IOTester ioTester) {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		Object[] meals = this.initializeMeals();
		Object stock = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_STOCK_ATTRIBUTE_NAME, sealSaloon, ReflectionTestUtils.getClazz(STOCK_CLASS));

		if (sealSaloon == null) {
			fail("Cannot initialize the SealSaloon class, make sure you implemented it properly");
		}

		if (stock == null) {
			fail("Cannot initialize the Stock class, make sure you implemented it properly");
		}
		ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_EMPTY_METHOD));
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_ORDER_MEAL_METHOD_NAME, meals[2]);

		List<String> lines = ioTester.out().getLinesAsString();
		if (lines.size() != 0) {
			fail("Did not expect any message to be printed, since there are not enough ingredients in stock, but got " + lines);
		}
	}

	@PublicTest
	void testOrderMealWithEnoughIngredientsInStock(IOTester ioTester) {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		Object[] ingredients = this.initializeIngredients();
		Object[] meals = this.initializeMeals();
		Object stock = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_STOCK_ATTRIBUTE_NAME, sealSaloon, ReflectionTestUtils.getClazz(STOCK_CLASS));

		if (sealSaloon == null) {
			fail("Cannot initialize the SealSaloon class, make sure you implemented it properly");
		}

		if (stock == null) {
			fail("Cannot initialize the Stock class, make sure you implemented it properly");
		}
		for (int i = 0; i < 6; i++) {
			ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_ADD_METHOD, ReflectionTestUtils.getClazz(STOCK_INGREDIENT_CLASS)), ingredients[i]);
		}
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_ORDER_MEAL_METHOD_NAME, meals[2]);

		Integer totalOrdersObj = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_TOTAL_ORDERS_ATTRIBUTE_NAME, sealSaloon, Integer.class);
		if (totalOrdersObj == null) {
			fail("The totalOrders attribute is null, expected a non-null value.");
		}
		int totalOrders = totalOrdersObj;
		if (totalOrders != 1) {
			fail("The totalOrders attribute is not updated properly after ordering a meal");
		}

		List<String> lines = ioTester.out().getLinesAsString();
		if (lines.size() != 1) {
			fail("Expected one message to be printed, but got " + lines);
		}
		if (!lines.get(0).equals("The order is ready: Veggie Meal")) {
			fail("Expected message to be \"The order is ready: Veggie Meal\", but got " + lines.get(0));
		}
	}

	@PublicTest
	void testOrderMealAndThenOrderSecondMeal(IOTester ioTester) {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		Object[] ingredients = this.initializeIngredients();
		Object[] meals = this.initializeMeals();
		Object stock = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_STOCK_ATTRIBUTE_NAME, sealSaloon, ReflectionTestUtils.getClazz(STOCK_CLASS));

		if (sealSaloon == null) {
			fail("Cannot initialize the SealSaloon class, make sure you implemented it properly");
		}

		if (stock == null) {
			fail("Cannot initialize the Stock class, make sure you implemented it properly");
		}
		for (int i = 0; i < 6; i++) {
			ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_ADD_METHOD, ReflectionTestUtils.getClazz(STOCK_INGREDIENT_CLASS)), ingredients[i]);
		}
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_ORDER_MEAL_METHOD_NAME, meals[2]);
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_ORDER_MEAL_METHOD_NAME, meals[0]);

		Integer totalOrdersObj = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_TOTAL_ORDERS_ATTRIBUTE_NAME, sealSaloon, Integer.class);
		if (totalOrdersObj == null) {
			fail("The totalOrders attribute is null, expected a non-null value.");
		}
		int totalOrders = totalOrdersObj;
		if (totalOrders != 2) {
			fail("The totalOrders attribute is not updated properly after ordering two meals");
		}

		List<String> lines = ioTester.out().getLinesAsString();
		if (lines.size() != 2) {
			fail("Expected two messages to be printed, but got " + lines);
		}
		if (!lines.get(0).equals("The order is ready: Veggie Meal")) {
			fail("Expected message to be \"The order is ready: Veggie Meal\", but got " + lines.get(0));
		}
		if (!lines.get(1).equals("The order is ready: Cheese Meal")) {
			fail("Expected message to be \"The order is ready: Cheese Meal\", but got " + lines.get(1));
		}
	}

	@PublicTest
	void testOrderMealWithMissingIngredients(IOTester ioTester) {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		Object[] ingredients = this.initializeIngredientsNotEnough();
		Object[] meals = this.initializeMeals();
		Object stock = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_STOCK_ATTRIBUTE_NAME, sealSaloon, ReflectionTestUtils.getClazz(STOCK_CLASS));
		if (sealSaloon == null) {
			fail("Cannot initialize the SealSaloon class, make sure you implemented it properly");
		}

		if (stock == null) {
			fail("Cannot initialize the Stock class, make sure you implemented it properly");
		}
		ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_EMPTY_METHOD));
		ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_ADD_METHOD, ReflectionTestUtils.getClazz(STOCK_INGREDIENT_CLASS)), ingredients[0]);
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_ORDER_MEAL_METHOD_NAME, meals[0]);

		List<String> lines = ioTester.out().getLinesAsString();
		if (lines.size() > 0) {
			fail("Console should not print anything, since there are missing ingredients");
		}
	}

	@PublicTest
	void testOrderSeveralDifferentTypesOfMeals() {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		Object[] ingredients = this.initializeIngredients();
		Object[] meals = this.initializeMeals();
		Object stock = AttributeHelper.readAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_STOCK_ATTRIBUTE_NAME, sealSaloon, ReflectionTestUtils.getClazz(STOCK_CLASS));

		if (sealSaloon == null) {
			fail("Cannot initialize the SealSaloon class, make sure you implemented it properly");
		}

		if (stock == null) {
			fail("Cannot initialize the Stock class, make sure you implemented it properly");
		}
		for (int i = 0; i < 6; i++) {
			ReflectionTestUtils.invokeMethod(stock, ReflectionTestUtils.getMethod(stock, STOCK_ADD_METHOD, ReflectionTestUtils.getClazz(STOCK_INGREDIENT_CLASS)), ingredients[i]);
		}
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_ORDER_MEAL_METHOD_NAME, meals[0]);
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_ORDER_MEAL_METHOD_NAME, meals[1]);
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_ORDER_MEAL_METHOD_NAME, meals[2]);

		int firstMealPrice = (int) ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_CALCULATE_TOTAL_PRICE_METHOD_NAME, meals[0]);
		int secondMealPrice = (int) ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_CALCULATE_TOTAL_PRICE_METHOD_NAME, meals[1]);
		int thirdMealPrice = (int) ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_CALCULATE_TOTAL_PRICE_METHOD_NAME, meals[2]);

		if (firstMealPrice != 15) {
			fail("Your calculateTotalPrice method does not return the correct price for a Meal");
		}
		if (secondMealPrice != 19) {
			fail("Your calculateTotalPrice method does not return the correct price for a Meal");
		}
		if (thirdMealPrice != 17) {
			fail("Your calculateTotalPrice method does not return the correct price for a Meal");
		}
	}

	@PublicTest
	@DisplayName("Calculate Remaining Order Number with Orders")
	void testCalculateRemainingOrderNumber(IOTester ioTester) {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		Class<?> mealClass = ReflectionTestUtils.getClazz(MEAL_CLASS);
		Object mealArray = Array.newInstance(mealClass, 3);
		Array.set(mealArray, 0, HelperMethods.getInstance(MEAL_CLASS, MEAL_NAME, new String[]{STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1}));
		Array.set(mealArray, 1, HelperMethods.getInstance(MEAL_CLASS, MEAL_NAME, new String[]{STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1}));
		Array.set(mealArray, 2, HelperMethods.getInstance(MEAL_CLASS, MEAL_NAME, new String[]{STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1}));

		AttributeHelper.setAttribute(ReflectionTestUtils.getClazz(SEAL_SALOON_CLASS), SEAL_SALOON_ORDERS_ATTRIBUTE_NAME, sealSaloon, mealArray);
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_CAL_REMAINING_ORDERS_METHOD_NAME);
		List<String> lines = ioTester.out().getLinesAsString();
		if (lines.size() != 4) {
			fail("Expected 4 lines to be printed, but got " + lines.size());
		}
		for (int i = 0; i < 4; i++) {
			if (!lines.get(i).equals("Order number: " + i)) {
				fail("Mismatch at line " + i + ": expected 'Order number: " + i + "' but got '" + lines.get(i) + "'");
			}
		}
	}

	@PublicTest
	@DisplayName("Calculate Remaining Order Number with Empty Orders")
	void testCalculateRemainingOrderNumberEmptyOrders(IOTester ioTester) {
		Object sealSaloon = HelperMethods.getInstance(SEAL_SALOON_CLASS);
		ReflectionTestUtils.invokeMethod(sealSaloon, SEAL_SALOON_CAL_REMAINING_ORDERS_METHOD_NAME);
		List<String> lines = ioTester.out().getLinesAsString();
		if (lines.size() != 1) {
			fail("Expected 1 line to be printed, but got " + lines.size());
		}
		if (!lines.get(0).equals("Order number: 0")) {
			fail("Mismatch: expected 'Order number: 0' but got '" + lines.get(0) + "'");
		}
	}

	Object[] initializeIngredients() {
		return List.of(
				createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, 10, 17),
				createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, 3, 12),
				createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3, 2, 10),
				createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_4, 4, 15),
				createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_5, 1, 5),
				createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_6, 1, 5)).toArray(new Object[0]);
	}

	Object[] initializeMeals() {
		return List.of(
				createInstance(MEAL_CLASS, new Class[]{String.class, String[].class},
						"Cheese Meal", List.of(STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3).toArray(new String[0])),
				createInstance(MEAL_CLASS, new Class[]{String.class, String[].class},
						"Bacon Meal", List.of(STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3,STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_4).toArray(new String[0])),
				createInstance(MEAL_CLASS, new Class[]{String.class, String[].class},
						"Veggie Meal", List.of(STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_5, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_6).toArray(new String[0]))).toArray(new Object[0]);
	}

	Object[] initializeIngredientsNotEnough() {
		return List.of(
				createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, 18, 4)).toArray(new Object[0]);
	}

}
