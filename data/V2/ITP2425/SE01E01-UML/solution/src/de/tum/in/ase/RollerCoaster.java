package de.tum.in.ase;

public abstract class RollerCoaster extends Ride {

	private int numberOfLoopings;

	public RollerCoaster(String name, char abbreviation, int numberOfLoopings) {
		super(name, abbreviation);
		this.numberOfLoopings = numberOfLoopings;
	}

	public int getNumberOfLoopings() {
		return numberOfLoopings;
	}

}