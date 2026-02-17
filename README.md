# Django Bookstore Project

A Django-based bookstore application with user authentication and book reviews.

## Features

- User authentication (signup, login, logout)
- Book listing and detail views
- Book reviews and ratings
- Search functionality
- Admin interface

## Requirements

- Python 3.10+
- Django 4.0.4
- PostgreSQL (optional, SQLite for development)

---

## Quickstart for Reviewers

The fastest way to verify everything works is with Docker — no local Python setup needed:

```bash
git clone <your-repo-url>
cd ch4-bookstore
docker build -t bookstore .
docker run bookstore
```

All 21 tests should pass. No environment variables or extra configuration required — the Docker image is fully self-contained.

---

## Running Tests Locally

### 1. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Create a `.env` file in the project root:
```
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///tmp/test.db
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_SECURE_HSTS_SECONDS=0
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=False
DJANGO_SECURE_HSTS_PRELOAD=False
DJANGO_SESSION_COOKIE_SECURE=False
DJANGO_CSRF_COOKIE_SECURE=False
```

### 3. Collect static files:
```bash
python manage.py collectstatic --noinput
```

### 4. Run the tests:
```bash
pytest -v
```

---

## Running Tests with Docker

### Build the image:
```bash
docker build -t bookstore .
```

### Run the tests:
```bash
docker run bookstore
```

Tests run automatically on container start. No flags or environment variables needed.

---

## Running the Development Server

1. Run database migrations:
```bash
python manage.py migrate
```

2. Create a superuser:
```bash
python manage.py createsuperuser
```

3. Start the server:
```bash
python manage.py runserver
```

Then visit http://127.0.0.1:8000

---

## Project Structure

- `accounts/` - User authentication app
- `books/` - Book catalog and reviews app
- `pages/` - Static pages (home, about)
- `django_project/` - Django project settings
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates
- `media/` - User-uploaded files

---

## Bug Fixed

The original `requirements.txt` listed `environ==1.5.0` (wrong package). Django's
`settings.py` imports `from environs import Env`, which requires the `environs` package.
The fix was replacing `environ==1.5.0` with `environs==9.5.0` in `requirements.txt`.

See `EXPLANATION.md` for full details.

---

## License

MIT
