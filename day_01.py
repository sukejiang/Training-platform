# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# wy = webdriver.Chrome(options=options)
#
# wy.get("https://dev.znk.group/training/manage.htm")
# wy.find_element(By.ID,'txtuserid').send_keys("江啟锋")
# time.sleep(3)
# wy.find_element(By.ID,'txtpassword').send_keys("jqf123456")
# wy.find_element(By.ID,'btnLogin').click()
# time.sleep(500)
# wy.quit()
#
# from pywinauto import application
# from selenium import webdriver
#      # 进入文件上传页面的代码省略
#
# driver.find_element_by_id('upload_pic').click()   # 点击上传/浏览按钮
# sleep(2)                      # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
# app = application.Application()   # 实例化Application
# # 这里用的class而没有加窗口title，主要为了保证兼容性
# app.connect(class_name='#32770')    #根据class_name找到弹出窗口
# app["Dialog"]["Edit1"].TypeKeys("E:\\1.jpg")     # 在输入框中输入值
# app["Dialog"]["Button1"].click()                 # 点击打开/保存按钮
import os
import json
jiang = 1
current_directory = os.path.abspath('./Management side/导入的信息数据/教师导入.xls')
str = json.dumps(current_directory,ensure_ascii=0)
print(current_directory)