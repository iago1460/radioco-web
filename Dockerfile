# Stage 1: Build Sass files
FROM node:23-alpine AS sass-builder

WORKDIR /app

# Install dart-sass (modern Sass implementation)
RUN npm install -g sass

# Copy sass files (adjust paths as needed)
COPY ./backend/radioco/main/static/main/scss /app/sass/

# Build CSS from Sass
RUN sass /app/sass/:/app/css/ --style=compressed


# Stage 2: Python application
FROM python:3.13-alpine

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy poetry configuration files
COPY pyproject.toml poetry.lock* /app/

# Configure poetry to not use virtualenv
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-root --no-interaction

# Copy application code
COPY ./backend/ /app/backend/

# Copy compiled CSS from first stage
COPY --from=sass-builder /app/css/ /app/backend/radioco/main/static/main/css/

# Working directory for the application
WORKDIR /app/backend/

# Prepare static files
RUN poetry run python manage.py collectstatic --no-input
RUN poetry run python manage.py compress
RUN poetry run python manage.py collectstatic --no-input

# Add gettext for translations
RUN apk add --no-cache gettext

# Command to run the application
CMD ["gunicorn", "radioco.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]