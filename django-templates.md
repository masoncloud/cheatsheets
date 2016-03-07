# Django Templates

### Concatenate value to argument sent to include

    {% include 'widget.html' with action=some_var|add:"/new" %}

### Access current iteration count of a template loop

Starting at 1, you can access the current iteration count via:

    {% for item in items %}
        {{ forloop.counter }}
    {% endfor %}

### Access content in inherited template block

Note the usage of `block.super`

    [base.html]
    ...
    {% block content %}
        <h1>Content</h1>
    {% endblock %}
    
    [child.html]
    {% extends 'base.html' %}
    ...
    {% block content %}
        {{ block.super }}
        <p>Some content</p>
    {% end block %}
    
Would yield the following output

    <h1>Content</h1>
    <p>Some content</p>
    