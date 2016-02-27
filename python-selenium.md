# Python Selenium

The below show how the selenium project is used within Python. Most examples below assume you are working in the context of a unittest.

### Initialize Firefox webdriver

    from selenium import webdriver
    ...
        
        self.browser = webdriver.Firefox()

### Make a request

    self.browser.get('<url>')

### Check if value in body

    self.assertNotIn('Some Value', self.browser.find_element_by_tag_name('body').text)
    
### Set browser window dimensions

    self.browser.set_window_size(1024, 768)

### Ask selenium to explicitly wait until an element is present

    from selenium.webdriver.support.ui import WebDriverWait
    ...
    
            ...
            WebDriverWait(self.browser, timeout=30).until(
                lambda b: b.find_element_by_id('<some element id>')
            )
