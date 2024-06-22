from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))


try:
    # 打开网页
    driver.get('https://infinite-scroll.com/demo/full-page/')  # 将URL替换为实际的无限滚动网页地址

    # 重复滚动直到特定条件满足或达到最大滚动次数
    max_scrolls = 10
    for i in range(max_scrolls):
        # 滚动到页面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 等待新内容加载
        time.sleep(2)  # 实际情况下，可根据网络速度和服务器响应速度调整

        # 检查新内容是否存在
        new_elements = driver.find_elements(By.CSS_SELECTOR, '.new-element-class')  # 替换CSS选择器以匹配新内容
        if new_elements:
            print(f"Loaded new content after {i+1} scrolls.")
            break

finally:
    # 关闭浏览器
    driver.quit()
