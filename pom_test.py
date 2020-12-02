from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from pages.training_ground_page import TrainingGroundPage
from pages.trial_page import TrialPage


# Test Setup
browser = webdriver.Chrome(ChromeDriverManager().install())

# Trial Page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()

sleep(3)
browser.quit()