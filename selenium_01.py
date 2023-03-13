from selenium import webdriver
from time import *
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
we = webdriver.Chrome(options=options)
we = webdriver.Chrome()
we.get('http://dev.znk.group/training/')
we.find_element(By.ID,"txtuserid").clear()
we.find_element(By.ID,"txtuserid").send_keys("123")
sleep(20)
we.close()
