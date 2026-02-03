package de.tum.cit.ase;

public class Goat extends Animal implements Milkable {

	public Goat(String name) {
		super(name);
	}

	@Override
	public String messageOnFeed() {
		return "Maah!";
	}

	@Override
	public String messageOnMilk(double volume) {
		return "Goat " + getName() + " is milked (" + volume + "L)";
	}
}
