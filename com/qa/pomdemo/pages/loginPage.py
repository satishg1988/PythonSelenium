# from selenium import webdriver
# from com.qa.pomdemo.tests.loginTC import Logintest
import time
from selenium.webdriver.common.by import By
from com.qa.pomdemo.locators import allPageLocators
from com.qa.pomdemo.utilities.allevents import Events


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome("/Users/sateeshg/PycharmProjects/PythonSelenium/drivers/chromedriver")

        self.username_textbox = allPageLocators.AllLocators.username_textbox
        self.password_textbox = allPageLocators.AllLocators.password_textbox
        self.login_button = allPageLocators.AllLocators.login_button

    def enter_username(self, username, locator_type="XPATH"):
        if not self.username_textbox.isspace():
            print("User Name textbox is not empty", self.username_textbox.isspace())
            time.sleep(1)

            # Declaring object to Events class from allevents.py
            global ae
            ae = Events(self.driver)
            by_type = ae.bytype(locator_type="XPATH")

            self.driver.find_element(by_type, self.username_textbox).clear()
            # self.driver.find_element(by_type, self.username_textbox).clear()
            # self.driver.find_element(By.XPATH, self.username_textbox).clear()
            self.driver.find_element(by_type, self.username_textbox).send_keys(username)

    def enter_password(self, password):
        by_type = ae.bytype(locator_type="XPATH")

        if not self.password_textbox.isspace():
            print("Password textbox is not empty", self.password_textbox.isspace())
            time.sleep(1)
            self.driver.find_element(by_type, self.password_textbox).clear()
        self.driver.find_element(by_type, self.password_textbox).send_keys(password)

    def click_login(self):
        by_type = ae.bytype(locator_type="ID")

        self.driver.find_element(by_type, self.login_button).click()
        print("User Login Successful")