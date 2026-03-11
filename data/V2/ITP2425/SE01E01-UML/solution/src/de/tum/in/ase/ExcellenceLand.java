package de.tum.in.ase;

import java.util.List;

public class ExcellenceLand {
	
	private double excellencyLevel;
	private boolean excellentEnough;
	private List<Ride> rides;

	public ExcellenceLand(double excellencyLevel, boolean excellentEnough, List<Ride> rides) {
		this.excellencyLevel = excellencyLevel;
		this.excellentEnough = excellentEnough;
		this.rides = rides;
	}

	public double getExcellencyLevel() {
		return excellencyLevel;
	}

	public boolean isExcellentEnough() {
		return excellentEnough;
	}

	public List<Ride> getRides() {
		return rides;
	}

}