# Django Production

### Using Gunicorn to serve your Django application

Gunicorn may be used as a WSGI HTTP server to server your Django application. The below example assumes a preexisting Django project called 'some_django_site'.

    # First, install Gunicorn (recommended to first be within a virtual environment)
    pip install gunicorn
    
    # Launch gunicorn specifying the 'app' variable within your sites wsgi.py module. 
    gunicorn django_project.wsgi:application
    
    # You may specify the number of workers by using the -w argument. 2-4 works per core is recommended.
    gunicorn -w 4 django_project.wsgi:application
    
### Make Gunicorn use Unix domain sockets instead of binding to a TCP port

    gunicorn --bind unix:/tmp/some_app.domain.com.socket django_project.wsgi:application