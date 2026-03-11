package de.tum.in.ase.eist;

import com.fasterxml.jackson.databind.ObjectMapper;
import de.tum.in.ase.eist.model.Person;
import de.tum.in.ase.eist.repository.PersonRepository;
import de.tum.in.ase.eist.service.PersonService;
import org.mockito.invocation.InvocationOnMock;
import org.springframework.context.ApplicationContext;
import org.springframework.http.HttpStatus;
import org.springframework.test.util.ReflectionTestUtils;
import org.springframework.web.server.ResponseStatusException;

import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.Optional;
import java.util.function.Function;

import static de.tum.in.test.api.util.ReflectionTestUtils.getMethod;
import static de.tum.in.test.api.util.ReflectionTestUtils.invokeMethod;
import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.fail;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doAnswer;

public record PersonTestHelper(PersonRepository personRepository,
                               PersonService personService,
                               ApplicationContext applicationContext) {

    public void test_testAddParent(Object testClass, boolean injectObjectMapper) {
        executeTestShouldSucceed(testClass, "testAddParent", injectObjectMapper);
        // simply throw
        executeTestShouldFail(
                testClass,
                "testAddParent",
                "Should fail if PersonService::addParent throws an error.",
                (invocation) -> new ResponseStatusException(HttpStatus.BAD_REQUEST, "Should fail if PersonService::addParent throws an error."),
                injectObjectMapper);
        // not persisted parent-child relation
        executeTestShouldFail(
                testClass,
                "testAddParent",
                "Should fail if PersonService::addParent did not add the parent to the person's parents.",
                (invocation) -> invocation.getArgument(0), injectObjectMapper);
        // not saved to DB
        executeTestShouldFail(
                testClass,
                "testAddParent",
                "Should fail if PersonService::addParent did not save the persons to the database.",
                (invocation) -> {
                    var person = (Person) invocation.getArgument(0);
                    var parent = (Person) invocation.getArgument(1);
                    person.getParents().add(parent);
                    return person;
                }, injectObjectMapper);
    }

    public void test_testAddThreeParents(Object testClass, boolean injectObjectMapper) {
        executeTestShouldSucceed(testClass, "testAddThreeParents", injectObjectMapper);
        // simply throw
        executeTestShouldFail(
                testClass,
                "testAddThreeParents",
                "Should fail if PersonService::addParent throws an error.",
                (invocation) -> new ResponseStatusException(HttpStatus.BAD_REQUEST, "Should fail if PersonService::addParent throws an error."),
                injectObjectMapper);
        // not fail for three parents
        executeTestShouldFail(
                testClass,
                "testAddThreeParents",
                "Should fail if PersonService::addParent adds more than three parents.",
                (invocation) -> {
                    var person = (Person) invocation.getArgument(0);
                    var parent = (Person) invocation.getArgument(1);
                    person.getParents().add(parent);
                    return personRepository.save(person);
                }, injectObjectMapper);
        // not saving to repository
        executeTestShouldFail(
                testClass,
                "testAddThreeParents",
                "Should fail if PersonService::addParent does not save the entities to the database.",
                (invocation) -> {
                    var person = (Person) invocation.getArgument(0);
                    var parent = (Person) invocation.getArgument(1);
                    person.getParents().add(parent);
                    return person;
                }, injectObjectMapper);
    }

    private void executeTestShouldSucceed(Object testClass, String testName, boolean injectObjectMapper) {
        // inject beans and prepare test class
        applicationContext.getAutowireCapableBeanFactory().autowireBean(testClass);
        if (injectObjectMapper) {
            injectObjectMapper(testClass);
        }

        Method testMethod = getTestMethod(testClass, testName);

        try {
            invokeMethod(testClass, testMethod);
        } catch (Throwable t) {
            fail(String.format("PersonIntegrationTest::%s should succeed, but failed: %s", testName, t.getMessage()));
        }
    }

    private void executeTestShouldFail(Object testClass, String testName, String failureMessage, Function<InvocationOnMock, Object> mockedAddParentBehavior, boolean injectObjectMapper) {
        // inject beans and prepare test class
        applicationContext.getAutowireCapableBeanFactory().autowireBean(testClass);
        if (injectObjectMapper) {
            injectObjectMapper(testClass);
        }
        doAnswer(mockedAddParentBehavior::apply).when(personService).addParent(any(), any());

        Method testMethod = getTestMethod(testClass, testName);

        try {
            invokeMethod(testClass, testMethod);
        } catch (Throwable t) {
            // testClass failure was expected
            return;
        }

        fail(String.format("PersonIntegrationTest::%s should fail, but succeed: %s", testName, failureMessage));
    }

	private Method getTestMethod(Object testClass, String testName) {
		try {
			var testMethod = getMethod(testClass, testName);
			testMethod.setAccessible(true);
			return testMethod;
		} catch (Throwable t) {
			fail(String.format("PersonIntegrationTest::%s does not exist.", testName));
		}
		return null;
	}

    // The test class has problems finding/registering the modules for the ObjectMapper, therefore this
    // method injects the ObjectMapper with reflection
    private void injectObjectMapper(Object testClass) {
        ObjectMapper mapper = new ObjectMapper();
        mapper.findAndRegisterModules();

        Optional<Field> optionalField = Arrays.stream(testClass.getClass().getDeclaredFields()).filter(field -> "ObjectMapper".equals(field.getType().getSimpleName())).findFirst();
        assertThat(optionalField).as(String.format("An attribute of type ObjectMapper with name 'objectMapper' is required in %s.", testClass.getClass().getSimpleName())).isPresent();
        Field field = optionalField.get();
        String fieldName = field.getName();

        try {
            ReflectionTestUtils.setField(testClass, fieldName, mapper);
        } catch (Exception e) {
            fail("Something went wrong. Please contact a tutor or instructor.");
        }
    }
}
