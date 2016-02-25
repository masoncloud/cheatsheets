# Django Management

### Create a new Django project

    django-admin.py startproject project_name

### Create a new Django app

    python manage.py startapp app_name
    
### Create migration scripts

    python manage.py makemigrations

### Update database schema

    # Update database schema
    python manage.py migrate
    
    # Update database schema without prompting
    python manage.py migrate --noinput
    
### Start Django development webserver

    python manage.py runserver
    
### Collect all static files and place in STATIC_ROOT directory

Running the following command will gather all static content and place them in the directory specified by the STATIC_ROOT variable within the projects settings.py file. 

    python manage.py collectstatic  # Add --noinput to avoid confirmation prompting. 
