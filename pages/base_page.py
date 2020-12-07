class BasePage(object):
    """Returns basic requirements to start webdriver"""
    url = None

    def __init__(self, driver):
        """Initialization method requiring instance of webdriver

        Args:
            driver (Webdriver): requires instance of webdriver class
        """
        self.driver = driver

    def go(self):
        """Helper method to go to url provided by page objects"""
        self.driver.get(self.url)