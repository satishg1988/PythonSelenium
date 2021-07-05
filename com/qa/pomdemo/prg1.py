from selenium import webdriver
import unittest

driver = webdriver.Chrome("/Users/sateeshg/PycharmProjects/PythonSelenium/drivers/chromedriver")
# driver = webdriver.Firefox("/Users/sateeshg/PycharmProjects/PythonSelenium/drivers/geckodriver")
driver.get("https://freecrm.co.in/")
title = driver.title
print(title)

driver.fi
