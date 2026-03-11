package de.tum.cit.ase;

public class Meal {
	private final String name;
	private final String[] ingredients;

	public Meal(String[] ingredients, String name) {
		this.name = name;
		this.ingredients = ingredients;
	}

	public String getName() {
		return this.name;
	}

	public String[] getIngredients() {
		return this.ingredients;
	}
}
