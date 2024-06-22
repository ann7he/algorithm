from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


# 初始化WebDriver
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))
try:
    # 打开DemoQA的Automation Practice Form页面
    driver.get('https://demoqa.com/automation-practice-form')

    # 等待页面加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'firstName'))
    )
    driver.maximize_window()

    # 填写表单
    driver.find_element(By.ID, 'firstName').send_keys('Ann')
    driver.find_element(By.ID, 'lastName').send_keys('He')
    driver.find_element(By.ID, 'userEmail').send_keys('Ann@example.com')

    # 选择性别
    driver.find_element(By.XPATH, '//label[contains(text(),"Male")]').click()

    # 输入手机号码
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')

    # 处理日期选择器
    driver.find_element(By.ID, 'dateOfBirthInput').click()
    Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')).select_by_visible_text('June')
    Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')).select_by_visible_text('2024')
    driver.find_element(By.XPATH, '//div[contains(text(),"2")]').click()

    # 选择专业
    subjects = ['Maths', 'Physics', 'Computer Science']
    subject_input = driver.find_element(By.ID, 'subjectsInput')

    for subject in subjects:
        subject_input.send_keys(subject[:3])  # 输入部分文本，触发自动完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            f"//div[contains(@class, 'subjects-auto-complete__menu')]//div[contains(text(), '{subject}')]"))
        )
        suggestion = driver.find_element(By.XPATH,
                                         f"//div[contains(@class, 'subjects-auto-complete__menu')]//div[contains(text(), '{subject}')]")
        suggestion.click()

    # 选择爱好
    driver.find_element(By.XPATH, '//label[contains(text(), "Sports")]').click()

    # 上传图片
    driver.find_element(By.ID, 'uploadPicture').send_keys(r'D:\DELL\Pictures\html图片素材\animation-1297198_1280.png')

    # 输入地址
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, Anytown, USA')

    # 选择州和城市
    driver.find_element(By.XPATH, '//div[contains(text(), "Select State")]').click()
    driver.find_element(By.XPATH, '//div[contains(text(), "NCR")]').click()
    driver.find_element(By.XPATH, '//div[contains(text(), "Select City")]').click()
    driver.find_element(By.XPATH, '//div[contains(text(), "Delhi")]').click()

    # 滚动到提交按钮可见位置
    submit_button = driver.find_element(By.ID, 'submit')
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    # 等待提交按钮可见
    WebDriverWait(driver, 10).until(EC.visibility_of(submit_button))

    # 提交表单
    submit_button.click()

    # 等待表单提交后的弹窗
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'example-modal-sizes-title-lg'))
    )
    print("Form submitted successfully!")

finally:
    # 关闭浏览器
    driver.quit()
