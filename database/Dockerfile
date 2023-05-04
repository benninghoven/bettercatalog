# Use an official MySQL runtime as a parent image
FROM mysql

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=root

# build the db
COPY ./create.sql /docker-entrypoint-initdb.d/

# Expose port 3306 for MySQL
EXPOSE 3306

# Run the command to start the MySQL server
CMD ["mysqld"]

