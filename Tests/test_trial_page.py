from pytest import mark
from Pages.trial_page import TrialPage


# Test Setup
class TrialPagesTests:
    """List of smoke tests for Trial Page"""

    # browser = webdriver.Chrome(ChromeDriverManager().install())
    # Trial Page

    def test_example(self, browser):
        self.trial_page = TrialPage(driver=browser)
        self.trial_page.go()
        self.trial_page.stone_input.input_text("rock")
        self.trial_page.stone_button.click()
