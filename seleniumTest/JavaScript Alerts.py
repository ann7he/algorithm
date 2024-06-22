from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))

try:
    # 打开The Internet主页
    driver.get('http://the-internet.herokuapp.com/')

    # 测试弹窗处理
    # 打开JavaScript Alerts页面
    js_alerts_link = driver.find_element(By.LINK_TEXT, 'JavaScript Alerts')
    js_alerts_link.click()

    # 等待JavaScript Alerts页面加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Click for JS Alert']"))
    )

    # 处理JS Alert
    js_alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    js_alert_button.click()

    # 切换到alert并接受
    alert = driver.switch_to.alert
    print(f"Alert text: {alert.text}")
    alert.accept()
    print("Alert accepted!")

    # 处理JS Confirm
    js_confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    js_confirm_button.click()

    # 切换到confirm并接受
    confirm = driver.switch_to.alert
    print(f"Confirm text: {confirm.text}")
    confirm.accept()
    print("Confirm accepted!")

    # 处理JS Prompt
    js_prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
    js_prompt_button.click()

    # 切换到prompt并输入文本，然后接受
    prompt = driver.switch_to.alert
    print(f"Prompt text: {prompt.text}")
    prompt.send_keys("Test input")
    prompt.accept()
    print("Prompt accepted with input!")

finally:
    # 关闭浏览器
    driver.quit()
