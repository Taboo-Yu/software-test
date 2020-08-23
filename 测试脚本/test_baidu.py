# ！/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Time  :2020/8/21 11:02\
# !@Author : 俞涛
# !@File   : .py
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()

driver.quit()
