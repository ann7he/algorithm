from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

title = driver.title

print(title)

# 查找单个元素
element = driver.find_element(By.NAME, 'q')
element.click()

# 查找多个元素
elements = driver.find_elements(By.TAG_NAME, 'a')

# 输入文本
element.send_keys('Selenium tutorial')

# 点击按钮
element = driver.find_element(By.NAME, 'btnK')
element.click()

# 隐式等待
driver.implicitly_wait(10)  # 等待10秒

# 显式等待
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.NAME, 'q')))

# 接受弹窗
alert = driver.switch_to.alert
alert.accept()

# 拒绝弹窗
alert.dismiss()

# 切换到iframe
driver.switch_to.frame('iframe_name')

# 切换回主内容
driver.switch_to.default_content()

# 最大化窗口
driver.maximize_window()

# 设置窗口大小
driver.set_window_size(1024, 768)

# 获取页面标题
title = driver.title

# 获取当前URL
current_url = driver.current_url

# 获取页面源代码
page_source = driver.page_source

# 截取整个页面
driver.save_screenshot('screenshot.png')

# 截取元素
element = driver.find_element(By.NAME, 'q')
element.screenshot('element_screenshot.png')

# 关闭当前标签页
driver.close()

# 关闭浏览器
driver.quit()
