call ./gradlew clean build
call docker build --progress plain -t eist-heroku .

call docker push registry.heroku.com/morrien-test/web
call heroku container:release web -a morrien-test

call docker rmi registry.heroku.com/morrien-test/web