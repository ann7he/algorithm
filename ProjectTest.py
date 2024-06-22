import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class ProjectTest(unittest.TestCase):
    def setUp(self):
        # 初始化WebDriver
        self.driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))
        self.driver.get('http://localhost:5173')
        time.sleep(3)  # 等待页面加载完成
        self.driver.maximize_window()

    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

    # 辅助方法
    def login(self, username, password):
        # 输入用户名和密码
        username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
        username_input.clear()
        password_input.clear()
        username_input.send_keys(username)
        password_input.send_keys(password)

        # 提交登录表单
        self.driver.find_element(By.CLASS_NAME, "el-button--primary").click()

    # 测试用例
    def test_login(self):
        # 登录测试1：用户名的长度不够
        self.login('何安琪', '12345')
        self.verify_username_password_error('长度为5~16非空字符')
        time.sleep(2)

        # 登录测试2：输入错误的用户名密码
        self.login('何安琪123', '12345')
        self.verify_message('服务异常')
        time.sleep(2)

        # 登录测试3：输入正确的用户名和密码
        self.login('何安琪123', '123456')
        self.verify_successful_login()
        time.sleep(2)

    def verify_username_password_error(self, expected_message):
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "el-form-item__error"))
            )
            self.assertEqual(error_message.text, expected_message, f"错误提示出现: {expected_message}")
        except Exception as e:
            self.fail(f"错误提示未出现: {e}")

    def verify_message(self, expected_message):
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "el-message__content"))
            )
            self.assertEqual(error_message.text, expected_message, f"服务异常弹窗出现: {expected_message}")
        except Exception as e:
            self.fail(f"服务异常弹窗未出现: {e}")

    def verify_successful_login(self, who, name):
        """
        Verify whether the login was successful.
        :param who: A unique identifier for the user (e.g., role or status text in the div element).
        :param name: The name of the user to look for in the strong tag.
        """
        # 等待登录结果加载
        time.sleep(3)

        try:
            # Build the XPath expression dynamically with provided 'who' and 'name'
            xpath_expression = f"//div[contains(text(), '{who}')]//strong[contains(text(), '{name}')]"

            # Locate the student info element
            student_info = self.driver.find_element(By.XPATH, xpath_expression)

            # Assert that the student info element is found
            self.assertIsNotNone(student_info, "登录成功")
        except NoSuchElementException:
            self.fail("登录失败: 无法找到指定的元素")
        except Exception as e:
            self.fail(f"登录失败: 发生异常 {e}")

    # 登录成功后验证用户通用功能是否正常
    def test_user_module(self):
        self.login('何安琪123', '123456')
        time.sleep(3)  # 等待登录完成
        self.verify_successful_login('何安琪123', '123456')
        # 通用模块（通过头部/菜单栏）
        # 修改基本资料
        # 更换头像
        # 重置密码
        # 退出登录

        # 等待悬浮菜单出现，可以使用显式等待
        dropdown_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "el-dropdown__box"))
        )

        # 使用 ActionChains 类来模拟鼠标悬停操作
        action = ActionChains(self.driver)
        action.move_to_element(dropdown_menu).perform()

        # 等待菜单项出现，例如等待退出登录按钮可点击
        logout_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "退出登录")]'))
        )

        # 点击退出登录按钮
        logout_button.click()
        # 等待退出登录操作完成，可以添加相应的断言或者验证

    # 验证学生模块特有功能是否正常
    def test_student_module(self):
        self.login('何安琪123', '123456')
        time.sleep(3)  # 等待登录完成
        self.verify_successful_login('何安琪123', '123456')
        # 1、查看我的信息
        # 显式等待菜单出现
        try:
            my_info_menu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '我的信息')]"))
            )
            my_info_menu.click()
        except Exception as e:
            self.fail(f"无法找到我的信息菜单: {e}")

        # 等待页面加载
        time.sleep(2)

        # 验证模块内容是否正确
        try:
            # 检查是否包含姓名和专业
            student_name = self.driver.find_element(By.XPATH, "//td[contains(text(), '何安琪')]")
            major = self.driver.find_element(By.XPATH, "//td[contains(text(), '软件工程')]")

            self.assertIsNotNone(student_name, "姓名存在")
            self.assertIsNotNone(major, "专业存在")

        except Exception as e:
            self.fail(f"验证模块内容失败: {e}")

        # 2、查看我的宿舍

        my_room = self.driver.find_element(By.XPATH, "//span[contains(text(), '我的宿舍')]")
        my_room.click()

        # 等待页面加载
        time.sleep(2)

        # 验证模块内容是否正确
        try:
            # 检查是否包含楼号和宿舍号
            roomID = self.driver.find_element(By.XPATH, "//td[contains(text(), '东三321')]")
            Building = self.driver.find_element(By.XPATH, "//td[contains(text(), '学生公寓')]")
            admin = self.driver.find_element(By.XPATH, "//td[contains(text(), '大婶')]")

            self.assertIsNotNone(admin, "admin存在")
            self.assertIsNotNone(roomID, "宿舍号存在")
            self.assertIsNotNone(Building, "楼号存在")

        except Exception as e:
            self.fail(f"验证模块内容失败: {e}")

        # 3、缴纳电费

        my_pay = self.driver.find_element(By.XPATH, "//span[contains(text(), '缴纳电费')]")
        my_pay.click()

        # 等待页面加载
        time.sleep(2)

        # 2.1查看电费列表是否正常显示，分页功能正常
        # 验证模块内容是否正确
        try:
            # 检查是否包含楼号和宿舍号
            payList = self.driver.find_element(By.XPATH, "//span[contains(text(), '水电费清单')]")
            payId = self.driver.find_element(By.XPATH, "//div[contains(text(), '记录号')]")
            self.assertIsNotNone(payList, "水电费清单存在")
            self.assertIsNotNone(payId, "记录号存在")

            # 找到所有匹配的输入框元素
            input_elements = self.driver.find_elements(By.CLASS_NAME, "el-input__inner")
            # 获取第二个输入框元素
            second_input_element = input_elements[1]

            # 分页测试
            # 点击输入框# 向下按键4次
            second_input_element.click()
            for _ in range(4):
                second_input_element.send_keys(Keys.ARROW_DOWN)
                # 按下回车键
            second_input_element.send_keys(Keys.ENTER)
            time.sleep(3)
        except Exception as e:
            self.fail(f"验证模块内容失败: {e}")

        # 2.2缴纳未缴纳的电费
        # 找到第一个具有特定样式的按钮元素
        button_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                    "button.el-button.el-button--warning.is-plain.is-circle")
        # 点击第一个按钮
        button_elements[0].click()
        time.sleep(1)

        # 获取弹窗中的文本内容
        message_text = self.driver.find_element(By.XPATH, "//div[@class='el-message-box__message']/p").text
        # 验证文本内容是否正确
        expected_message = "你确认支付？"
        self.assertEqual(message_text, expected_message, f"弹窗消息内容不正确: {message_text}")

        # 2.2.1确认支付？取消
        cancel_button = self.driver.find_element(By.XPATH, "//button[contains(span, '取消')]")
        cancel_button.click()

        time.sleep(1)

        # 2.2.2确认支付？确认
        # 点击第一个按钮
        button_elements[0].click()
        time.sleep(1)
        # 获取弹窗中的文本内容
        message_text = self.driver.find_element(By.XPATH, "//div[@class='el-message-box__message']/p").text
        # 验证文本内容是否正确
        expected_message = "你确认支付？"
        self.assertEqual(message_text, expected_message, f"弹窗消息内容不正确: {message_text}")
        identify_button = self.driver.find_element(By.XPATH, "//button[contains(span, '确定')]")
        identify_button.click()

        # 3、访客登记

        # 访问访客登记模块
        visitor = self.driver.find_element(By.XPATH, "//span[contains(text(), '访客登记')]")
        visitor.click()
        time.sleep(3)

        # 验证访客列表
        try:
            payList = self.driver.find_element(By.XPATH, "//span[contains(text(), '访客列表')]")
            payId = self.driver.find_element(By.XPATH, "//div[contains(text(), '记录号')]")
            self.assertIsNotNone(payList, "访客列表存在")
            self.assertIsNotNone(payId, "记录号存在")
        except Exception as e:
            self.fail(f"验证访客列表内容失败: {e}")

        # 进行访客登记
        button = self.driver.find_element(By.XPATH, "//button[span[text()='访客登记']]")
        button.click()

        input_elements = self.driver.find_elements(By.CLASS_NAME, "el-input__inner")

        # 填写错误的访客信息
        id1 = input_elements[0]
        stuNo = input_elements[1]
        stuName = input_elements[2]
        people = input_elements[3]

        id1.clear()
        stuNo.clear()
        stuName.clear()
        people.clear()

        id1.send_keys("787878")
        stuNo.send_keys("787878")
        stuName.send_keys("何安琪123")
        people.send_keys("Lily")

        yes_button = self.driver.find_element(By.XPATH, "//button[contains(span, '确认')]")
        time.sleep(2)
        yes_button.click()
        self.verify_message('服务异常')

        # 填写正确的访客信息
        id1.clear()
        stuNo.clear()
        stuName.clear()
        people.clear()

        time.sleep(1)
        id1.send_keys("5445454")
        stuNo.send_keys("212106282")
        stuName.send_keys("何安琪")
        people.send_keys("Lily345")

        yes_button.click()
        time.sleep(2)
        self.verify_message('添加成功')

        # 访问访客登记模块
        visitor = self.driver.find_element(By.XPATH, "//span[contains(text(), '访客登记')]")
        visitor.click()
        time.sleep(3)

        # 4.1验证报修列表
        repair = self.driver.find_element(By.XPATH, "//span[contains(text(), '报修申请')]")
        repair.click()
        time.sleep(3)

        try:
            dorList = self.driver.find_element(By.XPATH, "//span[contains(text(), '宿舍财产')]")
            dorId = self.driver.find_element(By.XPATH, "//div[contains(text(), '财产号')]")
            self.assertIsNotNone(dorList, "宿舍财产存在")
            self.assertIsNotNone(dorId, "财产号存在")
            # 分页测试
            # 找到所有匹配的输入框元素
            input_elements = self.driver.find_elements(By.CLASS_NAME, "el-input__inner")
            # 获取第二个输入框元素
            second_input_element = input_elements[1]
            # 点击输入框# 向下按键4次
            second_input_element.click()
            for _ in range(4):
                second_input_element.send_keys(Keys.ARROW_DOWN)
                # 按下回车键
                time.sleep(1)
            time.sleep(2)
            second_input_element.send_keys(Keys.ENTER)
            time.sleep(3)

        except Exception as e:
            self.fail(f"验证报修列表内容失败: {e}")

        # 4.2申请报修
        # 找到第一个具有特定样式的按钮元素
        button_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                    "button.el-button.el-button--success.is-plain.is-circle")
        # button_elements = self.driver.find_elements(By.CSS_SELECTOR,
        #                                             "button.el-button.el-button--warning.is-plain.is-circle")
        # 点击第一个按钮
        button_elements[0].click()
        time.sleep(1)

        # 获取弹窗中的文本内容
        message_text = self.driver.find_element(By.XPATH, "//div[@class='el-message-box__message']/p").text
        # 验证文本内容是否正确
        expected_message = "你确认申请报修？"
        self.assertEqual(message_text, expected_message, f"弹窗消息内容不正确: {message_text}")

        # 2.2.1确认支付？取消
        cancel_button = self.driver.find_element(By.XPATH, "//button[contains(span, '取消')]")
        cancel_button.click()
        time.sleep(2)
        self.verify_message('取消报修')
        time.sleep(1)

        # 2.2.2确认支付？确认
        # 点击第一个按钮
        button_elements[0].click()
        time.sleep(1)
        # 获取弹窗中的文本内容
        message_text = self.driver.find_element(By.XPATH, "//div[@class='el-message-box__message']/p").text
        # 验证文本内容是否正确
        self.assertEqual(message_text, expected_message, f"弹窗消息内容不正确: {message_text}")
        identify_button = self.driver.find_element(By.XPATH, "//button[contains(span, '确定')]")
        time.sleep(1)
        identify_button.click()

    # 验证管理员模块模块特有功能是否正常
    def test_admin_module(self):
        self.login('Tomss', '123456')
        time.sleep(3)  # 等待登录完成
        self.verify_successful_login('Tomss', '123456')
        # 1、查看我的信息
        # 显式等待菜单出现
        try:
            my_info_menu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '我的信息')]"))
            )
            my_info_menu.click()
        except Exception as e:
            self.fail(f"无法找到我的信息菜单: {e}")

    # 验证水电工模块特有功能是否正常
    def test_engineer_module(self):
        self.login('fancy', '123456')
        time.sleep(3)  # 等待登录完成
        self.verify_successful_login('水电工', 'fan')
        # 1、维修管理
        # 显式等待菜单出现
        # try:
        #     repair_menu = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '维修管理')]"))
        #     )
        #     repair_menu.click()
        # except Exception as e:
        #     self.fail(f"无法找到我的维修管理: {e}")
        #
        # # 等待页面加载
        # time.sleep(2)
        #
        # # 验证模块内容是否正确
        # try:
        #     # 检查是否包含"维修ID"和"宿舍号"
        #     repair_id_element = self.driver.find_element(By.XPATH,
        #                                                  "//div[contains(@class, 'cell') and contains(text(), '维修ID')]")
        #     dorm_number_element = self.driver.find_element(By.XPATH,
        #                                                    "//div[contains(@class, 'cell') and contains(text(), '宿舍号')]")
        #
        #     self.assertIsNotNone(repair_id_element, "维修ID存在")
        #     self.assertIsNotNone(dorm_number_element, "宿舍号存在")
        #
        #     # 找到所有匹配的输入框元素
        #     input_elements = self.driver.find_elements(By.CLASS_NAME, "el-input__inner")
        #
        #     # 获取第1个个输入框元素
        #     firth_input_element = input_elements[0]
        #     # 获取第2个个输入框元素
        #     second_input_element = input_elements[1]
        #     # 获取第3个个输入框元素
        #     third_input_element = input_elements[2]
        #     # 获取第4个个输入框元素
        #     forth_input_element = input_elements[3]
        #
        #     reset_btn = self.driver.find_element(By.XPATH,
        #                                          "//button[contains(@class, 'el-button')]//span[text()='重置']")
        #
        #     search_btn = self.driver.find_element(By.XPATH,
        #                                           "//button[contains(@class, 'el-button') and contains(@class, "
        #                                           "'el-button--primary')"
        #                                           "and contains(span, '搜索')]")
        #
        #     firth_input_element.click()
        #     for _ in range(2):
        #         firth_input_element.send_keys(Keys.ARROW_DOWN)
        #         # 按下回车键
        #     firth_input_element.send_keys(Keys.ENTER)
        #     search_btn.click()
        #     time.sleep(3)
        #     reset_btn.click()
        #     time.sleep(1)
        #     search_btn.click()
        #     time.sleep(2)
        #
        #     second_input_element.click()
        #     for _ in range(2):
        #         second_input_element.send_keys(Keys.ARROW_DOWN)
        #         # 按下回车键
        #     second_input_element.send_keys(Keys.ENTER)
        #     search_btn.click()
        #     time.sleep(3)
        #     reset_btn.click()
        #     time.sleep(1)
        #     search_btn.click()
        #     time.sleep(2)
        #
        #     third_input_element.clear()
        #     time.sleep(1)
        #     third_input_element.click()
        #     second_input_element.send_keys("2")
        #     time.sleep(1)
        #     second_input_element.send_keys(Keys.ENTER)
        #     time.sleep(1)
        #
        #     # 分页测试
        #     # 点击输入框# 向下按键4次
        #     forth_input_element.click()
        #     for _ in range(4):
        #         forth_input_element.send_keys(Keys.ARROW_DOWN)
        #         # 按下回车键
        #     forth_input_element.send_keys(Keys.ENTER)
        #
        #     time.sleep(3)
        #
        #     # 测试每行的按钮是否可用
        #
        #     info_btn = self.driver.find_elements(By.CSS_SELECTOR,
        #                                          "button.el-button.el-button--info.is-plain.is-circle.el"
        #                                          "-tooltip__trigger")
        #     # 点击第一个按钮
        #     info_btn[0].click()
        #     time.sleep(3)
        #
        #     danger_btn = self.driver.find_elements(By.CSS_SELECTOR,
        #                                            "button.el-button.el-button--danger.is-plain.is-circle")
        #     # 点击第一个按钮
        #     danger_btn[0].click()
        #     time.sleep(1)
        #
        #     # 获取弹窗中的文本内容
        #     message = self.driver.find_element(By.XPATH, "//div[@class='el-message-box__message']/p").text
        #     # 验证文本内容是否正确
        #     expected = "你确认要删除该宿舍信息吗"
        #     self.assertEqual(message, expected, f"弹窗消息内容不正确: {message}")
        #     identify_btn = self.driver.find_element(By.XPATH, "//button[contains(span, '确定')]")
        #     identify_btn.click()
        #     time.sleep(10)
        #
        #     warning_btn = self.driver.find_elements(By.CSS_SELECTOR,
        #                                             "button.el-button.el-button--warning.is-plain.is-circle")
        #     # 点击第一个按钮
        #     warning_btn[0].click()
        #     time.sleep(1)
        #     # 获取弹窗中的文本内容
        #     message = self.driver.find_element(By.XPATH, "//div[@class='el-message-box__message']/p").text
        #     # 验证文本内容是否正确
        #     expected = "你确认已报修？"
        #     self.assertEqual(message, expected, f"弹窗消息内容不正确: {message}")
        #     identify_btn = self.driver.find_element(By.XPATH, "//button[contains(span, '确定')]")
        #     identify_btn.click()
        #
        # except Exception as e:
        #     self.fail(f"验证模块内容失败: {e}")

        # 2、电费管理

        ele_menu = self.driver.find_element(By.XPATH, "//span[contains(text(), '电费管理')]")
        ele_menu.click()
        # 等待页面加载
        time.sleep(2)

        # 验证模块内容是否正确
        try:
            # 检查是否包含"维修ID"和"宿舍号"
            repair_id_element = self.driver.find_element(By.XPATH,
                                                         "//div[contains(@class, 'cell') and contains(text(), '记录号')]")
            dorm_number_element = self.driver.find_element(By.XPATH,
                                                           "//div[contains(@class, 'cell') and contains(text(), '宿舍号')]")

            self.assertIsNotNone(repair_id_element, "记录号存在")
            self.assertIsNotNone(dorm_number_element, "宿舍号存在")

            # 找到所有匹配的输入框元素
            input_elements = self.driver.find_elements(By.CLASS_NAME, "el-input__inner")

            # 获取第1个个输入框元素
            firth_input_element = input_elements[0]
            # 获取第2个个输入框元素
            second_input_element = input_elements[1]
            # 获取第3个个输入框元素
            third_input_element = input_elements[2]
            # 获取第4个个输入框元素
            forth_input_element = input_elements[3]
            # 重置按钮
            # 显式等待包含特定类名的按钮加载（最多等待10秒）

            # 遍历找到文本为'重置'和'搜索'的按钮

            reset_btn = self.driver.find_element(By.XPATH,
                                                 "//button[contains(@class, 'el-button')]//span[text()='重置']")

            search_btn = self.driver.find_element(By.XPATH,
                                                  "//button[contains(@class, 'el-button') and contains(@class, "
                                                  "'el-button--primary')"
                                                  "and contains(span, '搜索')]")

            # 分页测试
            # 点击输入框# 向下按键4次
            forth_input_element.click()
            for _ in range(4):
                forth_input_element.send_keys(Keys.ARROW_DOWN)
                # 按下回车键
            forth_input_element.send_keys(Keys.ENTER)
            time.sleep(3)

            firth_input_element.click()
            for _ in range(2):
                firth_input_element.send_keys(Keys.ARROW_DOWN)
                # 按下回车键

            third_input_element.clear()
            time.sleep(1)
            third_input_element.click()
            second_input_element.send_keys("2")
            time.sleep(1)
            second_input_element.send_keys(Keys.ENTER)
            time.sleep(1)

            firth_input_element.send_keys(Keys.ENTER)
            search_btn.click()
            time.sleep(3)
            reset_btn.click()
            time.sleep(1)
            search_btn.click()
            time.sleep(2)

            second_input_element.click()
            for _ in range(2):
                second_input_element.send_keys(Keys.ARROW_DOWN)
                # 按下回车键
            second_input_element.send_keys(Keys.ENTER)
            search_btn.click()
            time.sleep(3)
            reset_btn.click()
            time.sleep(1)
            search_btn.click()
            time.sleep(2)

            # 测试每行的按钮是否可用

            warning_button = self.driver.find_elements(By.CSS_SELECTOR,
                                                       "button.el-button.el-button--warning.is-plain.is-circle")
            # 点击第一个按钮
            warning_button[0].click()
            time.sleep(1)
            # 获取弹窗中的文本内容
            message_text = self.driver.find_element(By.XPATH, "//div[@class='el-message-box__message']/p").text
            # 验证文本内容是否正确
            expected_message = "确认提醒该宿舍成员缴纳电费"
            self.assertEqual(message_text, expected_message, f"弹窗消息内容不正确: {message_text}")
            identify_button = self.driver.find_element(By.XPATH, "//button[contains(span, '确定')]")
            identify_button.click()
            time.sleep(2)

            danger_button = self.driver.find_elements(By.CSS_SELECTOR,
                                                      "button.el-button.el-button--danger.is-plain.is-circle")
            # 点击第一个按钮
            danger_button[0].click()
            time.sleep(1)

            # 获取弹窗中的文本内容
            message_text = self.driver.find_element(By.XPATH, "//div[@class='el-message-box__message']/p").text
            # 验证文本内容是否正确
            expected_message = "你确认要删除该财产信息吗"
            self.assertEqual(message_text, expected_message, f"弹窗消息内容不正确: {message_text}")
            identify_button = self.driver.find_element(By.XPATH, "//button[contains(span, '确定')]")
            identify_button.click()


        except Exception as e:
            self.fail(f"验证模块内容失败: {e}")


if __name__ == "__main__":
    unittest.main()
