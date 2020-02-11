#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.jd.com/')
print(browser.page_source)
browser.close()


browser = webdriver.Chrome()

browser.get('https://www.jd.com/')
input_key = browser.find_element_by_id('key')
print(input_key)
browser.close()
"""
所有的获得单个节点的方法
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""
browser = webdriver.Chrome()

browser.get('https://www.jd.com/')
input_key1 = browser.find_element(By.ID, 'key')
print(input_key1)
browser.close()

lis = browser.find_elements_by_css_selector('.cate_menu li')
print(lis)
