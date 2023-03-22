import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class My():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr') 获取所有单元长度

    def login(self):  # 获取登录页面并截图保存
        self.driver.get("https://dev.znk.group/training/manage.htm")
        self.driver.maximize_window()
        self.driver.find_element(By.ID,'txtuserid').send_keys("江啟锋")
        time.sleep(1)
        self.driver.find_element(By.ID,'txtpassword').send_keys("jqf123456")
        self.driver.find_element(By.ID,"btnLogin").click()
        self.driver.get_screenshot_as_file("./截图保存的信息/登录页面的信息.png")


    def addInstitutions(self):  #完成新增机构功能(脚本运行时间9秒)
        self.driver.find_element(By.XPATH,'//*[@id="navigator"]/ul/li[2]').click() #获取机构管理页面
        elementi = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(elementi) #跳转到iframe窗口
        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/button').click() #点击新增按钮
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID,'txtOName').send_keys('自动新增机构')  #新增机构名称
        self.driver.find_element(By.ID,'txtOMemo').send_keys('自动增加测试描述') #新增机构描述
        self.driver.find_element(By.XPATH,'//*[@id="dlgOrganization"]/div[3]/a[2]').click() #确定新增机构
        time.sleep(1)
        self.driver.get_screenshot_as_file("./截图保存的信息/自动添加机构.png")
        self.driver.quit()
    def run(self):
        self.login()
        self.driver.implicitly_wait(3)
        self.addInstitutions()

if __name__ == '__main__':
    my = My()
    my.run()