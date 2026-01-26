package de.tum.in.ase.eist;

import de.tum.in.ase.eist.model.Person;
import de.tum.in.ase.eist.repository.PersonRepository;
import de.tum.in.ase.eist.service.PersonService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.web.server.ResponseStatusException;

import java.time.LocalDate;
import java.util.Set;

import static org.assertj.core.api.Assertions.assertThatExceptionOfType;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT)
@AutoConfigureTestDatabase
@DirtiesContext(classMode = DirtiesContext.ClassMode.BEFORE_EACH_TEST_METHOD)
class PersonServiceTest {

    @Autowired
    private PersonService personService;

    @Autowired
    private PersonRepository personRepository;

    @Test
    void testAddPerson() {
        var person = new Person();
        person.setFirstName("Max");
        person.setLastName("Mustermann");
        person.setBirthday(LocalDate.now());

        // in an integration test, we would invoke the corresponding REST endpoint here
        personService.save(person);

        assertEquals(1, personRepository.findAll().size());
    }

    @Test
    void testDeletePerson() {
        var person = new Person();
        person.setFirstName("Max");
        person.setLastName("Mustermann");
        person.setBirthday(LocalDate.now());

        person = personRepository.save(person);

        // in an integration test, we would invoke the corresponding REST endpoint here
        personService.delete(person);

        assertTrue(personRepository.findAll().isEmpty());
    }

    @Test
    void testAddParent() {
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
        personService.addParent(child, parent);

        parent = personRepository.findWithParentsAndChildrenById(parent.getId()).orElseThrow();
        child = personRepository.findWithParentsAndChildrenById(child.getId()).orElseThrow();
        assertEquals(Set.of(child), parent.getChildren());
        assertEquals(Set.of(parent), child.getParents());
    }

    @Test
    void testAddThreeParents() {
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

        child = personService.addParent(child, parent1);
        child = personService.addParent(child, parent2);
        Person finalChild = child;
        Person finalParent = parent3;
        assertThatExceptionOfType(ResponseStatusException.class).isThrownBy(() -> personService.addParent(finalChild, finalParent))
                .matches(e -> e.getStatusCode() == HttpStatus.BAD_REQUEST);

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
