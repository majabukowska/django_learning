# Blog Application with Django

This is a simple blog application built with Django and Django Rest Framework. It includes functionality for posting blog entries, commenting on posts, and includes integration with Celery for background tasks.

## Features

- CRUD operations for blog posts.
- Comments on blog posts.
- Daily summary of posts sent via email.
- Periodic checks for posts with more than 10 comments using Celery.

## Technologies

- Django 3.2+
- Django Rest Framework
- Celery for asynchronous task queue
- SQLite for development, PostgreSQL recommended for production
- Docker for containerization (optional)

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone https://yourrepository.git
    cd yourrepository
    ```
2. Create a virtual environment:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  
    # On Windows use `myenv\Scripts\activate`
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Setup the database:

    - Ensure you have a database system installed and running (SQLite for development, PostgreSQL for production).
    - Adjust the database settings in myproject/settings.py to point to your database.

5. Migrate the database:
    ```bash
    python manage.py migrate
    ```
6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
7. Run the development server:
    ```bash
    python manage.py runserver
    ```
8. Visit http://127.0.0.1:8000/ in your web browser.

### Celery Configuration

To run the Celery worker:
```bash
celery -A myproject worker -l info
```

To start Celery Beat for periodic tasks:
```bash
celery -A myproject beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

### Testing

To run tests, use:
```bash
python manage.py test
```







