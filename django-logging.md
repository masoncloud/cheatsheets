# Django Logging

### Have debug log outputted to the terminal

Within `settings.py`, add the following declaration which will send debug output to Python logging's StreamHandler:

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console']
            }
        }
        'root': {'level': 'INFO'}
    }