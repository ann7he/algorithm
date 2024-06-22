from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置ChromeDriver的路径

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))

try:
    # 打开Google
    driver.get('https://www.google.com')

    # 查找搜索框并输入文本
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Selenium tutorial')

    # 查找搜索按钮并点击
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'btnK'))
    )
    search_button.click()

    # 等待搜索结果加载并获取标题
    WebDriverWait(driver, 10).until(EC.title_contains('Selenium tutorial'))
    print(driver.title)

finally:
    # 关闭浏览器
    driver.quit()
