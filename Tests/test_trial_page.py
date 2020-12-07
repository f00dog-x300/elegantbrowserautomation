from pytest import mark, fixture
from Pages.trial_page import TrialPage


# Test Setup
class TrialPagesTests:
    """List of smoke tests for Trial Page"""

    @fixture(scope='function')
    def trial_page(self, browser):
        """Pytest fixture for trial page to create instance of trial page
        and to load page. 

        Args:
            browser (object): Get webdriver instance from BasePage inherited from TrialPage

        Returns:
            self.trial_page (object): returns instance of TrialPage for accessing
            methods and properties of TrialPage class.
        """
        self.trial_page = TrialPage(driver=browser)
        self.trial_page.go()
        return self.trial_page

    def test_example(self, trial_page):
        """Validate to see if secret word appears"""
        trial_page.stone_input.input_text("rock")
        trial_page.stone_button.click()
        assert trial_page.secret_word.text == "bamboo"

    def test_example2(self, trial_page):
        """Validate to see if success appears"""
        trial_page.secrets_input.input_text("bamboo")
        trial_page.secrets_button.click()
        assert trial_page.success_word.text == "Success!"
