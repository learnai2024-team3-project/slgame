# Base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files and to use unbuffered mode
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /slgsite

# Copy requirements.txt and install dependencies
COPY requirements.txt /slgsite/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . /slgsite/

# Set Django environment variables
ENV DJANGO_SETTINGS_MODULE=slgame.settings

# Expose the application port
EXPOSE 8000

# Add Docker entrypoint to run migrations and collect static files when the container starts
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Create a non-root user to run the application
RUN useradd -m django_user
USER django_user

# Set entrypoint to the custom script
ENTRYPOINT ["/docker-entrypoint.sh"]

# Use Gunicorn to run the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "slgame.wsgi:application"]

