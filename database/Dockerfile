FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./create.sql /docker-entrypoint-initdb.d/
