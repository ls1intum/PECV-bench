package de.tum.cit.ase;

import de.tum.in.test.api.BlacklistPath;
import de.tum.in.test.api.WhitelistPath;
import de.tum.in.test.api.jupiter.Public;
import de.tum.in.test.api.jupiter.PublicTest;
import de.tum.in.test.api.util.ReflectionTestUtils;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.text.ParseException;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

/**
 * @author Stephan Krusche (krusche@in.tum.de)
 * @version 5.1 (11.06.2021)
 */
@H01E02
class BehaviorTest {

    private static final Random RNG = new Random();

    private final String LECTURE_NAME = String.valueOf(RNG.nextInt(9999999));
    private final int INSCRIBED_STUDENTS = RNG.nextInt(9999999);
    private final int GUEST_STUDENTS = RNG.nextInt(9999999);
    private final int LECTURERS = RNG.nextInt(9999999);
    private final int TUTORS = RNG.nextInt(9999999);

    private Class<?> lectureClass = ReflectionTestUtils.getClazz("de.tum.cit.ase.Lecture");

    private Object tester;

    @BeforeEach
    void setup() {
        Constructor<?> lectureConstructor = ReflectionTestUtils.getConstructor(lectureClass, String.class, int.class, int.class, int.class, int.class);
        tester = ReflectionTestUtils.newInstance(lectureConstructor, LECTURE_NAME, INSCRIBED_STUDENTS, GUEST_STUDENTS, LECTURERS, TUTORS);
    }

    @PublicTest
    void getLectureNameTest() {
        testGetter(lectureClass, "getLectureName", tester, LECTURE_NAME, String.class);
    }

    @PublicTest
    void getNumberOfInscribedStudentsTest() {
        testGetter(lectureClass, "getNumberOfInscribedStudents", tester, INSCRIBED_STUDENTS, int.class);
    }

    @PublicTest
    void getNumberOfGuestStudentsTest() {
        testGetter(lectureClass, "getNumberOfGuestStudents", tester, GUEST_STUDENTS, int.class);
    }

    @PublicTest
    void getNumberOfLecturersTest() {
        testGetter(lectureClass, "getNumberOfLecturers", tester, LECTURERS, int.class);
    }

    @PublicTest
    void getNumberOfTutorsTest() {
        testGetter(lectureClass, "getNumberOfTutors", tester, TUTORS, int.class);
    }

    @PublicTest
    void setLectureNameTest() {
        Method setter = ReflectionTestUtils.getMethod(lectureClass, "setLectureName", String.class);
        String valueToSet = String.valueOf(RNG.nextInt(9999999));
        ReflectionTestUtils.invokeMethod(tester, setter, valueToSet);


        Class<?> lectureClass1 = ReflectionTestUtils.getClazz("de.tum.cit.ase.Lecture");
        var valueSetter = AttributeHelper.readAttribute(lectureClass1, "lectureName", tester, String.class);

        if (!valueSetter.equals(valueToSet)) {
            fail("The method setLectureName does not return the correct value.");
        }
    }

    @PublicTest
    void setNumberOfInscribedStudentsTest() {
        Method setter = ReflectionTestUtils.getMethod(lectureClass, "setNumberOfInscribedStudents", int.class);
        int valueToSet = RNG.nextInt(9999999);
        ReflectionTestUtils.invokeMethod(tester, setter, valueToSet);


        Class<?> lectureClass1 = ReflectionTestUtils.getClazz("de.tum.cit.ase.Lecture");
        var valueSetter = AttributeHelper.readAttribute(lectureClass1, "numberOfInscribedStudents", tester, Integer.class);

        if (!valueSetter.equals(valueToSet)) {
            fail("The method setNumberOfInscribedStudents does not return the correct value.");
        }
    }

    @PublicTest
    void setNumberOfGuestStudentsTest() {
        Method setter = ReflectionTestUtils.getMethod(lectureClass, "setNumberOfGuestStudents", int.class);
        int valueToSet = RNG.nextInt(9999999);
        ReflectionTestUtils.invokeMethod(tester, setter, valueToSet);


        Class<?> lectureClass1 = ReflectionTestUtils.getClazz("de.tum.cit.ase.Lecture");
        var valueSetter = AttributeHelper.readAttribute(lectureClass1, "numberOfGuestStudents", tester, Integer.class);

        if (!valueSetter.equals(valueToSet)) {
            fail("The method setNumberOfGuestStudents does not return the correct value.");
        }
    }

    @PublicTest
    void setNumberOfLecturersTest() {
        Method setter = ReflectionTestUtils.getMethod(lectureClass, "setNumberOfLecturers", int.class);
        int valueToSet = RNG.nextInt(9999999);
        ReflectionTestUtils.invokeMethod(tester, setter, valueToSet);


        Class<?> lectureClass1 = ReflectionTestUtils.getClazz("de.tum.cit.ase.Lecture");
        var valueSetter = AttributeHelper.readAttribute(lectureClass1, "numberOfLecturers", tester, Integer.class);

        if (!valueSetter.equals(valueToSet)) {
            fail("The method setNumberOfLecturers does not return the correct value.");
        }
    }

    @PublicTest
    void setNumberOfTutorsTest() {
        Method setter = ReflectionTestUtils.getMethod(lectureClass, "setNumberOfTutors", int.class);
        int valueToSet = RNG.nextInt(9999999);
        ReflectionTestUtils.invokeMethod(tester, setter, valueToSet);


        Class<?> lectureClass1 = ReflectionTestUtils.getClazz("de.tum.cit.ase.Lecture");
        var valueSetter = AttributeHelper.readAttribute(lectureClass1, "numberOfTutors", tester, Integer.class);

        if (!valueSetter.equals(valueToSet)) {
            fail("The method setNumberOfTutors does not return the correct value.");
        }
    }

    @PublicTest
    void toStringTest() {
        String[] requiredStrings = {LECTURE_NAME, String.valueOf(INSCRIBED_STUDENTS), String.valueOf(GUEST_STUDENTS), String.valueOf(LECTURERS), String.valueOf(TUTORS)};
        String[] requiredStringLabels = {"lecture name", "number of inscribed students", "number of guest students", "number of lecturers", "number of tutors"};
        String stringToTest = (String) invokeGetterFromClass(lectureClass, "toString", tester);
        for (int i = 0; i < requiredStrings.length; i++) {
            assertTrue(stringToTest.contains(requiredStrings[i]), "The method toString does not generate a string that contains the " + requiredStringLabels[i] + ".");
        }
    }

    @PublicTest
    void getTotalNumberOfStudentsTest() {
        assertEquals(invokeGetterFromClass(lectureClass, "getTotalNumberOfStudents", tester), INSCRIBED_STUDENTS + GUEST_STUDENTS, "The method getTotalNumberOfStudentsTest does not return the correct number of total students");
    }

    @PublicTest
    void getNameAndTotalNumberOfStudentsTest() {
        assertEquals(invokeGetterFromClass(lectureClass, "getNameAndTotalNumberOfStudents", tester), LECTURE_NAME + " (" + (INSCRIBED_STUDENTS + GUEST_STUDENTS) + ")", "The method getNameAndTotalNumberOfStudents does not return the correct text");
    }

    @PublicTest
    void getNumberOfStudentsPerTutorTest() {
        assertEquals(invokeGetterFromClass(lectureClass, "getNumberOfStudentsPerTutor", tester), (INSCRIBED_STUDENTS + GUEST_STUDENTS) / TUTORS, "The method getNumberOfStudentsPerTutor does not return the correct value");
    }

    @PublicTest
    void addGuestStudentsTest() {
        Method addGuestStudents = ReflectionTestUtils.getMethod(lectureClass, "addGuestStudents", int.class);
        int valueToAdd = RNG.nextInt(9999999);
        ReflectionTestUtils.invokeMethod(tester, addGuestStudents, valueToAdd);
        assertEquals((GUEST_STUDENTS + valueToAdd), invokeGetterFromClass(lectureClass, "getNumberOfGuestStudents", tester), "The method addGuestStudents does not properly add the given amount of guest students");
    }

    // Utility Methods

    private static Object invokeGetterFromClass(Class<?> classObject, String getterName, Object tester) {
        Method method = ReflectionTestUtils.getMethod(classObject, getterName);
        return ReflectionTestUtils.invokeMethod(tester, method);
    }

    private static void testGetter(Class<?> classObject, String getterName, Object tester, Object correctValue, Class<?> getterAttributeClass) {
        if (!invokeGetterFromClass(classObject, getterName, tester).equals(correctValue)) {
            fail("The method " + getterName + " does not return the correct value.");
        }
    }

    private static void testSetter(Class<?> classObject, String setterName, Class<?> setterAttributeClass, String attributeName, Object tester) {
        Method setter = ReflectionTestUtils.getMethod(classObject, setterName, setterAttributeClass);
        String valueToSet = String.valueOf(RNG.nextInt(9999999));
        ReflectionTestUtils.invokeMethod(tester, setter, valueToSet);


       Class<?> lectureClass1 = ReflectionTestUtils.getClazz("de.tum.cit.ase.Lecture");
       var valueSetter = AttributeHelper.readAttribute(lectureClass1, attributeName, tester, setterAttributeClass);

        if (!valueSetter.equals(setterName)) {
            fail("The method " + setterName + " does not return the correct value.");
        }
    }

}
