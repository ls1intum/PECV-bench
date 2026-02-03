package de.tum.cit.ase;


public class Seal extends Animal implements Rideable, Milkable {


	public Seal(String name) {
		super(name);
	}


	@Override
	public String messageOnFeed() {
		return "Arf Arf!";
	}


	@Override
	public String messageOnMilk(double volume) {
		return "Seal " + getName() + " is milked (" + volume + "L)";
	}


	@Override
	public String messageOnRide() {
		return "Riding on Seal " + getName();
	}
}
