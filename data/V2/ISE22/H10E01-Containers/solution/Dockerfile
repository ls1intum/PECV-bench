FROM openjdk:17-bullseye

WORKDIR /app
COPY build/libs/Eist-Heroku-*.jar app.jar
COPY start.sh start.sh
RUN chmod 770 start.sh
CMD ./start.sh