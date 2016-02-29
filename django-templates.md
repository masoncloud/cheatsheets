# Django Templates

### Concatenate value to argument sent to include

    {% include 'widget.html' with action=some_var|add:"/new" %}

### Access current iteration count of a template loop

Starting at 1, you can access the current iteration count via:

    {% for item in items %}
        {{ forloop.counter }}
    {% endfor %}
