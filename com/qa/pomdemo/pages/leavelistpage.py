import time

from selenium.webdriver.common.by import By

from com.qa.pomdemo.locators import allPageLocators
from com.qa.pomdemo.utilities.screenshots import ScreenShots


class LeaveList:
    def __init__(self, driver):
        self.driver = driver
        # calling all the locators from allpageLocators>>AllLocators
        self.fromdate_field = allPageLocators.AllLocators.fromdate_field
        self.year_leavelist = allPageLocators.AllLocators.year_leavelist
        self.month_leavelist = allPageLocators.AllLocators.month_leavelist
        self.day_leavelist = allPageLocators.AllLocators.day_leavelist
        self.todate_field = allPageLocators.AllLocators.todate_field
        # self.month_todate_leavelist = allPageLocators.AllLocators.month_todate_leavelist

    def click_fromdate_leavelist(self, req_year, req_month, req_day):
        self.driver.find_element(By.XPATH, self.fromdate_field).click()
        # selecting year in from date
        fromyear = self.driver.find_elements(By.XPATH, self.year_leavelist)
        print("Total Years: " + str(len(fromyear)))
        for year in fromyear:
            if year.text == req_year:
                year.click()
                print(req_year + " month clicked")
                time.sleep(2)
                break
        else:
            print(req_year + " not found")
            self.driver.find_element(By.XPATH, self.fromdate_field).click()

        # selecting month in from date
        frommonth = self.driver.find_elements(By.XPATH, self.month_leavelist)
        print("Total Months: " + str(len(frommonth)))
        for month in frommonth:
            if req_month.casefold() == month.text.casefold():
                month.click()
                print(req_month + " month clicked")
                break
        else:
            print(req_month + " not found")
            self.driver.find_element(By.XPATH, self.fromdate_field).click()
        time.sleep(2)

        # click day in from date
        fromday = self.driver.find_elements(By.XPATH, self.day_leavelist)
        print("Total days:" + str(len(fromday)))
        for day in fromday:
            if req_day.casefold() == day.text.casefold():
                day.click()
                print(req_day + " day clicked")

                # Calling screenshots method
                ss = ScreenShots
                ss.captureScreenShots(self)
                break
        else:
            print(req_day + " not found")
            self.driver.find_element(By.XPATH, self.fromdate_field).click()
        time.sleep(2)

    def click_todate_leavelist(self, req_year, req_month, req_day):
        self.driver.find_element(By.XPATH, self.todate_field).click()
        # selecting year in to date
        fromyear = self.driver.find_elements(By.XPATH, self.year_leavelist)
        print("Total Years: " + str(len(fromyear)))
        for year in fromyear:
            if year.text == req_year:
                year.click()
                print(req_year + " year clicked")
                time.sleep(2)
                break
        else:
            print(req_year + " not found")
            self.driver.find_element(By.XPATH, self.todate_field).click()
        # selecting month in to date
        frommonth = self.driver.find_elements(By.XPATH, self.month_leavelist)
        print("Total Months: " + str(len(frommonth)))
        for month in frommonth:
            if req_month.casefold() == month.text.casefold():
                month.click()
                print(req_month + " month clicked")
                break
        else:
            print(req_month + " not found")
            self.driver.find_element(By.XPATH, self.todate_field).click()
        time.sleep(2)

        # click day in to date
        fromday = self.driver.find_elements(By.XPATH, self.day_leavelist)
        print("Total days:" + str(len(fromday)))
        for day in fromday:
            if req_day.casefold() == day.text.casefold():
                day.click()
                print(day.text + " day clicked")
                break
        else:
            print(req_day + " not found")
            self.driver.find_element(By.XPATH, self.todate_field).click()
        time.sleep(2)
