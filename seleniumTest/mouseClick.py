from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 1. Create WebDriver object, specifying the use of Chrome browser driver
driver = webdriver.Chrome(service=Service(r'D:\MyApp\chromedriver-win64\chromedriver.exe'))

# Open the webpage
driver.get('https://www.baidu.com')
driver.maximize_window()

# 2. Locate the element to hover over
# driver.find_element(By.LINK_TEXT, "设置")

try:
    # Wait up to 10 seconds for the element to be present
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "设置"))
    )
    # Interact with the element
    element.click()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the driver
    driver.quit()


# # 3. Perform mouse hover action on the located element
# ActionChains(driver).move_to_element(element).perform()
#
# # Locate the link after hovering and click it
# elem1 = driver.find_element(By.LINK_TEXT, "搜索设置")
# elem1.click()
#
# # Locate the element by ID and click it (using By.ID)
# elem2 = driver.find_element(By.ID, "sh_1")
# elem2.click()
#
# # Locate the element by class name and click it (using By.CLASS_NAME)
# elem3 = driver.find_element(By.CLASS_NAME, "prefpanelgo")
# elem3.click()

# It's good practice to close the WebDriver

