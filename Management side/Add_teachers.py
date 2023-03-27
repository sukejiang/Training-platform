from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class My():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):  # 获取登录页面
        self.driver.get("https://dev.znk.group/training/manage.htm")
        self.driver.maximize_window()
        self.driver.find_element(By.ID,'txtuserid').send_keys("江啟锋")
        time.sleep(1)
        self.driver.find_element(By.ID,'txtpassword').send_keys("jqf123456")
        self.driver.find_element(By.ID,"btnLogin").click()

    def addteachers(self):
        self.driver.find_element(By.XPATH, '//*[@id="navigator"]/ul/li[6]').click()  # 获取用户管理标签页
        self.driver.implicitly_wait(3)
        element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(element)  # 跳转到标签页
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[6]').click() #点击导入按钮
        self.driver.find_element(By.XPATH,'//*[@id="select_btn_1"]').send_keys(os.path.abspath('./导入的信息数据/教师导入.xls')) #点击上传按钮
        time.sleep(1)
        self.driver.get_screenshot_as_file('./截图保存的信息/自动导入教师.png')
        self.driver.quit()
    def run(self):
        self.login()
        self.driver.implicitly_wait(3)
        self.addteachers()








if __name__ == "__main__":
    my = My()
    my.run()