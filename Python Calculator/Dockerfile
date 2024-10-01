# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install Tkinter and Xvfb for headless display
RUN apt-get update && apt-get install -y python3-tk xvfb

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Start Xvfb before running the Python application
CMD ["xvfb-run", "python", "main.py"] 
