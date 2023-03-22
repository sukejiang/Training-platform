from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class My():  #完成新增用户操作
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):  # 获取登录页面
        self.driver.get("https://dev.znk.group/training/manage.htm")
        self.driver.maximize_window()
        self.driver.find_element(By.ID,'txtuserid').send_keys("江啟锋")
        time.sleep(1)
        self.driver.find_element(By.ID,'txtpassword').send_keys("jqf123456")
        self.driver.find_element(By.ID,"btnLogin").click()

    def addUser(self):

        self.driver.find_element(By.XPATH,'//*[@id="navigator"]/ul/li[3]').click() #获取用户管理标签页
        self.driver.implicitly_wait(3)
        element = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(element)          #跳转到标签页
        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/button').click() #点击新增按钮
        self.driver.find_element(By.ID,'inpUserCode').send_keys('邓某') #登录账号
        self.driver.find_element(By.ID, 'txtUName').send_keys('邓仁')  #用户姓名
        self.driver.find_element(By.ID, 'txtUMail').send_keys('test@znk.com') #用户邮箱2ww
        self.driver.find_element(By.ID, 'txtUMobile').send_keys('13104976109') #用户手机号
        self.driver.find_element(By.ID,'btnAddRole').click()  #打开角色栏
        self.driver.find_element(By.XPATH,'//*[@id="dgRole"]/label[2]/div[1]').click() #选择角色
        self.driver.find_element(By.XPATH,'//*[@id="dlgRoleSelect"]/div[3]/a[2]').click() #确定角色
        self.driver.find_element(By.XPATH,'//*[@id="dlgUserEdit"]/div[3]/a[2]').click() #确定创建
        time.sleep(1)
        self.driver.get_screenshot_as_file('./截图保存的信息/自动生成的用户.png')
        self.driver.quit()


    def run(self):  #运行所有函数
        self.login()
        self.driver.implicitly_wait(3)
        self.addUser()







if __name__ == '__main__':
    my = My()
    my.run()