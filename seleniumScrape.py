print("this is Pablo testing if he can push things onto GitHub")
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

    # Navigate to url
driver.get("https://www.predictit.org/markets/detail/7456/Who-will-win-the-2024-US-presidential-election")
driver.implicitly_wait(2)
    # Retrieves the text of the element


#####  WARNING !!!!! we need to expand the page to find all the contracts available !!!!

more_button = driver.find_element(by=By.CLASS_NAME, value="market-detail__contracts-toggle-more")
driver.implicitly_wait(2)
more_button.click()
driver.implicitly_wait(2)
elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

#printing all the prices of offers & listing them in a single list
original_list = []

for element in elements:
    # print(element.text)
    # print(type(element.text))
    original_list.append(element.text)

# print(original_list)

#removing all '¢' and ' N/A'
filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
# print(filtered_list)

#keeping only the 'NO' contracts, that is every other contract, starting with i = 1 (not i=0)
final_str_list = filtered_list[1::2]
# print(final_str_list)
#final list in integer form
integer_list = [int(item) for item in final_str_list if item.isdigit()]
# print(integer_list)
# print(len(integer_list))

def minExpectedValue():
    value = (len(integer_list)-1) - (0.01 * sum(integer_list)) - (0.1*(1-0.01*smallest(integer_list, len(integer_list))))
    return(value)

def smallest(arr, n):
 
    # Initialize maximum element
    min = arr[0]
 
    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    return min
print("Minimum arbitrage profit:", minExpectedValue())
if minExpectedValue()>0:
    print("BUY")
    print("Cost:", sum(integer_list)*0.01)
else:
    print("DO NOT BUY")
