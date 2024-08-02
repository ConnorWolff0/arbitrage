from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

    # Navigate to url
running_sum=0
driver.get("https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination")
driver.implicitly_wait(5)
    # Retrieves the text of the element
elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

#printing all the prices of offers & listing them in a single list
original_list = []
filtered_list = []
i=0

for element in elements:
    original_list.append(element.text)


for element in elements:
    filtered_list.append(original_list[i][:-1])
    i+=1

    
    
print(filtered_list)
