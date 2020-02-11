#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.taobao.com/')
input = driver.find_element_by_id('q')
input.send_keys('IPad')
time.sleep(1)
input.clear()
input.send_keys('Surface Pro')
# 淘宝页面修改，必须先登录在能访问。
button = driver.find_element_by_class_name('btn-search')
button.click()
