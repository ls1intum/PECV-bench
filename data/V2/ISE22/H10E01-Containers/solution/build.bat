call ./gradlew clean build
call docker build --progress plain -t registry.heroku.com/H10E01-Containers/web .

call docker push registry.heroku.com/H10E01-Containers/web
call heroku container:release web -a H10E01-Containers

call docker rmi registry.heroku.com/H10E01-Containers/web