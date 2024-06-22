from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))
# chrome_driver
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址driver.get('https://www.baidu.com')
driver.get('https://www.baidu.com')
# 程序运行完会自动关闭浏览器，就是很多人说的闪退
# 这里加入等待用户输入，防止闪退
driver.find_element(By.ID, 'kw').send_keys('python')
input('等待回车键结束程序')
