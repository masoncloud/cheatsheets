# Python Unittest

### How to temporarily skip a unit test

    from unittest import skip
    ...
    
        @skip
        def test_example_to_skip(self):

### Force a test to fail

    def test_example_to_fail(self):
        ...
        
        self.fail('This will fail.')

### Test long strings for equality, show diff output

    def test_long_str_match(self):
        ...
        
        # Test and truncate long output
        self.assertMultiLineEqual(self.long_str_a, self.long_str_b)
        
        # Test and don't truncate long output
        self.assertMultiLineEqual(self.long_str_a, self.long_str_b, maxDiff=None)
