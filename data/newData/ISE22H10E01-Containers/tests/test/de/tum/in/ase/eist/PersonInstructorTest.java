package de.tum.in.ase.eist;

import de.tum.in.ase.eist.repository.PersonRepository;
import de.tum.in.ase.eist.service.PersonService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.SpyBean;
import org.springframework.context.ApplicationContext;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.web.servlet.MockMvc;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT)
@AutoConfigureTestDatabase
@DirtiesContext(classMode = DirtiesContext.ClassMode.BEFORE_EACH_TEST_METHOD)
@AutoConfigureMockMvc
public class PersonInstructorTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private PersonRepository personRepository;

    @Autowired
    private ApplicationContext applicationContext;

    @SpyBean
    private PersonService personService;

    @Test
    public void test_testAddParent_Integration() {
        PersonTestHelper testHelper = new PersonTestHelper(personRepository, personService, applicationContext);
        testHelper.test_testAddParent(new PersonIntegrationTest(), true);
    }

    @Test
    public void test_testAddThreeParents_Integration() {
        PersonTestHelper testHelper = new PersonTestHelper(personRepository, personService, applicationContext);
        testHelper.test_testAddThreeParents(new PersonIntegrationTest(), true);
    }

    @Test
    public void test_testAddParent_Service() {
        PersonTestHelper testHelper = new PersonTestHelper(personRepository, personService, applicationContext);
        testHelper.test_testAddParent(new PersonServiceTest(), false);
    }

    @Test
    public void test_testAddThreeParents_Service() {
        PersonTestHelper testHelper = new PersonTestHelper(personRepository, personService, applicationContext);
        testHelper.test_testAddThreeParents(new PersonServiceTest(), false);
    }
}
