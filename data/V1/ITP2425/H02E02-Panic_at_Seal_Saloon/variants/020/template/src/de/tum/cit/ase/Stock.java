package de.tum.cit.ase;

public class Stock {
	private StockIngredient[] stockIngredients;

	public Stock() {
		this.stockIngredients = new StockIngredient[0];
	}

	public void setStockIngredients(StockIngredient[] stockIngredients) {
		this.stockIngredients = stockIngredients;
	}

	public StockIngredient[] getStockIngredients() {
		return this.stockIngredients;
	}

	public void addToStockIngredients(StockIngredient ingredient) {
		this.stockIngredients = ArrayHelpers.addElementToArray(this.stockIngredients, ingredient);
	}

	public StockIngredient findStockIngredient(String name) {
		for (var x : this.stockIngredients) {
			if (x.getName().equals(name)) {
				return x;
			}
		}

		return null;
	}

	public int add(String ingredient) {
		StockIngredient stockIngredient = this.findStockIngredient(ingredient);

		if (stockIngredient != null) {
			stockIngredient.setQuantity(stockIngredient.getQuantity() + 1);
			return stockIngredient.getQuantity();
		}

		return -1;
	}

	public int take(String ingredient) {
		StockIngredient stockIngredient = this.findStockIngredient(ingredient);

		if (stockIngredient != null) {
			var stockQuant = stockIngredient.getQuantity();
			if (stockQuant < 1) {
				return -1;
			}

			stockIngredient.setQuantity(stockQuant - 1);
			return stockIngredient.getQuantity();
		}

		return -1;
	}

	public void emptyStock() {
		this.stockIngredients = new StockIngredient[0];
	}
}