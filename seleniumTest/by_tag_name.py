from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))
# chrome_driver
driver.maximize_window()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址driver.get('https://www.baidu.com')
driver.get('https://www.bilibili.com/')

# 只获取属性的第一个元素
# driver.find_element(By.NAME, 'nav-search-input').send_keys('至诚学院')

# driver.find_element(By.LINK_TEXT, '番剧').click()

driver.find_element(By.PARTIAL_LINK_TEXT, '游').click()

input('等待回车键结束程序')
