#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.jd.com/")
try:
    # 使用了 WebDriverWait 来设置最长等待时间,在 10s 内都无法返回结果，将会抛出 TimeoutException
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "key"))
    )
finally:
    driver.quit()
