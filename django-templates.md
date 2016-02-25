# Django Templates

### Concatenate value to argument sent to include

    {% include 'widget.html' with action=some_var|add:"/new" %}
