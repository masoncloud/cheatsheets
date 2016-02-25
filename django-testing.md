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