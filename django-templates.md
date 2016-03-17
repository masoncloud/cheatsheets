# Django Templates

### Include existing template in current template with arguments

    [_example_template_to_include.html]
    <h1>{{ greeting }} {{ target }}</h1>
    
    [normal_template.html]
    {% include "_example_template_to_include.html" with greeting="Hello" target="World" %}

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

### Place comment inside template

Multiline comment:

    {% comment 'Optional note' %}
    ... ignored lines
    {% endcomment %}

Single line:

    {# Comment #}


### Access GenericView's choices inside a template

    form.fields.field_name.choices
    
### Format a datetime 

    { item.date_time|date:"Y-m-d" }
