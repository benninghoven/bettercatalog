FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./sqlstart.sh /docker-entrypoint-initdb.d/
COPY ./create.sql /docker-entrypoint-initdb.d/

RUN ["/docker-entrypoint-initdb.d/sqlstart.sh"]



