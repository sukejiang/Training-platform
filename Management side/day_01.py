import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class My():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def login(self):  # 获取登录页面并截图保存
        self.driver.get("https://dev.znk.group/training/manage.htm")
        self.driver.find_element(By.ID,'txtuserid').send_keys("江啟锋")
        time.sleep(3)
        self.driver.find_element(By.ID,'txtpassword').send_keys("jqf123456")
        self.driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("./截图保存的信息/登录页面的信息.png")
        time.sleep(20)
    def run(self):
        self.login()


if __name__ == '__main__':
    my = My()
    my.run()