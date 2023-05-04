# Use an official Node.js image as the base image
FROM node:14

# Set the working directory in the container to /app
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package*.json ./

# Install the app's dependencies
RUN npm install
RUN npm install react-router-dom --save
RUN npm install react-select --save

# Copy the rest of the app's files to the container
COPY . .

# Specify the command to run when the container launches
CMD [ "npm", "start" ]

