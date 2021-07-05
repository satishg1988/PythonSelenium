import os
import sys
import unittest

import HtmlTestRunner

from com.qa.pomdemo.browsersetup.browserActions import Browser
from com.qa.pomdemo.pages.homePage import HomePage
from com.qa.pomdemo.pages.leavelistpage import LeaveList
from com.qa.pomdemo.pages.loginPage import LoginPage

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class Logintest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # self.driver = webdriver.Chrome("/Users/sateeshg/PycharmProjects/PythonSelenium/drivers/chromedriver")
        # self.driver.maximize_window()
        b = Browser
        b.browser_chrome(cls)
        b.launch_url(cls, "https://opensource-demo.orangehrmlive.com/index.php/auth/login")

    def test_01_ValidLogin(self):
        driver = self.driver

        lp = LoginPage(driver)
        lp.enter_username("Admin")
        lp.enter_password("admin123")
        lp.click_login()

    def test_02_HeaderLink(self):
        driver = self.driver

        hp = HomePage(driver)
        hp.click_welcome_admin_link()

    def test_03_HeaderMenuOptions(self):
        driver = self.driver

        hp = HomePage(driver)
        hp.click_header_menu_options("LEAVE")
        hp.click_header_leave_link()

    def test_04_LeaveList(self):
        driver = self.driver

        llp = LeaveList(driver)
        llp.click_fromdate_leavelist("1994", "SEP", "11")
        llp.click_todate_leavelist("2021", "JUN", "22")

        hp = HomePage(driver)
        hp.click_logout_link()

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver

        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/PycharmProjects/PythonSelenium/reports'))