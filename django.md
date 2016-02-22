# Django

## Installation

### Install using PIP

Run the following command to have PIP install Django version 1.8.9 (for example). It is recommended
to do so within an existing virtual environment (not shown).
    
    pip install django==1.8.9
    
## Management

### Create a New Django Project

    django-admin.py startproject project_name

### Create a New Django App

    python manage.py startapp app_name
    
### Create Migration Scripts

    python manage.py makemigrations

### Update Database Schema

    # Update database schema
    python manage.py migrate
    
    # Update database schema without prompting
    python manage.py migrate --noinput
    
### Start Django Development Webserver

    python manage.py runserver
    
### Collect All Static Files and Place in STATIC_ROOT Directory

Running the following command will gather all static content and place them in the directory specified by the STATIC_ROOT variable within the projects settings.py file. 

    python manage.py collectstatic  # Add --noinput to avoid confirmation prompting. 
    
## Configuration

### Disable Debug Mode Providing Full Tracebacks to Visitors

Within your settings.py file, set the following parameter:

    DEBUG = False

Also, within your TEMPLATES parameters, you may also want to set this DEBUG setting to match. 

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'debug': DEBUG,
            },
        },
    ]

    
## Testing

### Run All Tests

    python manage.py test
    
### Running Specific Tests

    python manage.py test specific_tests
    
## Production

### Using Gunicorn to Serve Your Django Application

Gunicorn may be used as a WSGI HTTP server to server your Django application. The below example assumes a preexisting Django project called 'some_django_site'.

    # First, install Gunicorn (recommended to first be within a virtual environment)
    pip install gunicorn
    
    # Launch gunicorn specifying the 'app' variable within your sites wsgi.py module. 
    gunicorn django_project.wsgi:application
    
    # You may specify the number of workers by using the -w argument. 2-4 works per core is recommended.
    gunicorn -w 4 django_project.wsgi:application
    
### Make Gunicorn Use Unix Domain Sockets Instead of Binding to a TCP Port

    gunicorn --bind unix:/tmp/some_app.domain.com.socket django_project.wsgi:application