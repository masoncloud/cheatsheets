# Django Testing

### Run all tests

    python manage.py test
    
### Running specific tests

    python manage.py test specific_tests
    
### Verify model raises validation error on invalid value within unit test

    from django.core.exceptions import ValidationError
    ...
    
        def test_some_invalid_input(self):
            
            item = Item(value='invalid_value')
            
            with self.assertRaises(ValidationError):
                item.save()
                
### Verify validation when database backend does not support constraint defined in model

    with self.assertRaises(ValidationError):
        item.save()
        item.full_clean()
        
### Verify form validation

    def test_form_invalidates_invalid_input(self):
    
        form = SomeForm(data={'should_not_be_empty': '')
        
        # Calling is_valid will validate input and also populate form.errors
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['should_not_be_empty'], ['Should not be empty should not be empty'])

### Verify page returns correct template

    def test_page_uses_correct_template(self):
    
        response = self.client.get('/some_resource')
        self.assertTemplateUsed(response, 'some_resource.html')

### Verify page uses correct form

    from resources.form import ResourceForm
    ...
    
    def test_page_uses_correct_form(self):
    
        response = self.client.get('/some_resource')
        self.assertIsInstance(response.context['form'], ResourceForm)

### Obtain returned HTML from Django test client

    response = self.client.get('/something')
    html = response.content
    
    # To test if string in content
    self.assertIn('something', response.content.decode())
    
### Run a single test within a test case

Provide the full module namespace to access the individual test:

    python manage.py test functional_tests.test_items.ItemTests.test_specific_test
