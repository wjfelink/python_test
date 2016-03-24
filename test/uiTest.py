# -*- coding:utf-8 -*-
__author__ = 'user'
from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get("http://www.so.com")
# assert "360搜索".decode('utf-8') in driver.title
#
# print driver.title
#
# driver.close()

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "C:\Users\user\AppData\Local\Google\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
print driver.title
assert "Google" in driver.title
driver.close()
driver.quit()
