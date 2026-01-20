package de.tum.in.ase.eist;

import static org.junit.jupiter.api.Assertions.*;
import static org.assertj.core.api.Assertions.assertThat;

import de.tum.in.ase.eist.model.Person;
import de.tum.in.ase.eist.util.PersonSortingOptions;
import de.tum.in.test.api.util.ReflectionTestUtils;

import java.lang.reflect.Field;
import java.util.List;
import java.util.Objects;
import java.util.function.Consumer;

public class H05E01Client {

    private static final String PERSON_CONTROLLER_FULL_NAME = "de.tum.in.ase.eist.controller.PersonController";

    public static Object createPersonController() {
        return ReflectionTestUtils.newInstance(ReflectionTestUtils.getConstructor(ReflectionTestUtils.getClazz(PERSON_CONTROLLER_FULL_NAME)));
    }

    public static void invokeAddPerson(Object personController, Person person, Consumer<List<Person>> personConsumer) {
        var method = ReflectionTestUtils.getMethod(personController, "addPerson", Person.class, Consumer.class);
        ReflectionTestUtils.invokeMethod(personController, method, person, personConsumer);
    }

    public static void invokeUpdatePerson(Object personController, Person person, Consumer<List<Person>> personConsumer) {
        var method = ReflectionTestUtils.getMethod(personController, "updatePerson", Person.class, Consumer.class);
        ReflectionTestUtils.invokeMethod(personController, method, person, personConsumer);
    }

    public static void invokeDeletePerson(Object personController, Person person, Consumer<List<Person>> personConsumer) {
        var method = ReflectionTestUtils.getMethod(personController, "deletePerson", Person.class, Consumer.class);
        ReflectionTestUtils.invokeMethod(personController, method, person, personConsumer);
    }

    public static void invokeGetAllPersons(Object personController, PersonSortingOptions sortingOptions, Consumer<List<Person>> personConsumer) {
        var method = ReflectionTestUtils.getMethod(personController, "getAllPersons", PersonSortingOptions.class, Consumer.class);
        ReflectionTestUtils.invokeMethod(personController, method, sortingOptions, personConsumer);
    }

    public static void assertPersonListEquals(List<Person> expectedList, List<Person> actualList, String methodName) {
        assertNotNull(actualList, "The resulting list of persons was null after invoking PersonController::" + methodName + ".");
        assertEquals(expectedList.size(), actualList.size(), "The resulting list of persons does not have the correct size after invoking PersonController::" + methodName + ".");

        boolean wrongOrder = false;

        for (int i=0; i<expectedList.size(); i++) {
            if(!checkIfPersonEqual(expectedList.get(i), actualList.get(i), false)) {
                wrongOrder = true;
                break;
            }
        }

        if(!wrongOrder) return;

        var sortedExpectedList = expectedList.stream().sorted((a, b) -> {
            if (a.getFirstName() == null) {
                return -1;
            } else if (b.getFirstName() == null) {
                return 1;
            } else {
                return a.getFirstName().compareTo(b.getFirstName());
            }
        }).toList();

        var sortedActualList = expectedList.stream().sorted((a, b) -> {
            if (a.getFirstName() == null) {
                return -1;
            } else if (b.getFirstName() == null) {
                return 1;
            } else {
                return a.getFirstName().compareTo(b.getFirstName());
            }
        }).toList();

        for (int i = 0; i < sortedExpectedList.size(); i++) {
            if(checkIfPersonEqual(sortedExpectedList.get(i), sortedActualList.get(i), false)) {
                fail("The resulting list of persons is not sorted correctly after invoking PersonController::" + methodName + ".");
            }
        }

        fail("The resulting list of persons does not contain the correct persons after invoking PersonController::" + methodName + ".");
    }

    public static void setPersonControllerPersons(Object personController, List<Person> personList) {
        Field persons;
        Object fieldValue;
        List<Person> reflectedPersonList;
        try {
            persons = personController.getClass().getDeclaredField("persons");
            persons.setAccessible(true);

            fieldValue = persons.get(personController);
            assertThat(fieldValue).isInstanceOf(List.class);

            reflectedPersonList = (List<Person>) fieldValue;
        } catch (NoSuchFieldException | IllegalAccessException e) {
            fail("The implementation of the attribute 'persons' in class 'PersonController' is not correct.");
            return;
        }
        try {
            reflectedPersonList.removeIf(p -> true);
            reflectedPersonList.addAll(personList);
        } catch (Exception e) {
            fail("An unexpected error has occurred. Contact your tutor.");
        }
    }

    public static boolean checkIfPersonEqual(Person expectedPerson, Person actualPerson, boolean ignoreId) {
        var res = ignoreId || Objects.equals(expectedPerson.getId(), actualPerson.getId());
        return res && Objects.equals(expectedPerson.getFirstName(), actualPerson.getFirstName())
                && Objects.equals(expectedPerson.getLastName(), actualPerson.getLastName())
                && Objects.equals(expectedPerson.getBirthday(), actualPerson.getBirthday());
    }
}
