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
    driver.get('http://the-internet.herokuapp.com/upload')
    # 上传文件
    file_input = driver.find_element(By.ID, 'file-upload')
    file_input.send_keys(r'D:\DELL\Pictures\html图片素材\顶部.png')

    # 点击上传按钮
    upload_button = driver.find_element(By.ID, 'file-submit')
    upload_button.click()

    # 等待上传完成
    success_message = driver.find_element(By.CSS_SELECTOR, '.example h3').text
    print(success_message)
finally:
    # 关闭浏览器
    driver.quit()
