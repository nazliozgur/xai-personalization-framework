# Multi-stage Dockerfile for XAE-Frame
# Build: docker build -t xae-frame:latest .
# Run: docker run -p 8000:8000 xae-frame:latest

# Stage 1: Base Image with Python and System Dependencies
FROM python:3.10-slim-bullseye AS base

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Stage 2: Development Image (includes dev tools)
FROM base AS development

# Copy requirements
COPY requirements.txt requirements-dev.txt ./

# Install all dependencies (including dev)
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

# Copy source code
COPY . .

# Set Python path
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Expose ports
EXPOSE 8000 8501 5000

# Default command (can be overridden)
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Stage 3: Production Image (minimal, optimized)
FROM base AS production

# Copy production requirements only
COPY requirements-prod.txt ./

# Install production dependencies
RUN pip install --no-cache-dir -r requirements-prod.txt

# Create non-root user for security
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app/data /app/models /app/logs && \
    chown -R appuser:appuser /app

# Copy source code
COPY --chown=appuser:appuser ./src /app/src
COPY --chown=appuser:appuser ./configs /app/configs
COPY --chown=appuser:appuser ./scripts /app/scripts

# Set Python path
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV LOG_LEVEL=INFO

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Expose ports
EXPOSE 8000

# Default command
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

# Stage 4: Testing Image (for CI/CD)
FROM development AS testing

# Copy test files
COPY tests/ ./tests/

# Run tests
CMD ["pytest", "tests/", "-v", "--cov=src", "--cov-report=html"]
