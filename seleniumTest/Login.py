from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))

try:
    # 打开登录界面
    driver.get('http://the-internet.herokuapp.com/login')
    # 输入用户名
    username = driver.find_element(By.ID, 'username')
    username.send_keys('tomsmith')
    # 输入密码
    password = driver.find_element(By.ID, 'password')
    password.send_keys('SuperSecretPassword!')
    # 提交表单
    password.send_keys(Keys.RETURN)
    # 等待页面加载
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'flash.success')))
    # 打印成功消息
    success_message = driver.find_element(By.CSS_SELECTOR, '.flash.success').text
    print(success_message)
finally:
    # 关闭浏览器
    driver.quit()



