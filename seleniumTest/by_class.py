from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.page_load_strategy = 'eager'

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))
# chrome_driver
driver.maximize_window()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址driver.get('https://www.baidu.com')
driver.get('https://www.bilibili.com/')
# 程序运行完会自动关闭浏览器，就是很多人说的闪退
# 根据 class name 选择元素，返回的是一个判表
# 里面都是class属性值为xxxx的元素的，WebElement的对象
driver.find_element(By.CLASS_NAME,'channel-link').click()

# driver.find_element(By.CLASS_NAME,'channel-link')[1].click()


# elements = driver.find_elements(By.CLASS_NAME, 'channel-link')
# 遍历所有符合条件的元素并逐个点击
# for element in elements:
#     element.click()

input('等待回车键结束程序')
