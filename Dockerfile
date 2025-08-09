# Use Python 3.13 Alpine image as base
FROM python:3.13-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # Tell poetry not to create a virtual environment
    POETRY_VIRTUALENVS_CREATE=false \
    # Install to system instead of virtualenv
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Add build argument for version
ARG VERSION=0.1.0
ENV APP_VERSION=${VERSION}

# Create non-root user
RUN addgroup -S app && \
    adduser -S -G app app

# Install system dependencies required for Python packages
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    git

# Install poetry
RUN pip install poetry==2.1.4 --root-user-action ignore

# Set working directory and change ownership
WORKDIR /app
RUN chown app:app /app

# Copy only requirements first to leverage Docker cache
COPY --chown=app:app pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application
COPY --chown=app:app . .

# Install the application
RUN poetry install --no-interaction --no-ansi && \
    # Clean up build dependencies to reduce image size
    apk del gcc musl-dev python3-dev libffi-dev openssl-dev cargo git

# Switch back to non-root user for running the application
USER app

# Expose the port the app runs on
EXPOSE 3000

# Run the application using the console script
ENTRYPOINT ["aimail"]
