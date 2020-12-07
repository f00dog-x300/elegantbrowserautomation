from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import namedtuple


Locator = namedtuple("locator", ["by", "value"])


class BaseElement:
    """Basic class containing helper methods to interact with web elements."""

    def __init__(self, driver, locator):
        """Initialization of BaseElement requires instance of webdriver and locator
        in form of a named tuple.

        Args:
            driver (Webdriver): requires an instance of selenium's webdriver class
            locator (NamedTuple): tuple provided by Locator named tuple
        """
        self.driver = driver
        self.locator = locator

    def find(self):
        """Used to find elements.
        Returns:
            [type]: [description]
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        return element

    def input_text(self, txt):
        """Helper method for inputting text into a text field

        Args:
            txt (str): String that user wants to enter in text field
        """
        self.find().send_keys(txt)

    def click(self):
        """Helper method for clicking a web element"""
        element = self.find()
        element.click()

    def attribute(self, attr_name):
        """Helper method for getting attribute of web element

        Args:
            attr_name (str): Finding name of attribute

        Returns:
            str: String contained in the attribute
        """
        attribute = self.find().get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        """Gets text from web element"""
        text = self.find().text
        return text
