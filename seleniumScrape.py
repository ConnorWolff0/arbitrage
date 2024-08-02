from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination")
driver.implicitly_wait(50)

# text = driver.find_element(By.ID, "button-price__price").text


offers = driver.find_element(By.CLASS_NAME, "button-price__price")

driver.quit()

print(text)

