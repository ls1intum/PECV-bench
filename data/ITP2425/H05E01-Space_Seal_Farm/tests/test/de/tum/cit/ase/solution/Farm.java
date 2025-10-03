package de.tum.cit.ase.solution;

import java.util.ArrayList;
import java.util.List;

/**
 * Represents a Farm
 */
public class Farm {
    private List<Animal> animals;

    /**
     * Constructs an empty farm
     */
    public Farm() {
        this.animals = new ArrayList<>();
    }

    /**
     * Gets all the animals in the farm
     *
     * @return - all the animals in the farm
     */
    public List<Animal> getAnimals() {
        return animals;
    }

    /**
     * Set animals to a new list of animals
     *
     * @param animals - animals to be set
     */
    public void setAnimals(List<Animal> animals) {
        this.animals = animals;
    }

    /**
     * Adds an animal to the farm
     *
     * @param animal - animal to be added to the farm
     */
    public void addAnimal(Animal animal) {
        animals.add(animal);
    }

    /**
     * Feeds all the animals on the farm
     * and prints respective messages on feed of each animal
     */
    public void feedAllAnimals() {
        for (Animal a : animals) {
            System.out.println(a.messageOnFeed());
        }
    }

    /**
     * Prints the animal specific song given an animal
     *
     * @param a - animal whose song is to be printed
     */
    public String singFarmSongVerse(Animal a) {
        return "Old MacDonald had a farm\n" + "Ee i ee i o\n" + "And on his farm he had some " + a.getClass().getSimpleName() + "s\n" +
                "Ee i ee i oh\nWith a \n" +
                a.messageOnFeed() + "\n" +
                a.messageOnFeed() + "\n" +
                "here, and a \n" +
                a.messageOnFeed() + "\n" +
                a.messageOnFeed() + "\n" +
                "there.\nHere a \n" +
                a.messageOnFeed() + "\n" +
                "There a \n" +
                a.messageOnFeed() + "\n" +
                "Everywhere a \n" +
                a.messageOnFeed() + "\n" +
                a.messageOnFeed() + "\n" +
                "Old MacDonald had a farm\n" +
                "Ee i ee i o\n";
    }


    /**
     * Sings farm song for all animals in the farm
     */
    public String singFarmSong() {
        StringBuilder result = new StringBuilder();
        for (Animal a : animals) {
            result.append(singFarmSongVerse(a));
        }
        return result.toString();
    }
}

