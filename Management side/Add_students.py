from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
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

    def add_students(self):
        self.driver.find_element(By.XPATH, '//*[@id="navigator"]/ul/li[7]').click()  # 获取用户管理标签页
        self.driver.implicitly_wait(3)
        element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(element)  # 跳转到标签页
        selectA = self.driver.find_element(By.XPATH,'//*[@id="selOrganization"]') #选着下拉框元素

        select = Select(selectA)
        select.select_by_value('13c99aa9-38d1-4d72-4c7d-3d054e6a3afd')  #完成下拉框选中

        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[6]').click() #完成学员导入
        self.driver.find_element(By.XPATH,'//*[@id="select_btn_1"]').send_keys(os.path.abspath('./导入的信息数据/学员导入.xls'))


        time.sleep(1)
        self.driver.get_screenshot_as_file('./截图保存的信息/自动导入学员.png') #截图保留证据
        self.driver.quit()

    def run(self):
        self.login()
        self.driver.implicitly_wait(3)
        self.add_students()









if __name__ == '__main__':
    my = My()
    my.run()