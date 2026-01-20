package de.tum.in.ase.eist;

import static de.tum.in.ase.eist.H05E01Client.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import com.fasterxml.jackson.databind.ObjectMapper;
import de.tum.in.ase.eist.model.Person;
import de.tum.in.ase.eist.util.PersonSortingOptions;
import okhttp3.mockwebserver.MockResponse;
import okhttp3.mockwebserver.MockWebServer;
import okhttp3.mockwebserver.RecordedRequest;
import org.junit.jupiter.api.*;
import org.mockito.ArgumentCaptor;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.function.Consumer;
import java.util.concurrent.TimeUnit;

@H05E01
public class PersonControllerTest {

    private static MockWebServer mockWebServer;
    private static ObjectMapper objectMapper;

    private Object personController;
    private Person person1;
    private Person person2;

    @BeforeAll
    static void setUp() {
        objectMapper = new ObjectMapper();
        objectMapper.findAndRegisterModules();
    }

    @BeforeEach
    void initialize() throws Exception {
        // restarting the server for every test is required because otherwise tests interfere with each other
        mockWebServer = new MockWebServer();
        mockWebServer.start(8080);
        personController = createPersonController();

        person1 = new Person();
        var uuid1 = UUID.randomUUID();
        person1.setId(uuid1);
        person1.setFirstName("Max");
        person1.setLastName("Musterfrau");
        person1.setBirthday(LocalDate.ofYearDay(2000, 125));

        person2 = new Person();
        var uuid2 = UUID.randomUUID();
        person2.setId(uuid2);
        person2.setFirstName("Erika");
        person2.setLastName("Mustermann");
        person2.setBirthday(LocalDate.ofYearDay(1999, 80));
    }

    @AfterEach
    void afterEach() throws Exception {
        mockWebServer.shutdown();
    }

    @Test
    @DisplayName("Add single valid persons (Client)")
    public void testAddSingleValidPerson() throws Exception {
        testAddPerson(200, person1, List.of(person1));
    }

    @Test
    @DisplayName("Add multiple valid persons (Client)")
    public void testAddMultipleValidPersons() throws Exception {
        testAddPerson(200, person1, new ArrayList<>(List.of(person1)));
        testAddPerson(200, person2, new ArrayList<>(List.of(person1, person2)));
    }

    @Test
    @DisplayName("Add single invalid person (Client)")
    public void testAddInvalidPerson() throws Exception {
        mockWebServer.enqueue(new MockResponse()
                .setResponseCode(400)
                .setHeader("Content-Type", "application/json"));
        Consumer<List<Person>> consumer = mock(Consumer.class);

        invokeAddPerson(personController, person1, consumer);

        // wait until the result has been processed by the client (100ms should be enough, just to be sure)
        Thread.sleep(350);
        if(mockWebServer.getRequestCount() == 0) {
            fail("PersonController::createPerson did not send a request.");
        }

        verify(consumer, never()).accept(any());
    }

    @Test
    @DisplayName("Edit single person (Client)")
    public void testEditSinglePerson() throws Exception {
        Person updatedPerson = new Person();
        updatedPerson.setId(person1.getId());
        updatedPerson.setFirstName(person1.getFirstName());
        updatedPerson.setLastName("Updated Last Name");
        updatedPerson.setBirthday(person1.getBirthday());

        setPersonControllerPersons(personController, new ArrayList<>(List.of(person1)));

        testUpdatePerson(200, updatedPerson, List.of(updatedPerson));
    }

    @Test
    @DisplayName("Edit single person for multiple existing persons (Client)")
    public void testEditSinglePersonForMultipleExistingPersons() throws Exception {
        Person updatedPerson = new Person();
        updatedPerson.setId(person1.getId());
        updatedPerson.setFirstName(person1.getFirstName());
        updatedPerson.setLastName("Updated Last Name");
        updatedPerson.setBirthday(person1.getBirthday());

        setPersonControllerPersons(personController, new ArrayList<>(List.of(person1, person2)));

        testUpdatePerson(200, updatedPerson, List.of(updatedPerson, person2));
    }

    @Test
    @DisplayName("Edit invalid person (Client)")
    public void testEditInvalidPerson() throws Exception {
        setPersonControllerPersons(personController, new ArrayList<>(List.of(person1, person2)));

        mockWebServer.enqueue(new MockResponse()
                .setResponseCode(400)
                .setHeader("Content-Type", "application/json"));
        Consumer<List<Person>> consumer = mock(Consumer.class);

        invokeUpdatePerson(personController, person1, consumer);

        // wait until the result has been processed by the client (100ms should be enough, just to be sure)
        Thread.sleep(350);
        if(mockWebServer.getRequestCount() == 0) {
            fail("PersonController::updatePerson did not send a request.");
        }
        verify(consumer, times(0));
    }

    @Test
    @DisplayName("Delete existing person 1 (Client)")
    public void testDeleteOnlyExistingPerson() throws Exception {
        setPersonControllerPersons(personController, new ArrayList<>(List.of(person1)));

        testDeletePerson(200, person1, List.of());
    }

    @Test
    @DisplayName("Delete existing person 2 (Client)")
    public void testDeletePerson() throws Exception {
        setPersonControllerPersons(personController, new ArrayList<>(List.of(person1, person2)));

        testDeletePerson(200, person1, List.of(person2));
    }

    @Test
    @DisplayName("Retrieve all persons 1 (Client)")
    public void testGetAllPerson() throws Exception {
        setPersonControllerPersons(personController, new ArrayList<>(List.of(person1, person2)));

        var sortingOptions = new PersonSortingOptions();
        sortingOptions.setSortField(PersonSortingOptions.SortField.ID);
        sortingOptions.setSortingOrder(PersonSortingOptions.SortingOrder.ASCENDING);

        testGetAllPersons(200, sortingOptions, List.of(person2, person1));
    }

    @Test
    @DisplayName("Retrieve all persons 2 (Client)")
    public void testGetAllPersonsResetsSavedResult() throws Exception {
        setPersonControllerPersons(personController, new ArrayList<>(List.of(person1, person2)));

        var sortingOptions = new PersonSortingOptions();

        sortingOptions.setSortField(PersonSortingOptions.SortField.ID);
        sortingOptions.setSortingOrder(PersonSortingOptions.SortingOrder.ASCENDING);

        testGetAllPersons(200, sortingOptions, List.of());
    }

    @Test
    @DisplayName("Sort options for retrieving all persons (Client)")
    public void testSortingOptions() throws Exception {
        for (var sortField : PersonSortingOptions.SortField.values()) {
            for (var sortOrder: PersonSortingOptions.SortingOrder.values()) {
                // this should not be required but leaving out may break some student's submission while this is the
                // real-life behavior
                mockWebServer.enqueue(new MockResponse()
                        .setResponseCode(200)
                        .setBody(objectMapper.writeValueAsString(List.of()))
                        .setHeader("Content-Type", "application/json"));

                var sortOptions = new PersonSortingOptions();
                sortOptions.setSortField(sortField);
                sortOptions.setSortingOrder(sortOrder);
                invokeGetAllPersons(personController, sortOptions, (res) -> {});

	            RecordedRequest recordedRequest = mockWebServer.takeRequest(2000, TimeUnit.MILLISECONDS);
	            if(mockWebServer.getRequestCount() == 0) {
                    fail("PersonController::createPerson did not send a request.");
                }

				Thread.sleep(350);
                assertGetAllPersonRequest(recordedRequest, sortOptions);
            }
        }
    }

    private void testAddPerson(int mockResponseCode, Person person, List<Person> expectedPersons) throws Exception {
        mockWebServer.enqueue(new MockResponse()
                .setResponseCode(mockResponseCode)
                .setBody(objectMapper.writeValueAsString(person))
                .setHeader("Content-Type", "application/json"));
        Consumer<List<Person>> consumer = mock(Consumer.class);
        ArgumentCaptor<List<Person>> argument = ArgumentCaptor.forClass(List.class);

        invokeAddPerson(personController, person, consumer);

        RecordedRequest recordedRequest = mockWebServer.takeRequest(2000, TimeUnit.MILLISECONDS);
        if(mockWebServer.getRequestCount() == 0) {
            fail("PersonController::createPerson did not send a request.");
        }
        Thread.sleep(350);

        verify(consumer, times(1)).accept(argument.capture());
        assertPersonListEquals(expectedPersons, argument.getValue(), "addPerson");

        assertEquals("POST", recordedRequest.getMethod(), "PersonController::createPerson did not send a message with the correct request type");
        assertEquals("/persons", recordedRequest.getPath(), "PersonController::createPerson send a message to the wrong correct endpoint path.");
        assertEquals(objectMapper.writeValueAsString(person), recordedRequest.getBody().readUtf8(), "PersonController::createPerson send a message with the wrong response body.");
    }

    private void testUpdatePerson(int mockResponseCode, Person updatedPerson, List<Person> expectedPersons) throws Exception {
        mockWebServer.enqueue(new MockResponse()
                .setResponseCode(mockResponseCode)
                .setBody(objectMapper.writeValueAsString(updatedPerson))
                .setHeader("Content-Type", "application/json"));
        Consumer<List<Person>> consumer = mock(Consumer.class);
        ArgumentCaptor<List<Person>> argument = ArgumentCaptor.forClass(List.class);

        invokeUpdatePerson(personController, updatedPerson, consumer);

        // wait until the result has been processed by the client (100ms should be enough, just to be sure)
	    RecordedRequest recordedRequest = mockWebServer.takeRequest(2000, TimeUnit.MILLISECONDS);
        if(mockWebServer.getRequestCount() == 0) {
	        fail("PersonController::updatePerson did not send a request.");
        }
	    Thread.sleep(350);

	    verify(consumer, times(1)).accept(argument.capture());
        assertPersonListEquals(expectedPersons, argument.getValue(), "updatePerson");


        assertEquals("PUT", recordedRequest.getMethod(), "PersonController::updatePerson did not send a message with the correct request type.");
        assertEquals("/persons/" + updatedPerson.getId(), recordedRequest.getPath(),"PersonController::updatePerson send a message to the wrong correct endpoint path.");
        assertEquals(objectMapper.writeValueAsString(updatedPerson), recordedRequest.getBody().readUtf8(), "PersonController::createPerson send a message with the wrong response body.");
    }

    private void testDeletePerson(int mockResponseCode, Person deletedPerson, List<Person> expectedPersons) throws Exception {
        mockWebServer.enqueue(new MockResponse()
                .setResponseCode(mockResponseCode)
                .setBody(objectMapper.writeValueAsString(deletedPerson))
                .setHeader("Content-Type", "application/json"));
        Consumer<List<Person>> consumer = mock(Consumer.class);
        ArgumentCaptor<List<Person>> argument = ArgumentCaptor.forClass(List.class);

        invokeDeletePerson(personController, deletedPerson, consumer);

	    RecordedRequest recordedRequest = mockWebServer.takeRequest(2000, TimeUnit.MILLISECONDS);
        if(mockWebServer.getRequestCount() == 0) {
	        fail("PersonController::deletePerson did not send a request.");
        }
	    Thread.sleep(350);

	    verify(consumer, times(1)).accept(argument.capture());
        assertPersonListEquals(expectedPersons, argument.getValue(), "deletePerson");

        assertEquals("DELETE", recordedRequest.getMethod(), "PersonController::deletePerson did not send a message with the correct request type.");
        assertEquals("/persons/" + deletedPerson.getId(), recordedRequest.getPath(),"PersonController::deletePerson send a message to the wrong correct endpoint path.");
        assertEquals("", recordedRequest.getBody().readUtf8(), "PersonController::deletePerson send a message with the wrong response body.");
    }

    private void testGetAllPersons(int mockResponseCode, PersonSortingOptions sortingOptions, List<Person> allPersons) throws Exception {
        mockWebServer.enqueue(new MockResponse()
                .setResponseCode(mockResponseCode)
                .setBody(objectMapper.writeValueAsString(allPersons))
                .setHeader("Content-Type", "application/json"));
        Consumer<List<Person>> consumer = mock(Consumer.class);
        ArgumentCaptor<List<Person>> argument = ArgumentCaptor.forClass(List.class);

        invokeGetAllPersons(personController, sortingOptions, consumer);

	    RecordedRequest recordedRequest = mockWebServer.takeRequest(2000, TimeUnit.MILLISECONDS);
        if(mockWebServer.getRequestCount() == 0) {
	        fail("PersonController::getAllPersons did not send a request.");
        }
	    Thread.sleep(350);

		verify(consumer, times(1)).accept(argument.capture());
        assertPersonListEquals(allPersons, argument.getValue(), "getAllPersons");

        assertGetAllPersonRequest(recordedRequest, null);
    }

    private void assertGetAllPersonRequest(RecordedRequest recordedRequest, PersonSortingOptions sortingOptions) {
        assertEquals("GET", recordedRequest.getMethod(), "PersonController::getAllPersons did not send a message with the correct request type.");
        if (sortingOptions == null) {
            if (!recordedRequest.getPath().startsWith("/persons")) {
                fail("PersonController::getAllPersons send a message to the wrong correct endpoint path.");
            }
        } else {
            if (!recordedRequest.getPath().startsWith("/persons")) {
                fail("PersonController::getAllPersons send a message to the wrong correct endpoint path.");
            }
            if (recordedRequest.getRequestUrl().queryParameterNames().size() != 2 || !recordedRequest.getRequestUrl().queryParameterNames().containsAll(List.of("sortField", "sortingOrder"))) {
                fail("PersonController::getAllPersons send a message without the correct sorting options.");
            }
        }
        assertEquals("", recordedRequest.getBody().readUtf8(), "PersonController::getAllPersons send a message with the wrong response body.");
    }
}
