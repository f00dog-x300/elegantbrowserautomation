from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        return element

    def input_text(self, txt):
        self.find().send_keys(txt)

    def click(self):
        element = self.find()
        element.click()

    def attribute(self, attr_name):
        attribute = self.find().get_attribute(attr_name)
        return attribute
    
    @property
    def text(self):
        text = self.find().text
        return text
        