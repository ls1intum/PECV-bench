package de.tum.cit.ase;

import java.util.ArrayList;
import java.util.List;

public class Farm {
	//TODO 3.1: Implement Farm as described in task

	private List<Animal> animals;

	public Farm() {
		this.animals = new ArrayList<>();
	}

	public List<Animal> getAnimals() {
		return animals;
	}

	public void setAnimals(List<Animal> animals) {
		this.animals = animals;
	}

	public void addAnimal(Animal animal) {
		animals.add(animal);
	}

	public void feedAllAnimals() {
		for (Animal a : animals) {
			System.out.println(a.messageOnFeed());
		}
	}

	private void singFarmSongVerse(Animal animal) {
		System.out.println("Old MacDonald had a farm\n" +
				"Ee i ee i o\n" +
				"And on his farm he had some " + animal.getClass().getSimpleName() + "s");
		System.out.println("Ee i ee i oh");
		System.out.println("With a ");
		System.out.println(animal.messageOnFeed());
		System.out.println(animal.messageOnFeed());
		System.out.println("here, and a ");
		System.out.println(animal.messageOnFeed());
		System.out.println(animal.messageOnFeed());
		System.out.println("there.");
		System.out.println("Here a ");
		System.out.println(animal.messageOnFeed());
		System.out.println("There a ");
		System.out.println(animal.messageOnFeed());
		System.out.println("Everywhere a ");
		System.out.println(animal.messageOnFeed());
		System.out.println(animal.messageOnFeed());
		System.out.println("Old MacDonald had a farm\n" +
				"Ee i ee i o");
	}

	/**
	 * Sings farm song for all animals in the farm
	 */
	public void singFarmSong() {
		// TODO 3.2: Let the Animals sing!
		for (Animal animal : animals) {
			singFarmSongVerse(animal);
		}
	}
}

