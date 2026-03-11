package de.tum.cit.ase;

import de.tum.in.test.api.util.ReflectionTestUtils;

import java.lang.reflect.Constructor;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import static de.tum.cit.ase.TestConstants.*;
import static org.junit.jupiter.api.Assertions.fail;

@H02E02
public abstract class BehaviorTest {
	/*
	protected StockIngredient[] initializeIngredients() {
		Object stockIngredient = createInstance(STOCK_INGREDIENT_CLASS,
				new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, 10, 17);
		if (stockIngredient == null) {
			return null;
		}
		return List.of(
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, 10, 17),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, 3, 12),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3, 2, 10),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_4, 4, 15),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_5, 1, 5),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_6, 1, 5)).toArray(new StockIngredient[0]);
	}

	protected Meal[] initializeMeals() {
		Object meal = createInstance(MEAL_CLASS, new Class[]{String.class, String[].class},
				"Cheese Meal", List.of(STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3).toArray(new String[0]));
		if (meal == null) {
			return null;
		}
		return List.of(
				(Meal) createInstance(MEAL_CLASS, new Class[]{String.class, String[].class},
						"Cheese Meal", List.of(STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3).toArray(new String[0])),
				(Meal) createInstance(MEAL_CLASS, new Class[]{String.class, String[].class},
						"Bacon Meal", List.of(STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3,STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_4).toArray(new String[0])),
				(Meal) createInstance(MEAL_CLASS, new Class[]{String.class, String[].class},
						"Veggie Meal", List.of(STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_5, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_6).toArray(new String[0]))).toArray(new Meal[0]);
	}

	protected StockIngredient[] initializeIngredients2() {
		Object ingredient = createInstance(STOCK_INGREDIENT_CLASS,
				new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, 10, 17);

		if (ingredient == null) {
			return null;
		}

		return List.of((StockIngredient)
						createInstance(STOCK_INGREDIENT_CLASS,
								new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, 18, 4),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, 9, 4),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3, 8, 6),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_4, 10, 6),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_5, 8, 2),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_6, 7, 3)).toArray(new StockIngredient[0]);
	}

	protected StockIngredient[] initializeIngredientsNotEnough() {
		Object ingredient = createInstance(STOCK_INGREDIENT_CLASS,
				new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, 10, 17);

		if (ingredient == null) {
			return null;
		}

		return List.of((StockIngredient)
						createInstance(STOCK_INGREDIENT_CLASS,
								new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_1, 18, 4),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_2, 9, 4),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_3, 8, 6),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_4, 10, 6),
				(StockIngredient) createInstance(STOCK_INGREDIENT_CLASS,
						new Class[]{String.class, int.class, int.class}, STOCK_INGREDIENT_NAME_ATTRIBUTE_EXAMPLE_5, 8, 2)).toArray(new StockIngredient[0]);
	}

	 */

	/**
	 * Helper method to find desired constructor.
	 *
	 * @param className  - Name of the class, including package.
	 * @param parameters - List of types taken by constructor.
	 * @return Constructor object with desired parameters, if nothing found returns
	 * null.
	 */
	protected Constructor<?> getConstructor(String className, Class<?>[] parameters) {
		try {
			List<Constructor<?>> constructorsList = Arrays
					.stream(ReflectionTestUtils.getClazz(className).getConstructors())
					.filter(constructor -> Arrays.equals(constructor.getParameterTypes(), parameters))
					.toList();
			if (constructorsList.isEmpty()) {
				return null;
			} else if (constructorsList.size() >= 2) {
				return null;
			} else {
				return constructorsList.get(0);
			}
		} catch (Exception e) {
			return null;
		}
	}

	/**
	 * Creates new instance of requested class with specific constructor.
	 *
	 * @param className       - Name of the class, including package.
	 * @param parameters      - List of types taken by constructor.
	 * @param constructorArgs -Parameter instances of the constructor of the class,
	 *                        that it should use to get instantiated with.
	 * @return New instance of class, if specified constructor was not found returns
	 * null.
	 */
	protected Object createInstance(String className, Class<?>[] parameters, Object... constructorArgs) {
		Constructor<?> constructor = getConstructor(className, parameters);
		if (constructor == null) {
			return null;
		}
		return ReflectionTestUtils.newInstance(constructor, constructorArgs);
	}
}
