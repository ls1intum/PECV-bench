# Build the image
./gradlew clean build
# docker build --progress plain -t eist-heroku .
docker buildx create
docker buildx build --platform linux/amd64 --progress plain --load -t registry.heroku.com/morrien-test/web .
docker buildx stop
docker buildx rm

# Release on Heroku
docker push registry.heroku.com/morrien-test/web
heroku container:release web -a morrien-test

# Remove the image locally
docker rmi registry.heroku.com/morrien-test/web