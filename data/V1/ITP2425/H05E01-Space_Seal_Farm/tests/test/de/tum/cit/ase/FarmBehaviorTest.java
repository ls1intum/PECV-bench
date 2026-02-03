package de.tum.cit.ase;

import de.tum.cit.ase.solution.Animal;
import de.tum.cit.ase.solution.Seal;
import de.tum.cit.ase.solution.Farm;
import de.tum.cit.ase.solution.Goat;
import de.tum.cit.ase.solution.Pig;
import de.tum.in.test.api.io.IOTester;
import de.tum.in.test.api.jupiter.PublicTest;

import java.lang.reflect.Method;
import java.util.*;

import static de.tum.in.test.api.util.ReflectionTestUtils.*;
import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.fail;

@T05E03
public class FarmBehaviorTest {
	private static final int ANIMAL_COUNT = 20;
	private final String farmClassName = "de.tum.cit.ase.Farm";
	private final String animalClassName = "de.tum.cit.ase.Animal";

	private final String cowClassName = "de.tum.cit.ase.Seal";
	private final String pigClassName = "de.tum.cit.ase.Pig";
	private final String goatClassName = "de.tum.cit.ase.Goat";

	@PublicTest
	void getAnimalsTest() {
		Class<?> farmClass = getClazz(farmClassName);
		Class<?> animalClass = getClazz(animalClassName);
		Class<?> cowClass = getClazz(cowClassName);
		Class<?> pigClass = getClazz(pigClassName);
		Class<?> goatClass = getClazz(goatClassName);

		Object farm = newInstance(farmClass);
		Method addAnimal = getMethod(farmClass, "addAnimal", animalClass);
		Method getAnimals = getMethod(farmClass, "getAnimals");
		ArrayList<Animal> expectedAnimals = new ArrayList<>();

		for (int i = 0; i < ANIMAL_COUNT; i++) {
			int random = new Random().nextInt(1, 4);
			switch (random) {
				case 1: {
					expectedAnimals.add(new de.tum.cit.ase.solution.Seal("elfriedecow" + i));
					invokeMethod(farm, addAnimal, newInstance(cowClass, ("elfriedecow" + i)));
				}
				case 2: {
					expectedAnimals.add(new de.tum.cit.ase.solution.Pig("elfriedepig" + i));
					invokeMethod(farm, addAnimal, newInstance(pigClass, ("elfriedepig" + i)));
				}
				case 3: {
					expectedAnimals.add(new de.tum.cit.ase.solution.Goat("elfriedegoat" + i));
					invokeMethod(farm, addAnimal, newInstance(goatClass, ("elfriedegoat" + i)));
				}
			}
		}

		ArrayList<Object> actualAnimals = (ArrayList<Object>) invokeMethod(farm, getAnimals);

		assertThat(actualAnimals.size()).as("Checking the number of animals in the farm at method: getAnimals of class: Farm").isEqualTo(expectedAnimals.size());

		for (int i = 0; i < expectedAnimals.size(); i++) {
			assertThat(actualAnimals.get(i)).as("Checking the animals in the farm at method: getAnimals of class: Farm").usingRecursiveComparison().isEqualTo(expectedAnimals.get(i));
		}
	}

	@PublicTest
	void executeSongMethod(IOTester io) {
		Class<?> farmClass = getClazz(farmClassName);
		Class<?> animalClass = getClazz(animalClassName);
		Class<?> cowClass = getClazz(cowClassName);
		Class<?> pigClass = getClazz(pigClassName);
		Class<?> goatClass = getClazz(goatClassName);

		Object farm = newInstance(farmClass);
		Method singFarmSong = getMethod(farmClass, "singFarmSong");
		Method addAnimal = getMethod(farmClass, "addAnimal", animalClass);

		de.tum.cit.ase.solution.Farm expectedFarm = new Farm();

		for (int i = 0; i < ANIMAL_COUNT; i++) {
			int random = new Random().nextInt(1, 4);
			switch (random) {
				case 1: {
					expectedFarm.addAnimal(new Seal("elfriedecow" + i));
					invokeMethod(farm, addAnimal, newInstance(cowClass, ("elfriedecow" + i)));
				}
				case 2: {
					expectedFarm.addAnimal(new Pig("elfriedepig" + i));
					invokeMethod(farm, addAnimal, newInstance(pigClass, ("elfriedepig" + i)));
				}
				case 3: {
					expectedFarm.addAnimal(new Goat("elfriedegoat" + i));
					invokeMethod(farm, addAnimal, newInstance(goatClass, ("elfriedegoat" + i)));
				}
			}
		}

		List<String> expectedLines = new ArrayList<>(Arrays.asList((expectedFarm.singFarmSong().split("\n"))));
		invokeMethod(farm, singFarmSong);
		var actualLines = io.getOutTester().getLinesAsString();

		assertThat(actualLines).as("Checking if song is empty at method: singFarmSong of class: Farm").isNotEmpty();
		assertThat(actualLines.size()).as("Checking the length of song at method: singFarmSong of class: Farm").isEqualTo(expectedLines.size());

		for (int i = 0; i < expectedLines.size(); i++) {
			assertThat(actualLines.get(i)).as("Checking the song at method: singFarmSong of class: Farm at line: " + i).isEqualTo(expectedLines.get(i));
		}
	}

	@PublicTest
	void farmConstructs() {
		Class<?> farmClass = getClazz(farmClassName);
		Object farm = newInstance(farmClass);

		if (Objects.isNull(farm)) {
			fail("Could not construct the Farm class. Make sure that it has a constructor with no parameters");
		}

		List<?> animalsList = AttributeHelper.readAttribute(farmClass, "animals", farm, List.class);
		if (Objects.isNull(animalsList)) {
			fail("You have failed to initialize the animals attribute in Farm to a default value, which is an empty ArrayList.");
		}
	}
}
