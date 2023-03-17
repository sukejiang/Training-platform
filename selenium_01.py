from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #获取浏览器控制

driver.get('https://baidu.com') #获取网页的地址

driver.maximize_window() #最大化浏览器

driver.refresh()  #刷新浏览器

# driver.back()  #返回上一页
#
# driver.forward() #前进

title = driver.title
print("标题：",title)

driver.get_screenshot_as_file('百度首页.png') #截图网页

html = driver.page_source

print("源码：",html)  #获取源码

driver.find_element(By.ID,"")
driver.quit()