from selenium.webdriver.common.by import By

from .base_element import BaseElement, Locator
from .base_page import BasePage


class TrialPage(BasePage):
    """Contains web elements from Trial Grounds page.

    Args:
        BasePage (object): Inherits from BasePage object
    """

    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def stone_input(self):
        """Refers to 1st input field in Trial Grounds page

        Returns:
            object: Containing instance of BaseElement class to find elements
        """
        # locator = (By.CSS_SELECTOR, 'input#r1Input')
        locator = Locator(by=By.CSS_SELECTOR, value='input#r1Input')
        return BaseElement(self.driver, locator)

    @property
    def stone_button(self):
        """Refers to 1st button in Trial Grounds page

        Returns:
            object: Containing instance of BaseElement class to find elements
        """
        # locator = (By.CSS_SELECTOR, 'button#r1Btn')
        locator = Locator(by=By.CSS_SELECTOR, value='button#r1Btn')
        return BaseElement(self.driver, locator)

    @property
    def secrets_input(self):
        """Refers to secrets text field in Trial Grounds page

        Returns:
            object: Containing instance of BaseElement class to find elements
        """
        locator = Locator(by=By.CSS_SELECTOR, value='input#r2Input')
        return BaseElement(self.driver, locator)

    @property
    def secrets_button(self):
        """Refers to secrets button in Trial Grounds page

        Returns:
            object: Containing instance of BaseElement class to find elements
        """
        locator = Locator(by=By.CSS_SELECTOR, value='button#r2Butn')
        return BaseElement(self.driver, locator)

    @property
    def secret_word(self):
        locator = Locator(by=By.ID, value='passwordBanner')
        return BaseElement(self.driver, locator)

    @property
    def success_word(self):
        locator = Locator(by=By.ID, value='successBanner1')
        return BaseElement(self.driver, locator)
