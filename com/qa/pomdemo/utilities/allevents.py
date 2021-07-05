import sre_compile
from selenium.webdriver.common.by import By


class Events():
    def __init__(self, driver):
        self.driver = driver

    def bytype(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "tagname":
            return By.TAG_NAME
        else:
            print("Locator type " + locator_type + " is not valid")
