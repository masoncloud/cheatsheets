# Django ORM

### Make all web request queries wrapped in a single transaction

    [settings.py]
    ...
    
    DATABASES = {
        'default': {
            ...
            'ATOMIC_REQUESTS': True,
        }
    }
    