# Python Unittest

### How to Temporarily Skip a Unit Test

    from unittest import skip
    ...
    
        @skip
        def test_example_to_skip(self):

### Force a Test to Fail

    def test_example_to_fail(self):
        ...
        
        self.fail('This will fail.')
