# Use official Python runtime as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "app.py"]
