# Pull base image
FROM python:3.10.4-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Django test/CI environment variables
ENV DJANGO_SECRET_KEY=test-secret-key-for-ci-only
ENV DJANGO_DEBUG=True
ENV DATABASE_URL=sqlite:////tmp/test.db
ENV DJANGO_SECURE_SSL_REDIRECT=False
ENV DJANGO_SECURE_HSTS_SECONDS=0
ENV DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=False
ENV DJANGO_SECURE_HSTS_PRELOAD=False
ENV DJANGO_SESSION_COOKIE_SECURE=False
ENV DJANGO_CSRF_COOKIE_SECURE=False
ENV DJANGO_STATICFILES_STORAGE=django.contrib.staticfiles.storage.StaticFilesStorage
# Set work directory
WORKDIR /app

# Copy requirements file
COPY ./requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run tests by default
CMD ["python", "-m", "pytest", "-v"]