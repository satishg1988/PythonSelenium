from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from com.qa.pomdemo.locators import allPageLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # calling all the locators from allpageLocators>>AllLocators
        self.welcome_admin_link = allPageLocators.AllLocators.welcome_admin_link
        self.header_leave_link = allPageLocators.AllLocators.header_leave_link
        self.logout_link = allPageLocators.AllLocators.logout_link
        self.header_menu_bar = allPageLocators.AllLocators.header_menu_bar

    # click the welcome username link on home page
    def click_welcome_admin_link(self):
        self.driver.find_element_by_xpath(self.welcome_admin_link).click()
        # element_welcome_admin_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.welcome_admin_link)))
        # element_welcome_admin_link.click()
        print("Welcome Successful")

    # Get all the header menu options and click the required option
    def click_header_menu_options(self, req_menu):
        header_menu = self.driver.find_elements(By.XPATH, self.header_menu_bar)
        print("Total Header Menu Options: " + str(len(header_menu)))
        for menu in header_menu:
            print(menu.text)
            if req_menu.casefold() == menu.text.casefold():
                action = ActionChains(self.driver)
                action.move_to_element(menu).click(menu).perform()
                # menu.click()
                print(req_menu + " - header menu option clicked")
                break

    def click_header_leave_link(self):
        self.driver.find_element_by_xpath(self.header_leave_link).click()
        # element_header_leave_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.header_leave_link)))
        # element_header_leave_link.click()
        print("Leave header link clicked")

    def click_logout_link(self):
        self.driver.find_element_by_xpath(self.welcome_admin_link).click()
        logout_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.logout_link)))
        # logout_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.logout_link)))
        logout_element.click()
        print("Logout Successful")
