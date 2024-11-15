# Use a base image with Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy the app.py file into the container
COPY . /app

# Expose port 8000 for the web server
EXPOSE 8000

# Define the command to run the Flask app
CMD ["python", "app.py"]
