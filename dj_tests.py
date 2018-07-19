#coding=utf-8
from selenium import webdriver
import time
#浏览器驱动
driver=webdriver.Firefox()
driver.get("http://127.0.0.1:8000")
assert 'Django' in driver.title
time.sleep(20)
driver.close()