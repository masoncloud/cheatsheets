# Django Forms

### Obtain form HTML from form instance

    form_html = SomeForm().as_p()
    
### Specify which model a ModelForm applies to

    from django import forms
    from items.model import Item 


    class ItemForm(forms.models.ModelForm):
    
        class Meta:
            
            model = Item
            fields = ('field_a', 'field_b', 'etc')

### Override ModelForm widget attributes

    from django import forms
    from items.model import Item 


    class ItemForm(forms.models.ModelForm):
    
        class Meta:
            
            model = Item
            fields = ('field_a', 'field_b', 'etc')
            
            widgets = {
                'field_a': forms.fields.TextInput(attrs={
                    'placeholder': 'Enter a value here',
                    'class': 'form-control input-lg'
                })
            }

### Customize error message returned on invalid ModelForm input

    from django import forms
    from items.model import Item 


    class ItemForm(forms.models.ModelForm):
    
        class Meta:
            
            model = Item
            fields = ('field_a', 'field_b', 'etc')
            
            error_messages = {
                'field_a': {'required': 'Field A must have a value specified.'}
            }

### Use form in template

    [view.py]
    from items.forms import ItemForm
    
    
    def home_page(request):
        
        return render(request, 'home.html', {'form': ItemForm()})
    
    
    [home.html]
    <form method="POST">
        {{ form.field_a }}
        ...

### Access database object completed form is bound to

    # If item is certainly saved
    item_form = ItemForm()
    item_instance = item_form.instance
    
    # Otherwise, the save method will return the instance when saved
    item_form = ItemForm()
    item_instance = item_form.save()

### Access form field error within template

    form.field.errors