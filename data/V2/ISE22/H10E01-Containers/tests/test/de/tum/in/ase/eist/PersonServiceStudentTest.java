package de.tum.in.ase.eist;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

import de.tum.in.ase.eist.model.Person;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.web.server.ResponseStatusException;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.HashSet;
import java.util.List;

import de.tum.in.ase.eist.service.PersonService;
import de.tum.in.ase.eist.repository.PersonRepository;

@ExtendWith(MockitoExtension.class)
public class PersonServiceStudentTest {
    private PersonService service;

    @Mock
    private PersonRepository repositoryMock;

    private Person person;

    @BeforeEach
    public void init() {
        this.service = new PersonService(repositoryMock);
        person = new Person();
        person.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
    }

    @Test
    public void addParentThrows() {
        Person parent1 = new Person();
        parent1.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        Person parent2 = new Person();
        parent2.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        parent2.setFirstName("no-duplicate");
        person.setParents(new HashSet<>(List.of(parent1, parent2)));

        Person parent3 = new Person();
        parent3.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));

        checkCorrectResponseException(() -> service.addParent(person, parent3), "PersonService::addParent", "PersonService::addParent should throw an exception if the person already has more than one parent.");
    }

    @Test
    public void addParent() {
        Person parent1 = new Person();
        parent1.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        Person parent2 = new Person();
        parent2.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        parent2.setFirstName("no-duplicate");

        assertDoesNotThrow(() -> service.addParent(person, parent1), "PersonService::addParent should succeed but failed with an exception.");
        assertThat(person.getParents()).withFailMessage("PersonService::addParent did not add the parent to the child' parents.").hasSize(1);
        verify(repositoryMock, times(1)).save(person);

        assertDoesNotThrow(() -> service.addParent(person, parent2), "PersonService::addParent should succeed but failed with an exception.");
        assertThat(person.getParents()).withFailMessage("PersonService::addParent did not add the parent to the child' parents.").hasSize(2);
        verify(repositoryMock, times(2)).save(person);
    }

    @Test
    public void addChildThrows() {
        Person parent1 = new Person();
        parent1.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        Person parent2 = new Person();
        parent2.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        parent2.setFirstName("no-duplicate");
        person.setParents(new HashSet<>(List.of(parent1, parent2)));

        Person parent3 = new Person();
        parent3.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));

        checkCorrectResponseException(() -> service.addChild(parent3, person), "PersonService::addChild", "PersonService::addChild should throw an exception if the person already has more than one parent.");
    }

    @Test
    public void addChild() {
        Person parent = new Person();
        parent.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        Person child2 = new Person();
        child2.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        child2.setFirstName("no-duplicate");

        assertDoesNotThrow(() -> service.addChild(parent, person), "PersonService::addChild should succeed but failed with an exception.");
        assertThat(parent.getChildren()).withFailMessage("PersonService::addChild did not add the parent to the parent's children.").hasSize(1);
        verify(repositoryMock, times(1)).save(parent);

        assertDoesNotThrow(() -> service.addChild(parent, child2), "PersonService::addChild should succeed but failed with an exception.");
        assertThat(parent.getChildren()).withFailMessage("PersonService::addChild did not add the parent to the parent's children.").hasSize(2);
        verify(repositoryMock, times(2)).save(parent);
    }

    @Test
    public void removeParentThrows() {
        Person parent1 = new Person();
        parent1.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        person.setParents(new HashSet<>(List.of(parent1)));

        checkCorrectResponseException(() -> service.removeParent(person, parent1), "PersonService::removeParent", "PersonService::removeParent should throw an exception if the person has only one parent.");
    }

    @Test
    public void removeParent() {
        Person parent1 = new Person();
        parent1.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        Person parent2 = new Person();
        parent2.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        parent2.setFirstName("no-duplicate");

        person.setParents(new HashSet<>(List.of(parent1, parent2)));

        assertDoesNotThrow(() -> service.removeParent(person, parent1), "PersonService::removeParent should succeed but failed with an exception.");
        assertThat(person.getParents()).withFailMessage("PersonService::removeParent did not remove the parent from the children's parents.").hasSize(1);
        verify(repositoryMock, times(1)).save(person);
    }

    @Test
    public void removeChildThrows() {
        Person child = new Person();
        child.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        child.setParents(new HashSet<>(List.of(person)));

        checkCorrectResponseException(() -> service.removeChild(person, child), "PersonService::removeChild", "PersonService::removeChild should throw an exception if the child has only one parent.");
    }

    @Test
    public void removeChild() {
        Person parent1 = new Person();
        parent1.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        parent1.setChildren(new HashSet<>(List.of(person)));
        Person parent2 = new Person();
        parent2.setBirthday(LocalDate.now().minus(2, ChronoUnit.YEARS));
        parent2.setFirstName("no-duplicate");
        parent2.setChildren(new HashSet<>(List.of(person)));

        person.setParents(new HashSet<>(List.of(parent1, parent2)));

        assertDoesNotThrow(() -> service.removeChild(parent1, person), "PersonService::removeChild should succeed but failed with an exception.");
        assertThat(parent1.getChildren()).withFailMessage("PersonService::removeChild did not remove the child from the parent's children.").hasSize(0);
        verify(repositoryMock, times(1)).save(parent1);
    }

    private void checkCorrectResponseException(Runnable method, String methodName, String errorMessage) {
        Exception exception = null;
        try {
            method.run();
        } catch (Exception e) {
            exception = e;
        }

        if (exception == null) {
            fail(errorMessage);
        }
        assertNotNull(exception, errorMessage);
        if (!(exception instanceof ResponseStatusException)) {
            fail(String.format("%s throws an exception of the wrong type.", methodName));
        }
        assertEquals(400, ((ResponseStatusException) exception).getStatusCode().value(), String.format("%s throws an ResponseStatusException with a wrong status code", methodName));
    }
}
