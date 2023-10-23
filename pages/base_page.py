from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    """ Contains methods common to all pages"""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)
    
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        self.get_element(locator).click()

    def set_element(self, locator, value):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(value)

    def get_text(self, locator):
        return self.get_element(locator).text

    def get_title(self):
        return self.driver.title
    
    def wait_for_presence_of_element(self, locator, *, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.presence_of_element_located(locator))
            
        except TimeoutError:
            return False
        else:
            return True
        
    class TextToChange:
        def __init__(self, locator, text):
            self.locator = locator
            self.text = text

        def __call__(self, driver):
            actual_text = driver.find_element(*self.locator).text
            # print(f'actual_text:{actual_text}')
            return self.text != actual_text
        
        
    def wait_for_text_to_change(self, locator, text_before, *, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)    
            wait.until(self.TextToChange(locator, text_before))
        except TimeoutError:
            return False
        else:
            return True
    
    class IntialLoad:
        def __init__(self, locator):
            self.locator = locator

        def __call__(self, driver):
            num_of_products = int(driver.find_element(*self.locator).text.split()[0])
            # print(f'no of products in initial load: {num_of_products}')
            return num_of_products > 0
        
    def wait_for_initial_load(self, locator, *, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(self.IntialLoad(locator))
        except TimeoutError:
            return False
        else:
            return True    
        
    def wait_for_alert(self, *, timeout=4):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.alert_is_present())
        except TimeoutError:
            return False
        else:
            return True
        
    
