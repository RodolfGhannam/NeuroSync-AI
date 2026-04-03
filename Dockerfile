# NeuroSync AI - Synchronous Layer
# Research-grade Dockerfile for the C-CARE Protocol API

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables for production
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=src/api_sync.py \
    FLASK_ENV=production

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (required for some Python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a non-root user for security
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Expose the port the app runs on
EXPOSE 5000

# Run the application using Gunicorn for deployment readiness
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "src.api_sync:app"]
