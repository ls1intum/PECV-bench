package de.tum.cit.ase;

import de.tum.in.test.api.jupiter.PublicTest;

import static de.tum.in.test.api.util.ReflectionTestUtils.*;
import static org.assertj.core.api.Assertions.assertThat;

@T05E03
public class GoatBehaviorTest {
    private final String goatClassName = "de.tum.cit.ase.Goat";

    @PublicTest
    void feedGoatTest() {
        Class<?> goatClass = getClazz(goatClassName);
        Object goat = newInstance(goatClass, "elfriedegoat");
        String actual = (String) invokeMethod(goat, "messageOnFeed");
        String expected = "Maah!";

        assertThat(actual).as("Checking message on feeding a goat at method: messageOnFeed of class: Goat").isEqualTo(expected);
    }

    @PublicTest
    void milkGoatTest() {
        Class<?> goatClass = getClazz(goatClassName);
        Object goat = newInstance(goatClass, "elfriedegoat");
        String actual = (String) invokeMethod(goat, "messageOnMilk");
        String expected = "Goat " + invokeMethod(goat, getMethod(goat, "getName")) + " is milked";

        assertThat(actual).as("Checking message on milking a goat at method: messageOnMilk of class: Goat").isEqualTo(expected);


    }
}
