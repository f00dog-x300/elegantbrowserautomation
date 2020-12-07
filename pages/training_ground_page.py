from selenium.webdriver.common.by import By

from .base_element import BaseElement, Locator
from .base_page import BasePage


class TrainingGroundPage(BasePage):
    """Contains web elements from Training Ground page.

    Args:
        BasePage (object): Inherits from BasePage object
    """
    
    url = 'https://techstepacademy.com/training-ground/'

    @property
    def button1(self):
        """Refers to 1st input field in Training Ground page

        Returns:
            object: Containing instance of BaseElement class to find elements
        """
        locator = Locator(by=By.ID, value='b1')
        return BaseElement(self.driver, locator)
