# Deliver and host your application

In this exercise, we are looking at a Spring Boot application that provides functionality to persist persons and create parent-child relationships between different persons.

We will host this app on the internet using Heroku and will connect a Postgres database to persist entities that our app works with. Before you can start working on this exercise, you will have to fulfill the following prerequisites: 
- install your system-specific [Docker](https://docs.docker.com/get-docker/) version.
- install your system-specific [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) version.

## The pipeline process

The following model describes the pipeline on how your Java source code files will be processed to deploy your application to Heroku.
![Deployment Overview.png](/api/core/files/markdown/Markdown_2022-07-05T20-20-26-289_e37c8bd9.png)
1. Java compiles the source code files (\*.java) to binary files (\*.class) to be executable on your local machine. As a side note, Java compiles your source code files every time you execute Java code locally.
2. Gradle executes the implemented unit and integration test cases.
3. Gradle builds an executable .jar-file that contains the application itself and all required external dependencies (e.g. the Spring Boot dependency).
4. Docker creates an image from this executable .jar-file.
5. The Docker image is deployed to Heroku and is now accessible via the internet.


## The system
Heroku runs a Docker container and a Postgres database. This Docker container contains our hosted Spring Boot application which uses functionality provided by Postgres (`Postgres API`) using a [socket and SQL-statements](https://devcenter.heroku.com/articles/connecting-heroku-postgres#connecting-in-java). A client (e.g. your local machine) can invoke HTTP requests to access functionality that your Spring Boot application provides (`Person REST API`). The Spring Boot application consists of three different layers:
- Web Layer: This layer contains `PersonResource` which provides HTTP(-REST) endpoints to the client.
- Application Layer: This layer contains `PersonService` which provides business logic to `PersonResource`.
- Persistence Layer: This layer contains `PersonRepository` which provides functionality to perform database actions regarding entities of type `Person`. This layer uses functionality of the connected Postgres database.


![Subsystem Decomposition](/api/core/files/markdown/Markdown_2022-07-05T20-19-07-792_d0aedaf0.png)




## Part 1: Create a database-connected application on Heroku
[task][Create app on Heroku](App name was set,App exists on Heroku)
You will have to create an app on [Heroku](https://www.heroku.com/), as shown in the tutor exercise. You have to perform the following steps:
1. [Sign up](https://signup.heroku.com/), if you did not create an account yet.
2. [Create an app](https://dashboard.heroku.com/new-app) with a descriptive name. Choose `Europe` as the region and confirm by clicking `Create App`.
3. Insert the name of your app from step 2 into the `heroku-app-name.txt` file. (Do not put anything else in it)
4. Run `heroku login` from your command line. Press any key if you are asked to complete the login process in the browser.
5. Run `heroku container:login` from your command line to login into the Heroku registry.

[task][Connect your Heroku app to a database](App has access to Postgres,App uses Postgres)
**Note**: These tests will always fail until the application has been deployed to Heroku in Part 3.

Now you will have to connect your Heroku app to a database. Heroku provides an easy way to connect a Postgres database to any hosted app as following:
1. Inside your Heroku app, navigate to the `Resources` tab and search for `Heroku Postgres` in the search bar.
2. Press the button `Submit Order Form`.

You have now created an app on Heroku with a connected database. Now it is time to prepare the deployment of your Spring application to Heroku. You will build a Docker image from your application and set up everything for the delivery.




## Part 2: Prepare the deployment
[task][Create Dockerfile](Dockerfile was adapted)
The Dockerfile in your local repository defines how Docker creates an image from your application. [This reference](https://docs.docker.com/get-started/02_our_app/) provides information on how to create a sample `Dockerfile` and outlines the general structure. [This site](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index) contains all commands that you will need to adjust the `Dockerfile` in your repository as described in the following steps:
1. Set `openjdk:17-bullseye` as the base image.
2. Set the working directory to `/app`. The command `WORKDIR` may be useful. The working directory is the directory where the commands in the `Dockerfile` are executed.
3. When you execute `./gradlew clean build`, Gradle generates a jar file from your application and stores this file in the standard Gradle build output directory (most likely in `./build/libs`). This is shown in step 3 in the pipeline process at the very start of the problem statment. Create a Docker command that copies this generated jar file to the current working directory with a new name `app.jar`. (Note that the file name may be different before!).
4. Create a command that copies the file `start.sh` into the working directory. Note that we set the working directory in step 2 and therefore, can simply copy the file to the current directory.
5. Might be necessary: Make `start.sh` executable by executing `chmod 700 start.sh` from the command line. Otherwise, you may receive an error about missing permissions.
6. Add the line `CMD ./start.sh` to your `Dockerfile`. This command defines that the script defined in `start.sh` will be executed as part of building the Docker image.

[task][Create build script](build.sh or build.bat was adapted)
**Note 1**: In this task, you will have to create a script that you will have to execute on your local computer. Since the supported file formats differ between existing operating systems, you will only have to adjust **one** script file and should ignore the other file. If you are working on a Windows setup, you will have to adjust the `build.bat`. If you are working on a Linux/Mac setup, you will have to adjust the `build.sh`. In both cases, only adjust your system-specific file.

**Note 2**: If you are working on a `Windows` setup, prepend `call ` before every command described in the following steps (e.g., `call ./gradlew clean build`).

**Note 3**: If you are working on an Apple computer with the M1/M2 chip (or any other ARM-based architecture) you will have to use the `docker buildx` command (e.g. `docker buildx create` or `docker buildx build`). If you are unsure whether you have an ARM-based architecture, you'll most likely won't have an ARM-based architecture. If you are interested in the background, you can find more information [here](https://www.docker.com/blog/multi-platform-docker-builds/).


This build script should automatically build your Spring Boot server, create a Docker image, and deploy this image to Heroku. To do so, you will have to add the following commands to the script file (replace `<app-name>` with the name set in Part 1):
1. Build the Spring Boot application with Gradle: `./gradlew clean build`
2. Create a new buildx container `docker buildx create` (only required for ARM-based architectures)
3. Build the Docker image with `docker build <options> .` (for Intel & AMD processors) or `docker buildx build <options> .` (only required for ARM-based architectures, because the local ARM-based architecture differs from the AMD-based architectures provided on Heroku) with these options:
    - `--platform linux/amd64` (only required for docker buildx)
    - `--load` (only required for docker buildx)
    - `-t registry.heroku.com/<app-name>/web`: This will set the tag of the Docker image. The tag specifies the URL of the Heroku Docker registry and the name of the image (which is the app name followed by `/web`)

4. Only required for ARM-based architectures: Stop the buildx container: `docker buildx stop`
5. Only required for ARM-based architectures: Delete the buildx container: `docker buildx rm`
6. Push the docker image to the heroku container registry: `docker push registry.heroku.com/<app-name>/web`
7. Release the container on the heroku registry: `heroku container:release web -a <app-name>`
8. Stop the docker container locally: `docker rmi registry.heroku.com/<app-name>/web`

**Note**: Steps 4, 5, and 8 are optional, but recommended. This ensures that the running Docker container on your local computer is stopped and deleted.

## Part 3: Deploy your app to Heroku

[task][Deploy to Heroku](Test running inside Docker,Endpoints work correctly,App has access to Postgres,App uses Postgres)
Make sure that Docker is running on your local machine. Then run your script to deploy your app to Heroku. You can run your script by executing `./build.bat` or `./build.sh` (depending on your OS) from the command line. ***Do not execute start.sh***.

**Note**: The submission of your deployed app is only tested (and rated) on Artemis on new push events to your repository. Therefore, make sure to perform a push for every new change that should be tested and scored on Artemis.

## Part 4: Implement new functionality

Now that you have deployed the first version of your application, you decide to improve the application and deploy an updated version. In this part, you should implement functionality to create and persist parent-child relationships between persons.

### Adding a feature
[task][Implement PersonService](addChild(),addChildThrows(),addParent(),addParentThrows(),removeChild(),removeChildThrows(),removeParent(),removeParentThrows())
You have to complete the implementation of some methods in `PersonService`. In case the following respective condition is not fulfilled, each method should throw an exception of type `ResponseStatusException` with status code 400 (Bad Request):
- `addParent(Person person, Person parent)`: `person` has to have less than 2 parents before adding the parent. `parent` should be added to the `person`'s list of parents. Afterward, `person` should be saved to the database by calling `save(..)` from `personRepository`. `addParent` should return the result of this method call.
- `addChild(Person person, Person child)`: `child` has to have less than 2 parents before adding the child. Add `child` to the `parent`'s list of children. Save and return the changed and persisted `person`.
- `removeParent(Person person, Person parent)`: `person` has to have a number of parents greater than 1 before removing the parent. Remove `parent` from the `person`'s list of parents. Save and return the changed and persisted `person`.
- `removeChild(Person person, Person child)`: `child` has to have a number of parents greater than 1 before removing the child. Remove `child` from the `person`'s list of children. Save and return the changed and persisted `person`.
 
***Important: You only have to save the parent-child in one direction. E.g., `addParent(person: Person, parent: Person)` only has to add `parent` to the list of parents of `child`, and not `child` to the list of children of `parent`. Saving the updated person to the database (with PersonRepository), Spring automatically sets this reference.***


### Writing test cases
Writing test cases should be part of implementating a new feature to test and ensure that the implemented functionality works correctly. We will look at two types of test cases: Unit Tests and Integration Tests. Check out the [lecture slides](https://artemis.ase.in.tum.de/courses/169/lectures/368) to make yourself aware of the purpose and characteristics of these types.

[task][Implement PersonServiceTest](test_testAddParent_Service(),test_testAddThreeParents_Service())
 You should implement two unit tests in `PersonServiceTest` using `JUnit5`. `PersonServiceTest` already contains two examples that may help you implementing the following test cases:
- `testAddParent`: Create two instances of `Person`, one acts as a child and one as a parent, and save these objects to the database. Invoke the method `addParent` in `PersonService`. Verify that all instances of `Person` have been correctly saved to the database and that the parent-child relationship has been created only for the first two added parents (in the database and the returned object of `addParent`).
- `testAddThreeParents`: Create four instances of `Person`, one acts as a child and three as parents, and save these objects to the database. Invoke the method `addParent` twice so that the parent-child relationships between the two instances of `Person` are created. Assert that the method invocations return the correct persons, the parent and child have been correctly saved to the database, and that the parent-child relationship is created (in the database and the returned objects of `addParent`). Invoke `addParent` again with the third parent and assert that the method throws a `ResponseStatusException` with status code 400 (Bad Request).


[task][Optional: Implement PersonIntegrationTest](test_testAddParent_Integration(),test_testAddThreeParents_Integration())
***Note 1: This task is optional and grants up to four bonus points. You are still able to reach the full score without solving this task.***

***Note 2: You will have to use an instance of `ObjectMapper` to serialize the instances of `Person` (example provided). You have to use the attribute named `objectMapper` in `PersonIntegrationTest`. Don't create and use a new instance of `ObjectMapper`, nor delete the existing one!***

To make sure that the whole system works correctly, you should write two integration tests in `PersonIntegrationTest`. These tests basically test the same functionality, but at the full scope of the system (instead of only the service and repository). Therefore, instead of invoking the methods of `PersonService` directly, we will invoke the REST endpoints of `PersonResource`. You should use [Spring MockMVC](https://www.baeldung.com/integration-testing-in-spring#Writing) to invoke the endpoints.
`PersonIntegrationTests` already contains two test cases that you can use as a reference, and in which you should implement the following test cases:
- `testAddParent`: Perform the same test setup and assertions as in `PersonServiceTest`, but instead of invoking `PersonService::addParent`, you should invoke the endpoint `PUT /persons/{personId}/parents` and pass the respective parent as the content.
- `testAddThreeParents`: Instead of invoking `PersonService::addParent`, you should invoke the endpoint `PUT /persons/{personId}/parents` and pass the respective parent as the content.


## Part 5: Deploy the updated version

[task][Re-deploy to Heroku](New Endpoints work correctly,New Endpoints work correctly 2)
Now it is time to deploy the updated version of your application. Perform the same actions as in Step 3 to automatically build the project, build the Docker image, and deploy this image to Heroku.
