# Use official Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy our app into the container
COPY app.py .

# Expose port 8000 for our app
EXPOSE 8000

# Run the Python app
CMD ["python", "app.py"]
