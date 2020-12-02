from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import namedtuple


Locator = namedtuple("locator", ["by", "value"])


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

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
