# -*- coding:utf-8 -*-

from selenium import webdriver
import time

url = "http://116.62.57.112/admin/login/loginDo?sys=admin"
driver = webdriver.Chrome()
driver.get(url)

try:
    #　自动化操作
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys("zheng")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("zheng")
    driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/input").click()
    # 释放资源  关闭浏览器
    driver.close()
    driver.quit()
except:
    print("登录失败")