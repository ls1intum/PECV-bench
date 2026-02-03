package de.tum.cit.ase;

public class SealSaloon {
	private Meal[] orders;
	private static final Stock stock = new Stock();
	private int totalOrders = 0;

	public SealSaloon() {
		this.orders = new Meal[]{};
	}

	public void orderMeal(Meal meal) {
		if (meal != null) {
			this.orders = ArrayHelpers.addElementToArray(this.orders, meal);
			totalOrders++;
			this.checkOrderReady();
		}
	}

	public void checkOrderReady() {
		while (this.orders.length > 0) {
			Meal meal = this.orders[0];
			String[] consumedIngredient = new String[0];

			boolean flag = true;

			for (var x : meal.getIngredients()) {
				if (stock.take(x) == -1) {
					flag = false;
					break;
				}
				consumedIngredient = ArrayHelpers.addElementToArray(consumedIngredient, x);
			}

			if (flag) {
				System.out.println("The order is ready: " + meal.getName());
				this.orders = ArrayHelpers.removeFirstElementFromArray(this.orders);
			} else {
				for (var x : consumedIngredient) {
					stock.add(x);
				}
				return;
			}
		}
	}

	public static void acceptSupplyDelivery(String name, int price, int quantity) {
		StockIngredient existing = stock.findStockIngredient(name);

		if (existing == null) {
			stock.addToStockIngredients(new StockIngredient(name, price, quantity));
		} else {
			existing.setQuantity(existing.getQuantity() + quantity);
		}
	}

	public static int calculateTotalPrice(Meal meal) {
		int sum = 0;

		for (var x : meal.getIngredients()) {
			StockIngredient ingredient = stock.findStockIngredient(x);

			if (ingredient != null) {
				sum += ingredient.getPrice();
			}
		}
		return sum;
	}

	public void calculateRemainingOrderNumber() {
        int remainingOrders = this.orders.length + 1;
        int number = 0;
        do {
			System.out.println("Order number: " + (number++));
		} while (number < remainingOrders);
	}

	public Meal[] getOrders() {
		return orders;
	}

	public static Stock getStock() {
		return stock;
	}

	public int getTotalOrders() {
		return totalOrders;
	}
}