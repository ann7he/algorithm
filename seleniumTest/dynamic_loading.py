from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))

try:
    # 打开动态加载页面
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
    # 找到start按钮并点击
    start_button = driver.find_element(By.CSS_SELECTOR, '#start button')
    start_button.click()

    # 等待页面加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#finish h4'))
    )
    # 打印成功消息
    finish_text = driver.find_element(By.CSS_SELECTOR, '#finish h4').text
    print(finish_text)
finally:
    # 关闭浏览器
    driver.quit()
