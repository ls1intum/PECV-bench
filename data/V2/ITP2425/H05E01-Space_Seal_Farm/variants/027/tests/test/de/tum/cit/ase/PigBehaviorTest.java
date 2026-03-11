package de.tum.cit.ase;

import de.tum.in.test.api.jupiter.PublicTest;

import static de.tum.in.test.api.util.ReflectionTestUtils.*;
import static org.assertj.core.api.Assertions.assertThat;

@T05E03
public class PigBehaviorTest {
    private final String pigClassName = "de.tum.cit.ase.Pig";

    @PublicTest
    void feedPigTest() {
        Class<?> pigClass = getClazz(pigClassName);
        Object pig = newInstance(pigClass, "elfriedepig");
        String actual = (String) invokeMethod(pig, "messageOnFeed");
        String expected = "Oink!";

        assertThat(actual).as("Checking message on feeding a pig at method: messageOnFeed of class: Pig").isEqualTo(expected);
    }

    @PublicTest
    void ridePigTest() {
        Class<?> pigClass = getClazz(pigClassName);
        Object pig = newInstance(pigClass, "elfriedepig");
        String actual = (String) invokeMethod(pig, "messageOnRide");
        String expected = "Riding on Pig " + invokeMethod(pig, getMethod(pig, "getName"));

        assertThat(actual).as("Checking message on riding a pig at method: messageOnRide of class: Pig").isEqualTo(expected);
    }
}
