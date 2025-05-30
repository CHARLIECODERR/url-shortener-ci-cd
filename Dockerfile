# Use a base image with Python installed
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
