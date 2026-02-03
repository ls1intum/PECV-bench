package de.tum.in.ase.eist;

import org.junit.jupiter.api.*;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.web.reactive.function.client.WebClient;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.assertj.core.api.Assertions.*;

import de.tum.in.ase.eist.model.Person;
import org.springframework.web.reactive.function.client.WebClientResponseException;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class HerokuTest {
    private static boolean skipRemainingTests = false;

    private String appName;
    private URI baseUri;
    private HttpClient httpClient;
    private WebClient webClient;

    @BeforeEach
    public void init() throws IOException {
      	if (skipRemainingTests) {
         	fail("Skipped due to previous test failure");
        }

        var path = Paths.get("./assignment/heroku-app-name.txt");
        var lines = Files.readAllLines(path);
        if (lines.size() >= 1) {
            this.appName = lines.get(0);
        }
        this.baseUri = URI.create("https://" + appName + ".herokuapp.com");
        this.httpClient = HttpClient.newBuilder()
                .build();

        this.webClient = WebClient.builder()
                .baseUrl("https://" + appName + ".herokuapp.com")
                .defaultHeader(HttpHeaders.ACCEPT, MediaType.APPLICATION_JSON_VALUE)
                .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .build();
    }

    @Test
    @DisplayName("App name was set")
    @Order(1)
    public void testAppName() {
        if (appName == null || appName.isBlank()) {
            skipRemainingTests = true;
            fail("App name was not set");
        }
    }

    @Test
    @DisplayName("App exists on Heroku")
    @Order(2)
    public void testAppExists() throws IOException, InterruptedException {
        var request = HttpRequest.newBuilder().GET()
                .uri(baseUri)
                .timeout(Duration.ofMinutes(1))
                .build();
        var response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.body().contains("www.herokucdn.com/error-pages/no-such-app.html")) {
            skipRemainingTests = true;
            fail("App '" + appName + "' does not exist on Heroku");
        }
    }

    @Test
    @DisplayName("Dockerfile was adapted")
    @Order(3)
    public void testDockerfile() {
        var path = Paths.get("./assignment/Dockerfile");
        List<String> lines = null;
        try {
            lines = Files.readAllLines(path);
        } catch (IOException e) {
            fail("Dockerfile could not be read (does it exist?)");
        }

        if (!contains(lines, "\\s*FROM\\s+openjdk:17-bullseye\\s*")) {
            skipRemainingTests = true;
            fail("Dockerfile is missing the correct image");
        }
        if (!contains(lines, "\\s*WORKDIR\\s+/app\\s*")) {
            skipRemainingTests = true;
            fail("Dockerfile is missing the correct WORKDIR statement");
        }
       if (!contains(lines, "\\s*COPY\\s+(\\./)?build/libs/.+\\s+(\\./)?app\\.jar\\s*")) {
            skipRemainingTests = true;
            fail("Dockerfile is missing the correct statement to copy the application Jar");
        }
        if (!contains(lines, "\\s*COPY\\s+(\\./)?start\\.sh\\s+(((\\./)?start\\.sh)|(\\.))\\s*")) {
            skipRemainingTests = true;
            fail("Dockerfile is missing the correct statement to copy the start.sh file");
        }
        if (!contains(lines, "\\s*CMD\\s+(\\./)?start.sh\\s*")) {
            skipRemainingTests = true;
            fail("Dockerfile is missing the correct CMD statement");
        }
    }

    @Test
    @DisplayName("build.sh or build.bat was adapted")
    @Order(4)
    public void testBuildFile() {
        var path1 = Paths.get("./assignment/build.sh");
        var path2 = Paths.get("./assignment/build.bat");
        Set<String> linesSet = new HashSet<>();
        boolean oneFileRead = false;
        try {
            List<String> lines1 = Files.readAllLines(path1);
            linesSet.addAll(lines1);
            oneFileRead = true;
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            List<String> lines2 = Files.readAllLines(path2);
            linesSet.addAll(lines2);
            oneFileRead = true;
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (!oneFileRead) {
            fail("build.sh/build.bat could not be read");
        }
        List<String> lines = new ArrayList<>(linesSet);

        if (!contains(lines, "\\s*(call )?(\\./)?gradlew( clean)? build\\s*")) {
            skipRemainingTests = true;
            fail("build.sh/build.bat is missing a correct command to build the Spring Boot application with Gradle");
        }
        if (!contains(lines, "\\s*(call )?docker build( .+)? \\.\\s*") &&
                !contains(lines, "\\s*(call )?docker buildx build( .+)? \\.\\s*")) {
            skipRemainingTests = true;
            fail("build.sh/build.bat is missing a correct command to build the Docker image");
        }
        if (!contains(lines, "\\s*(call )?docker push registry\\.heroku\\.com/" + appName + "/web\\s*")) {
            skipRemainingTests = true;
            fail("build.sh/build.bat is missing a correct command to push the image to heroku");
        }
        if (!contains(lines, "\\s*(call )?heroku container:release web( -a " + appName + ")?\\s*")) {
            skipRemainingTests = true;
            fail("build.sh/build.bat is missing a correct command to release the image on heroku");
        }
    }

    private boolean contains(List<String> lines, String searchedLine) {
        for (String line : lines) {
            if (line.matches(searchedLine)) {
                return true;
            }
        }
        return false;
    }

    @Test
    @DisplayName("Test running inside Docker")
    @Order(12)
    public void testInsideDocker() throws IOException, InterruptedException {
        var request = HttpRequest.newBuilder().GET()
                .uri(baseUri.resolve("/testing/structure"))
                .header("Accept", "application/json")
                .header("Content-Type", "application/json")
                .timeout(Duration.ofMinutes(1))
                .build();
        var response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        if (!response.body().contains("start.sh") &&
                !response.body().contains("jdbc.sh") &&
                !response.body().contains("app.jar") &&
                !response.body().contains(".wget-hsts")) {
            skipRemainingTests = true;
            fail("Your application is not running inside Docker");
        }
    }

    @Test
    @DisplayName("App has access to Postgres")
    @Order(20)
    public void testDatabase1() throws IOException, InterruptedException {
        var request = HttpRequest.newBuilder().GET()
                .uri(baseUri.resolve("/testing/url"))
                .header("Accept", "application/json")
                .header("Content-Type", "application/json")
                .timeout(Duration.ofMinutes(1))
                .build();
        var response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        if (!response.body().startsWith("jdbc:postgresql://")) {
            skipRemainingTests = true;
            fail("Database was not added correctly in Heroku");
        }
    }

    @Test
    @DisplayName("Endpoints work correctly")
    @Order(21)
    public void testEndpoints() {
        skipRemainingTests = true;
        var person1 = createPerson("Max", "Mustermann", LocalDate.of(2000, 1, 1));
        var person2 = createPerson("Hans", "Mustermann", LocalDate.of(1989, 4, 23));
        var person3 = createPerson("Anna", "Musterfrau", LocalDate.of(1700, 12, 31));
        var person4 = createPerson("Grete", "Musterfrau", LocalDate.of(2022, 6, 10));
        var savedPerson1 = addPerson(person1);
        var savedPerson2 = addPerson(person2);
        var savedPerson3 = addPerson(person3);
        var savedPerson4 = addPerson(person4);

        try {
            assertThat(savedPerson1).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person1);
            assertThat(savedPerson2).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person2);
            assertThat(savedPerson3).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person3);
            assertThat(savedPerson4).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person4);

            var allPersons = getAllPersons();
            assertThat(allPersons).as("Persons were not retrieved correctly").contains(savedPerson1, savedPerson2, savedPerson3, savedPerson4);
        } finally {
            deletePerson(savedPerson1);
            deletePerson(savedPerson2);
            deletePerson(savedPerson3);
            deletePerson(savedPerson4);
        }

        var allPersons = getAllPersons();
        assertThat(allPersons).as("Persons were not deleted correctly").doesNotContain(savedPerson1, savedPerson2, savedPerson3, savedPerson4);
        skipRemainingTests = false;
    }

    @Test
    @DisplayName("App uses Postgres")
    @Order(22)
    public void testDatabase2() throws IOException, InterruptedException {
        // Add Persons
        var person1 = createPerson("Max", "Mustermann", LocalDate.of(2000, 1, 1));
        var person2 = createPerson("Hans", "Mustermann", LocalDate.of(1989, 4, 23));
        var person3 = createPerson("Anna", "Musterfrau", LocalDate.of(1700, 12, 31));
        var person4 = createPerson("Grete", "Musterfrau", LocalDate.of(2022, 6, 10));
        var savedPerson1 = addPerson(person1);
        var savedPerson2 = addPerson(person2);
        var savedPerson3 = addPerson(person3);
        var savedPerson4 = addPerson(person4);

        // Restart
        var request1 = HttpRequest.newBuilder().GET()
                .uri(baseUri.resolve("/testing/restart"))
                .header("Accept", "application/json")
                .header("Content-Type", "application/json")
                .timeout(Duration.ofMinutes(1))
                .build();
        httpClient.send(request1, HttpResponse.BodyHandlers.discarding());

        // Wait for restart
        var request2 = HttpRequest.newBuilder().GET()
                .uri(baseUri)
                .header("Accept", "application/json")
                .header("Content-Type", "application/json")
                .timeout(Duration.ofMinutes(1))
                .build();
        httpClient.send(request2, HttpResponse.BodyHandlers.ofString());

        // Get Persons
        var allPersons = getAllPersons();
        assertThat(allPersons).as("Persons were not saved in the database properly").contains(savedPerson1, savedPerson2, savedPerson3, savedPerson4);

        deletePerson(savedPerson1);
        deletePerson(savedPerson2);
        deletePerson(savedPerson3);
        deletePerson(savedPerson4);
    }

    @Test
    @DisplayName("New Endpoints work correctly")
    @Order(31)
    public void testNewEndpoints1() {
        skipRemainingTests = true;
        var person1 = createPerson("Max", "Mustermann", LocalDate.of(2000, 1, 1));
        var person2 = createPerson("Hans", "Mustermann", LocalDate.of(1989, 4, 23));
        var person3 = createPerson("Anna", "Musterfrau", LocalDate.of(1700, 12, 31));
        var person4 = createPerson("Grete", "Musterfrau", LocalDate.of(2022, 6, 10));
        var savedPerson1 = addPerson(person1);
        var savedPerson2 = addPerson(person2);
        var savedPerson3 = addPerson(person3);
        var savedPerson4 = addPerson(person4);

        try {
            assertThat(savedPerson1).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person1);
            assertThat(savedPerson2).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person2);
            assertThat(savedPerson3).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person3);
            assertThat(savedPerson4).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person4);

            savedPerson1 = addParent(savedPerson1, savedPerson2);
            savedPerson1 = addParent(savedPerson1, savedPerson3);
            final Person finalSavedPerson = savedPerson1;
            assertThatExceptionOfType(WebClientResponseException.class)
                    .as("A person can only have 2 parents")
                    .isThrownBy(() -> addParent(finalSavedPerson, savedPerson4))
                    .matches(e -> e.getStatusCode() == HttpStatus.BAD_REQUEST, "Status code is not correct");

            assertThatExceptionOfType(WebClientResponseException.class)
                    .as("A person can only have 2 parents")
                    .isThrownBy(() -> addChild(savedPerson4, finalSavedPerson))
                    .matches(e -> e.getStatusCode() == HttpStatus.BAD_REQUEST, "Status code is not correct");

            assertThat(savedPerson1).as("Parent was not added correctly").isNotNull();
            assertThat(savedPerson1.getParents()).as("Parent was not added correctly").containsExactlyInAnyOrder(savedPerson2, savedPerson3);
        } finally {
            deletePerson(savedPerson1);
            deletePerson(savedPerson2);
            deletePerson(savedPerson3);
            deletePerson(savedPerson4);
        }

        var allPersons = getAllPersons();
        assertThat(allPersons).as("Persons were not deleted correctly").doesNotContain(savedPerson1, savedPerson2, savedPerson3, savedPerson4);
        skipRemainingTests = false;
    }

    @Test
    @DisplayName("New Endpoints work correctly 2")
    @Order(32)
    public void testNewEndpoints2() {
        skipRemainingTests = true;
        var person1 = createPerson("Max", "Mustermann", LocalDate.of(2000, 1, 1));
        var person2 = createPerson("Hans", "Mustermann", LocalDate.of(1989, 4, 23));
        var person3 = createPerson("Anna", "Musterfrau", LocalDate.of(1700, 12, 31));
        var person4 = createPerson("Grete", "Musterfrau", LocalDate.of(2022, 6, 10));
        var savedPerson1 = addPerson(person1);
        var savedPerson2 = addPerson(person2);
        var savedPerson3 = addPerson(person3);
        var savedPerson4 = addPerson(person4);

        try {
            assertThat(savedPerson1).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person1);
            assertThat(savedPerson2).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person2);
            assertThat(savedPerson3).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person3);
            assertThat(savedPerson4).as("Person was not saved correctly").isNotNull().usingRecursiveComparison().ignoringFields("id").isEqualTo(person4);

            savedPerson1 = addChild(savedPerson1, savedPerson3);
            savedPerson1 = addChild(savedPerson1, savedPerson4);
            savedPerson2 = addChild(savedPerson2, savedPerson3);
            savedPerson2 = addChild(savedPerson2, savedPerson4);

            assertThat(savedPerson1).as("Child was not added correctly").isNotNull();
            assertThat(savedPerson1.getChildren()).as("Child was not added correctly").containsExactlyInAnyOrder(savedPerson3, savedPerson4);
            assertThat(savedPerson2).as("Child was not added correctly").isNotNull();
            assertThat(savedPerson2.getChildren()).as("Child was not added correctly").containsExactlyInAnyOrder(savedPerson3, savedPerson4);
        } finally {
            deletePerson(savedPerson1);
            deletePerson(savedPerson2);
            deletePerson(savedPerson3);
            deletePerson(savedPerson4);
        }

        var allPersons = getAllPersons();
        assertThat(allPersons).as("Persons were not deleted correctly").doesNotContain(savedPerson1, savedPerson2, savedPerson3, savedPerson4);
        skipRemainingTests = false;
    }

    public Person addPerson(Person person) {
        return webClient.post()
                .uri("persons")
                .bodyValue(person)
                .retrieve()
                .bodyToMono(Person.class)
                .onErrorStop()
                .block(Duration.ofMinutes(1));
    }

    public Person addParent(Person person, Person parent) {
        return webClient.put()
                .uri("persons/" + person.getId() + "/parents")
                .bodyValue(parent)
                .retrieve()
                .bodyToMono(Person.class)
                .onErrorStop()
                .block(Duration.ofMinutes(1));
    }

    public Person addChild(Person person, Person child) {
        return webClient.put()
                .uri("persons/" + person.getId() + "/children")
                .bodyValue(child)
                .retrieve()
                .bodyToMono(Person.class)
                .onErrorStop()
                .block(Duration.ofMinutes(1));
    }

    public Person updatePerson(Person person) {
        return webClient.put()
                .uri("persons/" + person.getId())
                .bodyValue(person)
                .retrieve()
                .bodyToMono(Person.class)
                .onErrorStop()
                .block(Duration.ofMinutes(1));
    }

    public void deletePerson(Person person) {
        webClient.delete()
                .uri("persons/" + person.getId())
                .retrieve()
                .toBodilessEntity()
                .onErrorStop()
                .block(Duration.ofMinutes(1));
    }

    public List<Person> getAllPersons() {
        return webClient.get()
                .uri("persons")
                .retrieve()
                .bodyToMono(new ParameterizedTypeReference<List<Person>>() {})
                .onErrorStop()
                .block(Duration.ofMinutes(1));
    }
    
    public Person createPerson(String firstName, String lastName, LocalDate birthDay) {
        Person person = new Person();
        person.setFirstName(firstName);
        person.setLastName(lastName);
        person.setBirthday(birthDay);
        return person;
    }
}
