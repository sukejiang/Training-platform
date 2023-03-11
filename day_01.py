import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wy = webdriver.Chrome(options=options)

wy.get("https://dev.znk.group/training/manage.htm")
wy.find_element(By.ID,'txtuserid').send_keys("江啟锋")
time.sleep(3)
wy.find_element(By.ID,'txtpassword').send_keys("jqf123456")
wy.find_element(By.ID,'btnLogin').click()
time.sleep(500)
wy.quit()