package de.tum.cit.ase;

import de.tum.in.test.api.jupiter.PublicTest;

import static de.tum.in.test.api.util.ReflectionTestUtils.*;
import static org.assertj.core.api.Assertions.assertThat;

@T05E03
public class SealBehaviorTest {
    private final String cowClassName = "de.tum.cit.ase.Seal";

    @PublicTest
    void feedSealTest() {
        Class<?> cowClass = getClazz(cowClassName);
        Object seal = newInstance(cowClass, "elfriedecow");
        String actual = (String) invokeMethod(seal, "messageOnFeed");
        String expected = "Arf Arf!";

        assertThat(actual).as("Checking message on feeding a seal at method: messageOnFeed of class: Seal").isEqualTo(expected);
    }

    @PublicTest
    void milkSealTest() {
        Class<?> cowClass = getClazz(cowClassName);
        Object seal = newInstance(cowClass, "elfriedecow");
        String actual = (String) invokeMethod(seal, "messageOnMilk");
        String expected = "Seal " + invokeMethod(seal, getMethod(seal, "getName")) + " is milked";

        assertThat(actual).as("Checking message on milking a seal at method: messageOnMilk of class: Seal").isEqualTo(expected);
    }

    @PublicTest
    void rideSealTest() {
        Class<?> cowClass = getClazz(cowClassName);
        Object seal = newInstance(cowClass, "elfriedecow");
        String actual = (String) invokeMethod(seal, "messageOnRide");
        String expected = "Riding on Seal " + invokeMethod(seal, getMethod(seal, "getName"));

        assertThat(actual).as("Checking message on riding a seal at method: messageOnRide of class: Seal").isEqualTo(expected);
    }
}
