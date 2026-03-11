package de.tum.in.ase;

import de.tum.in.test.api.jupiter.HiddenTest;
import de.tum.in.test.api.util.ReflectionTestUtils;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.*;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

@E01V01
public class BehaviorTest {

	// Feedback messages for tests
	final String getNameMessage = "getName return value";
	final String getAbbreviationMessage = "getAbbreviation return value";
	final String chainSpeedMessage = "getChainSpeed return value";
	final String getNumberOfLoopingsMessage = "getNumberOfLoopings return value";
	final String getRidesMessage = "getRides return value";
	final String isExcellentEnoughMessage = "isExcellentEnough return value";
	final String getExcellencyLevelMessage = "getExcellencyLevel return value";

	@HiddenTest
	void checkLaunchedDropdownTowerConstructorAndGetters() {
		String name = "LaunchedDropdownTower";
		char abbreviation = 'D';

		Object launchedDropdownTower = HelperClass.createInstance("de.tum.in.ase.LaunchedDropdownTower",
				new Class[]{String.class, char.class},
				name, abbreviation);

		String actualName = (String) HelperClass.invokeMethod(launchedDropdownTower, "getName", false, new Class[]{});
		char actualAbbreviation = (char) HelperClass.invokeMethod(launchedDropdownTower, "getAbbreviation", false, new Class[]{});

		String testName = "LaunchedDropdownTower Constructor and Getters: ";

		assertEquals(name, actualName, testName + getNameMessage);
		assertEquals(abbreviation, actualAbbreviation, testName + getAbbreviationMessage);
	}

	@HiddenTest
	void checkLaunchedRollerCoasterConstructorAndGetters() {
		String name = "LaunchedRollerCoaster";
		char abbreviation = 'L';
		int numberOfLoopings = 5;

		Object launchedRollerCoaster = HelperClass.createInstance("de.tum.in.ase.LaunchedRollerCoaster",
				new Class[]{String.class, char.class, int.class},
				name, abbreviation, numberOfLoopings);

		String actualName = (String) HelperClass.invokeMethod(launchedRollerCoaster, "getName", false, new Class[]{});
		char actualAbbreviation = (char) HelperClass.invokeMethod(launchedRollerCoaster, "getAbbreviation", false, new Class[]{});
		int actualNumberOfLoopings = (int) HelperClass.invokeMethod(launchedRollerCoaster, "getNumberOfLoopings", false, new Class[]{});

		String testName = "LaunchedRollerCoaster Constructor and Getters: ";

		assertEquals(name, actualName, testName + getNameMessage);
		assertEquals(abbreviation, actualAbbreviation, testName + getAbbreviationMessage);
		assertEquals(numberOfLoopings, actualNumberOfLoopings, testName + getNumberOfLoopingsMessage);
	}

	@HiddenTest
	void checkExcellentLandConstructorAndGetters() throws InvocationTargetException, InstantiationException, IllegalAccessException {
		double latitude = 49.1466847;
		double longitude = 9.2175836;
		int heightAboveSea = 157;

		Object launchedRollerCoaster = HelperClass.createInstance("de.tum.in.ase.LaunchedRollerCoaster",
				new Class[]{String.class, char.class, int.class},
				"LaunchedRollerCoaster", 'L', 5);

		Object launchedDropdownTower = HelperClass.createInstance(
				"de.tum.in.ase.LaunchedDropdownTower",
				new Class[]{String.class, char.class},
				"LaunchedDropdownTower", 'D');

		assert launchedRollerCoaster != null;
		assert launchedDropdownTower != null;
		List<Object> rides = List.of(launchedRollerCoaster, launchedDropdownTower);

		Object excellenceLand = getExcellentLand(100.0, true, rides);

		Object actualExcellencyLevel = HelperClass.invokeMethod(excellenceLand, "getExcellencyLevel",
				false, new Class[]{});
		Object actualExcellentEnough = HelperClass.invokeMethod(excellenceLand, "isExcellentEnough", false, new Class[]{});
		Object actualVehicles = HelperClass.invokeMethod(excellenceLand, "getRides",
				false, new Class[]{});

		String testName = "ExcellenceLand Constructor and Getters: ";
		assertEquals(100.0, actualExcellencyLevel, testName + getExcellencyLevelMessage);
		assertEquals(true, actualExcellentEnough, testName + isExcellentEnoughMessage);
		assertEquals(rides, actualVehicles, testName + getRidesMessage);
	}

	private Object getExcellentLand(double excellencyLevel, boolean excellentEnough, List<Object> rides)
			throws InvocationTargetException, InstantiationException, IllegalAccessException {
		var excellenceLandClass = ReflectionTestUtils.getClazz("de.tum.in.ase.ExcellenceLand");

		var constructors = excellenceLandClass.getDeclaredConstructors();
		if(constructors.length == 0) fail();

		var constructor = constructors[0];

		var args = new Object[3];
		for(int i = 0; i < 3; i++) {
			var argument = constructor.getParameters()[i].getType();
			if(argument.equals(double.class)) {
				args[i] = excellencyLevel;
			} else if (argument.equals(boolean.class)) {
				args[i] = excellentEnough;
			} else if (argument.equals(List.class)) {
				args[i] = rides;
			}
		}

		var excellenceLand = constructor.newInstance(args);

		return excellenceLand;
	}
}
