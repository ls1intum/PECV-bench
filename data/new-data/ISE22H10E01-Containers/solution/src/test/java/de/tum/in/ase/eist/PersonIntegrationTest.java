package de.tum.in.ase.eist;

import com.fasterxml.jackson.databind.ObjectMapper;
import de.tum.in.ase.eist.model.Person;
import de.tum.in.ase.eist.repository.PersonRepository;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.web.servlet.MockMvc;

import java.time.LocalDate;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT)
@AutoConfigureTestDatabase
@DirtiesContext(classMode = DirtiesContext.ClassMode.BEFORE_EACH_TEST_METHOD)
@AutoConfigureMockMvc
class PersonIntegrationTest {
    @Autowired
    private MockMvc mvc;

    @Autowired
    private PersonRepository personRepository;

    private static ObjectMapper objectMapper;

    @BeforeAll
    static void setup() {
        objectMapper = new ObjectMapper();
        objectMapper.findAndRegisterModules();
    }

    @Test
    void testAddPerson() throws Exception {
        var person = new Person();
        person.setFirstName("Max");
        person.setLastName("Mustermann");
        person.setBirthday(LocalDate.now());

        var response = this.mvc.perform(
                post("/persons")
                        .content(objectMapper.writeValueAsString(person))
                        .contentType("application/json")
        ).andReturn().getResponse();


        assertEquals(HttpStatus.OK.value(), response.getStatus());
        assertEquals(1, personRepository.findAll().size());
    }

    @Test
    void testDeletePerson() throws Exception {
        var person = new Person();
        person.setFirstName("Max");
        person.setLastName("Mustermann");
        person.setBirthday(LocalDate.now());

        person = personRepository.save(person);

        var response = this.mvc.perform(
                delete("/persons/" + person.getId())
                        .contentType("application/json")
        ).andReturn().getResponse();

        assertEquals(HttpStatus.NO_CONTENT.value(), response.getStatus());
        assertTrue(personRepository.findAll().isEmpty());
    }

    @Test
    void testAddParent() throws Exception {
        var parent = new Person();
        parent.setFirstName("Max");
        parent.setLastName("Mustermann");
        parent.setBirthday(LocalDate.of(1900, 1, 1));

        var child = new Person();
        child.setFirstName("Anna");
        child.setLastName("Musterkind");
        child.setBirthday(LocalDate.now());

        parent = personRepository.save(parent);
        child = personRepository.save(child);

        var response = this.mvc.perform(
                put("/persons/" + child.getId() + "/parents")
                        .content(objectMapper.writeValueAsString(parent))
                        .contentType("application/json")
        ).andReturn().getResponse();

        assertEquals(HttpStatus.OK.value(), response.getStatus());
        parent = personRepository.findWithParentsAndChildrenById(parent.getId()).orElseThrow();
        child = personRepository.findWithParentsAndChildrenById(child.getId()).orElseThrow();
        assertEquals(Set.of(child),parent.getChildren());
        assertEquals(Set.of(parent), child.getParents());
    }

    @Test
    void testAddThreeParents() throws Exception {
        var parent1 = new Person();
        parent1.setFirstName("Max");
        parent1.setLastName("Mustermann1");
        parent1.setBirthday(LocalDate.of(1900, 1, 1));
        var parent2 = new Person();
        parent2.setFirstName("Max");
        parent2.setLastName("Mustermann2");
        parent2.setBirthday(LocalDate.of(1900, 1, 1));
        var parent3 = new Person();
        parent3.setFirstName("Max");
        parent3.setLastName("Mustermann3");
        parent3.setBirthday(LocalDate.of(1900, 1, 1));

        var child = new Person();
        child.setFirstName("Anna");
        child.setLastName("Musterkind");
        child.setBirthday(LocalDate.now());

        parent1 = personRepository.save(parent1);
        parent2 = personRepository.save(parent2);
        parent3 = personRepository.save(parent3);
        child = personRepository.save(child);

        var response1 = this.mvc.perform(
                put("/persons/" + child.getId() + "/parents")
                        .content(objectMapper.writeValueAsString(parent1))
                        .contentType("application/json")
        ).andReturn().getResponse();
        var response2 = this.mvc.perform(
                put("/persons/" + child.getId() + "/parents")
                        .content(objectMapper.writeValueAsString(parent2))
                        .contentType("application/json")
        ).andReturn().getResponse();
        var response3 = this.mvc.perform(
                put("/persons/" + child.getId() + "/parents")
                        .content(objectMapper.writeValueAsString(parent3))
                        .contentType("application/json")
        ).andReturn().getResponse();

        assertEquals(HttpStatus.OK.value(), response1.getStatus());
        assertEquals(HttpStatus.OK.value(), response2.getStatus());
        assertEquals(HttpStatus.BAD_REQUEST.value(), response3.getStatus());
        parent1 = personRepository.findWithParentsAndChildrenById(parent1.getId()).orElseThrow();
        parent2 = personRepository.findWithParentsAndChildrenById(parent2.getId()).orElseThrow();
        parent3 = personRepository.findWithParentsAndChildrenById(parent3.getId()).orElseThrow();
        child = personRepository.findWithParentsAndChildrenById(child.getId()).orElseThrow();
        assertEquals(Set.of(child), parent1.getChildren());
        assertEquals(Set.of(child), parent2.getChildren());
        assertTrue(parent3.getChildren().isEmpty());
        assertEquals(Set.of(parent1, parent2), child.getParents());
    }
}
