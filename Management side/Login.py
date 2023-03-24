import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoGin:
    def __init__(self):
        self.we = webdriver.Chrome()
        self.we.get("https://dev.znk.group/training/manage.htm")

    def login(self):
        self.we.implicitly_wait(5)
        self.we.find_element(By.ID,'txtuserid').send_keys("江啟锋")
        time.sleep(3)
        self.we.find_element(By.ID,"txtpassword").send_keys("jqf123456")
        
        try:
            self.we.find_element(By.ID,'btnLogin').click()

        except:
            print("登录失败")
        time.sleep(40)
        self.we.quit()
    def run(self):
        self.login()

if __name__ == '__main__':
    # url = input("请先输入网址：")
    # username = input("请输入用户名：")
    # password = input("请先输入密码：")
    login = LoGin()
    login.run()
