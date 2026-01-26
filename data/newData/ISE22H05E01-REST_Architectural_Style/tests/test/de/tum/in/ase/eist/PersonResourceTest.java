package de.tum.in.ase.eist;

import com.fasterxml.jackson.databind.ObjectMapper;
import de.tum.in.ase.eist.model.Person;
import de.tum.in.ase.eist.rest.PersonResource;
import de.tum.in.ase.eist.service.PersonService;
import de.tum.in.ase.eist.util.PersonSortingOptions;
import org.junit.jupiter.api.*;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.web.servlet.MockMvc;

import java.lang.reflect.Field;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import static de.tum.in.ase.eist.H05E01Client.checkIfPersonEqual;
import static de.tum.in.ase.eist.util.PersonSortingOptions.SortingOrder.ASCENDING;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;

@H05E01
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT)
// this is required to reset the persons saved in PersonService
@DirtiesContext(classMode = DirtiesContext.ClassMode.AFTER_EACH_TEST_METHOD)
@AutoConfigureMockMvc
public class PersonResourceTest {

    @Autowired
    private MockMvc mvc;

    @Autowired
    private ApplicationContext context;

    private static ObjectMapper objectMapper;
    private static Object personService;

    private Person person1;
    private Person person2;

    @BeforeAll
    static void setUp() {
        objectMapper = new ObjectMapper();
        objectMapper.findAndRegisterModules();
    }

    @BeforeEach
    void initialize() {
        try {
            personService = context.getBean(PersonService.class);
        } catch (NoSuchBeanDefinitionException e) {
            fail("PersonService is not defined correctly as a Spring-Service.");
        }

        try {
            context.getBean(PersonResource.class);
        } catch (NoSuchBeanDefinitionException e) {
            fail("PersonResource is not defined correctly as a Spring-Controller.");
        }

        person1 = new Person();
        person1.setFirstName("Max");
        person1.setLastName("Musterfrau");
        person1.setBirthday(LocalDate.ofYearDay(2000, 125));

        person2 = new Person();
        person2.setFirstName("Erika");
        person2.setLastName("Mustermann");
        person2.setBirthday(LocalDate.ofYearDay(1999, 80));
    }

    @Test
    @DisplayName("Create valid person (Server)")
    public void testAddSingleUser() throws Exception {
        var response = this.mvc.perform(
                post("/persons")
                        .content(objectMapper.writeValueAsString(person1))
                        .contentType("application/json")).andReturn().getResponse();

        if (response.getStatus() == 404 || response.getStatus() == 405) {
            fail("The endpoint POST /persons has not been implemented.");
        }
        assertEquals(200, response.getStatus(), "PersonResource::createPerson did not return the correct status code");
        assertEquals("application/json", response.getContentType());

        var personsInService = getAllPersonsByReflection();
        if (personsInService == null || personsInService.size() != 1) {
            fail("After calling PersonResource::createPerson, PersonResource::persons contain the wrong amount of persons.");
        }
        var createdPerson = personsInService.get(0);

        var responseEntity = objectMapper.readValue(response.getContentAsString(), Person.class);
        if (!checkIfPersonEqual(createdPerson, responseEntity, true)) {
            fail("PersonResource::createPerson did not return the correct person as response body.");
        }
    }

    @Test
    @DisplayName("Create invalid person (Server)")
    public void testAddInvalidPerson() throws Exception {
        var uuid = UUID.randomUUID();
        person1.setId(uuid);

        var response = this.mvc.perform(
                        post("/persons")
                                .content(objectMapper.writeValueAsString(person1))
                                .contentType("application/json")).andReturn().getResponse();
        if (response.getStatus() == 404 || response.getStatus() == 405) {
            fail("The endpoint POST /persons has not been implemented.");
        }
        assertEquals(400, response.getStatus(), "PersonResource::createPerson did not return the correct status code for an invalid request body.");
    }

    @Test
    @DisplayName("Update existing person (Server)")
    public void testUpdateExistingPerson() throws Exception {
        var id = UUID.randomUUID();
        person1.setId(id);
        setAllPersonsByReflection(List.of(person1));

        person1.setFirstName("Changed");
        person1.setLastName("Name");

        var response = this.mvc.perform(
                        put("/persons/" + person1.getId())
                                .content(objectMapper.writeValueAsString(person1))
                                .contentType("application/json")).andReturn().getResponse();
        if (response.getStatus() == 404 || response.getStatus() == 405) {
            fail("The endpoint PUT /persons/:personId has not been implemented.");
        }
        assertEquals(200, response.getStatus(), "PersonResource::updatePerson did not return the correct status code.");
        assertEquals("application/json", response.getContentType());

        var personsInService = getAllPersonsByReflection();
        if (personsInService == null || personsInService.size() != 1) {
            fail("After calling PersonResource::updatePerson, PersonResource::persons contain the wrong amount of persons.");
        }
        var updatedPerson = personsInService.get(0);

        var responseEntity = objectMapper.readValue(response.getContentAsString(), Person.class);
        if (!checkIfPersonEqual(updatedPerson, responseEntity, false)) {
            fail("PersonResource::updatePerson did not return the correct person as response body.");
        }
    }

    @Test
    @DisplayName("Update person with mismatching IDs (Server)")
    public void testUpdatePersonWithIdMismatch() throws Exception {
        var mismatchedId = UUID.randomUUID();

        var id = UUID.randomUUID();
        person1.setId(id);
        setAllPersonsByReflection(List.of(person1));

        var response = this.mvc.perform(
                        put("/persons/" + mismatchedId)
                                .content(objectMapper.writeValueAsString(person1))
                                .contentType("application/json")).andReturn().getResponse();
        if (response.getStatus() == 404 || response.getStatus() == 405) {
            fail("The endpoint PUT /persons/:personId has not been implemented.");
        }
        assertEquals(400, response.getStatus(), "PersonResource::updatePerson did not return the correct status code for an invalid response body.");
    }

    @Test
    @DisplayName("Delete existing person (Server)")
    public void testDeleteExistingPerson() throws Exception {
        var id = UUID.randomUUID();
        person1.setId(id);
        setAllPersonsByReflection(List.of(person1));

        var response = this.mvc.perform(
                delete("/persons/" + person1.getId())
                        .content(objectMapper.writeValueAsString(person1))
                        .contentType("application/json")).andReturn().getResponse();
        if (response.getStatus() == 404 || response.getStatus() == 405) {
            fail("The endpoint DELETE /persons/:personId has not been implemented.");
        }
        assertEquals(204, response.getStatus(), "PersonResource::deletePerson did not return the correct status code.");
    }

    @Test
    @DisplayName("Get all persons with sorting options (Server)")
    public void testGetAllPersons() throws Exception {
        var id1 = UUID.randomUUID();
        var id2 = UUID.randomUUID();
        person1.setId(id1);
        person2.setId(id2);
        setAllPersonsByReflection(List.of(person1, person2));

        for (var fieldOption: PersonSortingOptions.SortField.values()) {
            for (var orderOption: PersonSortingOptions.SortingOrder.values()) {
                var sortedList = getSortedList(List.of(person1, person2), orderOption, fieldOption);
                var response = this.mvc.perform(
                                get("/persons")
                                        .param("sortField", fieldOption.name())
                                        .param("sortingOrder", orderOption.name())
                                        .contentType("application/json")).andReturn().getResponse();

                if (response.getStatus() == 404 || response.getStatus() == 405) {
                    fail("The endpoint GET /persons has not been implemented.");
                }
                assertEquals(200, response.getStatus(), "PersonResource::getAllPersons did not return the correct status code.");

                var respondedPersons = objectMapper.readValue(response.getContentAsString(), Person[].class);
                if (respondedPersons.length != 2) {
                    fail("PersonResource::getAllPersons did not return the correct amount of persons.");
                }
                for (int i = 0; i < respondedPersons.length; i++){
                    if (!checkIfPersonEqual(sortedList.get(i), respondedPersons[i], false)) {
                        fail("PersonResource::getAllPersons did not contain the correct person/correct order as response body for a request with sorting options.");
                    }
                }
            }
        }
    }

    @Test
    @DisplayName("Get all persons with default request parameters (Server)")
    public void testDefaultSortValues() throws Exception {
        var id1 = UUID.randomUUID();
        var id2 = UUID.randomUUID();
        person1.setId(id1);
        person2.setId(id2);
        setAllPersonsByReflection(List.of(person1, person2));

        var sortedList = getSortedList(List.of(person1, person2), ASCENDING, PersonSortingOptions.SortField.ID);
        var response = this.mvc.perform(
                        get("/persons")
                                .contentType("application/json")).andReturn().getResponse();

        if (response.getStatus() == 404 || response.getStatus() == 405) {
            fail("The endpoint GET /persons has not been implemented.");
        }
        assertEquals(200, response.getStatus(), "PersonResource::getAllPersons did not return the correct status code.");
        var respondedPersons = objectMapper.readValue(response.getContentAsString(), Person[].class);
        if (respondedPersons.length != 2) {
            fail("PersonResource::getAllPersons did not return the correct amount of persons.");
        }
	    var sortedRespondedPersons = getSortedList(List.of(respondedPersons), ASCENDING, PersonSortingOptions.SortField.ID);
	    for (int i = 0; i < sortedRespondedPersons.size(); i++){
            if (!checkIfPersonEqual(sortedList.get(i), sortedRespondedPersons.get(i), false)) {
                fail("PersonResource::getAllPersons did not contain the correct person/correct order as response body when performing a request without sorting options.");
            }
        }
    }

    private static List<Person> getSortedList(List<Person> persons, PersonSortingOptions.SortingOrder sortingOrder, PersonSortingOptions.SortField sortField) {
        var sortedList = new ArrayList<>(persons);
        sortedList.sort((p1, p2) -> {
            Person person1;
            Person person2;
            if (sortingOrder == ASCENDING) {
                person1 = p1;
                person2 = p2;
            } else {
                person1 = p2;
                person2 = p1;
            }

            return switch (sortField) {
                case ID -> person1.getId().compareTo(person2.getId());
                case FIRST_NAME -> person1.getFirstName().compareTo(person2.getFirstName());
                case LAST_NAME -> person1.getLastName().compareTo(person2.getLastName());
                case BIRTHDAY -> person1.getBirthday().compareTo(person2.getBirthday());
            };
        });

        return sortedList;
    }

    public static void setAllPersonsByReflection(List<Person> personList) {
        Field persons;
        Object fieldValue;
        List<Person> reflectedPersonList;
        try {
            persons = PersonService.class.getDeclaredField("persons");
            persons.setAccessible(true);

            fieldValue = persons.get(personService);
            if (!(fieldValue instanceof List)) {
                fail("The attribute 'persons' in class 'PersonResource' has not the correct type.");
            }

            reflectedPersonList = (List<Person>) fieldValue;
        } catch (NoSuchFieldException | IllegalAccessException e) {
            fail("The attribute 'persons' in class 'PersonResource' has not been implemented as described.");
            return;
        }
        try {
            reflectedPersonList.removeIf(p -> true);
            reflectedPersonList.addAll(personList);
        } catch (Exception e) {
            fail("An unexpected error has occurred. Contact your tutor.");
        }
    }

    public static List<Person> getAllPersonsByReflection() {
        try {
            Field persons = PersonService.class.getDeclaredField("persons");
            persons.setAccessible(true);

            Object fieldValue = persons.get(personService);

            if (!(fieldValue instanceof List)) {
                fail("The attribute 'persons' in class 'PersonService' has not the correct type.");
            }
            return (List<Person>) fieldValue;
        } catch (NoSuchFieldException | IllegalAccessException e) {
            fail("The attribute 'persons' in class 'PersonService' has not been implemented as described.");
            return null;
        }
    }
}
