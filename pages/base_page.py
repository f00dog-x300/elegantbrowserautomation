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
        """Helper method to go to url provided by page objects. Goes to 
        url specified by page. Search page object's url property to see URL"""
        self.driver.get(self.url)