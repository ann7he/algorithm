from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))

try:
    # 打开SauceDemo主页
    driver.get('https://www.saucedemo.com/')
    # 输入用户名和密码
    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    # 提交登录表单
    password.send_keys(Keys.RETURN)
    time.sleep(3)
    # 检查是否登录成功
    products_title = driver.find_element(By.CLASS_NAME, 'title')
    print(products_title)
    # 添加产品到购物车当中
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()

    # 打开购物车
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    # 等待购物车加载
    time.sleep(3)
    # 检查购物车中是否有产品
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    print(f"Number of items: {len(cart_items)}")
    # 点击Checkout按钮
    checkout_button = driver.find_element(By.ID, 'checkout')
    checkout_button.click()
    time.sleep(3)
    # 等待结账信息
    first_name = driver.find_element(By.ID, 'first-name')
    last_name = driver.find_element(By.ID, 'last-name')
    postal_code = driver.find_element(By.ID, 'postal-code')
    first_name.send_keys('he')
    last_name.send_keys('anqi')
    postal_code.send_keys('zc123456')
    # 点击继续
    driver.find_element(By.ID, 'continue').click()
    # 等待页面订单加载
    time.sleep(3)
    # 验证订单信息
    item_total = driver.find_element(By.CLASS_NAME, 'summary_subtotal_label').text
    print(f"Item total:{item_total}")
    # 点击完成按钮
    driver.find_element(By.ID, 'finish').click()
    # 等待页面完成加载
    time.sleep(3)
    # 验证完成页面
    complete_header = driver.find_element(By.CLASS_NAME, 'complete-header').text
    print(f"Order complete: {complete_header}")  # 输出完成订单信息
finally:
    # 关闭浏览器
    driver.quit()
