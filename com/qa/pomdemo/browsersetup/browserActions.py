from selenium import webdriver


# import unittest
# from com.qa.pomdemo.pages.loginPage import LoginPage
# from com.qa.pomdemo.pages.homePage import HomePage

class Browser():

    # def __init__(self, driver):
    #     self.driver = webdriver.Chrome("/Users/sateeshg/PycharmProjects/PythonSelenium/drivers/chromedriver")
    #     self.driver.maximize_window()

    def browser_chrome(self):
        self.driver = webdriver.Chrome("E:/PycharmProjects/PythonSelenium/drivers/chromedriver90.0.4430.24.exe")
        self.driver.maximize_window()

    def launch_url(self, url):
        self.driver.get(url)
        print("URL Launch Successful")

# b = Browser()
# b.browser_chrome()
