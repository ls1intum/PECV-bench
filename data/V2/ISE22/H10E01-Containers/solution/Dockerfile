FROM openjdk:17-bullseye

WORKDIR /app
COPY build/libs/H10E01-Containers-*.jar app.jar
COPY start.sh start.sh
RUN chmod 770 start.sh
CMD ./start.sh