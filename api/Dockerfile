# Use an official Python runtime as the base image
FROM python:3

# Set the working directory in the container to /app
WORKDIR /app

# Copy the local requirements.txt file to the container
COPY requirements.txt .

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0"]