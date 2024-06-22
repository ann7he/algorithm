import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PetstoreCartTest(unittest.TestCase):
    def setUp(self):
        # 初始化WebDriver
        self.driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))
        self.driver.get('https://petstore.octoperf.com/')
        self.login()

    def login(self):
        driver = self.driver
        # 等待并点击进入按钮
        enter_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Enter the Store"))
        )
        enter_link.click()

        # 点击登录
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign In"))
        ).click()

        # 输入用户名和密码
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        username.clear()
        password.clear()
        username.send_keys('j2ee')
        password.send_keys('j2ee')

        # 提交登录表单
        driver.find_element(By.NAME, "signon").click()

        # 检查是否登录成功
        welcome_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='WelcomeContent']"))
        )
        self.assertIn("Welcome", welcome_message.text)
        print("Login successful")

    def add_item_to_cart(self, category, item_link_text):
        driver = self.driver
        # 添加产品到购物车
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@id='QuickLinks']//a[contains(@href, '{category}')]"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, item_link_text))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Add to Cart"))
        ).click()

        # 返回主菜单
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Return to Main Menu"))
        ).click()

        print(f"Added {item_link_text} to cart from category {category}")

    def test_cart_operations(self):
        driver = self.driver

        # 添加两个商品到购物车
        self.add_item_to_cart('FISH', 'FI-SW-01')
        self.add_item_to_cart('DOGS', 'K9-BD-01')

        # 打开购物车页面
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "img_cart"))
        ).click()

        print("Opened cart page")

        # 确保购物车页面已加载，并且有商品
        item_quantities = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[@type='text' and contains(@name, 'EST-')]"))
        )

        print("Found item quantity fields:", len(item_quantities))

        # 更新购物车商品数量
        for quantity_field in item_quantities:
            quantity_field.clear()
            quantity_field.send_keys('2')

        # 点击更新购物车按钮
        driver.find_element(By.NAME, 'updateCartQuantities').click()

        print("Updated cart quantities")

        # 获取每个商品的数量和价格并计算总金额
        item_rows = driver.find_elements(By.XPATH, "//td/input[contains(@name, 'EST-')]/ancestor::tr")
        total_price = 0
        for row in item_rows:
            quantity = int(row.find_element(By.TAG_NAME, "input").get_attribute("value"))
            price = float(row.find_elements(By.TAG_NAME, "td")[1].text.strip('$'))
            total_price += price * quantity

        cart_total = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[@align='right']"))
        ).text.strip('$')
        cart_total = float(cart_total)

        print(f"Total calculated price: {total_price}, Cart total from page: {cart_total}")

        # self.assertAlmostEqual(total_price, cart_total, places=2)

        # 删除购物车中的商品
        for quantity_field in item_quantities:
            quantity_field.clear()
            quantity_field.send_keys('0')

        driver.find_element(By.NAME, 'updateCartQuantities').click()

        print("Cleared cart quantities")

        # 验证购物车为空
        empty_cart_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='Cart']//p"))
        )
        self.assertIn('Your cart is empty', empty_cart_message.text)

        print("Cart is empty")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
