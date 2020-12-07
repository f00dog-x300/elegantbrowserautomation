from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@fixture(scope='module')
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    yield browser
    browser.close()
    browser.quit()
