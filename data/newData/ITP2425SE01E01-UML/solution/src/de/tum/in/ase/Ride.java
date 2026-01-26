package de.tum.in.ase;

public abstract class Ride {

	private String name;
	private char abbreviation;

	public Ride(String name, char abbreviation) {
		this.name = name;
		this.abbreviation = abbreviation;
	}

	public String getName() {
		return name;
	}

	public char getAbbreviation() {
		return abbreviation;
	}

}