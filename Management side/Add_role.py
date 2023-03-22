from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class My():  #完成新建用户操作
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):  # 获取登录页面
        self.driver.get("https://dev.znk.group/training/manage.htm")
        self.driver.maximize_window()
        self.driver.find_element(By.ID,'txtuserid').send_keys("江啟锋")
        time.sleep(1)
        self.driver.find_element(By.ID,'txtpassword').send_keys("jqf123456")
        self.driver.find_element(By.ID,"btnLogin").click()

    def addrole(self):
        self.driver.find_element(By.XPATH, '//*[@id="navigator"]/ul/li[4]').click()  # 获取用户管理标签页
        self.driver.implicitly_wait(3)
        element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(element)  # 跳转到标签页
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/button').click() #点击新增按钮
        self.driver.find_element(By.ID,'txtRoleName').send_keys('自动新增角色') #自动新增角色
        self.driver.find_element(By.ID,'txtRoleMemo').send_keys('这是通过自动化测试进行新增的项目') #新增角色描述
        self.driver.find_element(By.ID,'selectAll').click()  #给新增加的角色所有权限
        self.driver.find_element(By.XPATH,'//*[@id="dlgRoleEdit"]/div[3]/a[2]').click() #完成角色创建
        time.sleep(1)
        self.driver.get_screenshot_as_file('./截图保存的信息/自动生成的角色.png')
        self.driver.quit()
    def run(self):
        self.login()
        self.driver.implicitly_wait(3)
        self.addrole()









if __name__ == '__main__':
    my = My()
    my.run()