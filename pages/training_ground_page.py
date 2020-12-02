from selenium.webdriver.common.by import By

from .base_element import BaseElement, Locator
from .base_page import BasePage


class TrainingGroundPage(BasePage):
    
    url = 'https://techstepacademy.com/training-ground/'

    @property
    def button1(self):
        locator = Locator(by=By.ID, value='b1')
        return BaseElement(self.driver, locator)
