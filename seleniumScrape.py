from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def Democratic_vice_presidential_nominee(): # KEEP COMMENTS FOR THIS FUNCTION (FOR FUTURE REFERENCE)

        # Navigate to url
    driver.get("https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination")
    driver.implicitly_wait(0.4)
        # Retrieves the text of the element

    # expands page to reveal all contracts
    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)
    except NoSuchElementException:
        print()

    # collects all information regarding offer prices
    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    #listing all the prices of offers in a single list
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
    print("\n DEMOCRATIC VICE PRESIDENTIAL NOMINEE")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Democratic_2024_presidential_nominee():

    driver.get("https://www.predictit.org/markets/detail/7057/Who-will-win-the-2024-Democratic-presidential-nomination")
    driver.implicitly_wait(0.4)

    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)
    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\n DEMOCRATIC 2024 PRESIDENTIAL NOMINEE")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Electoral_College_margin_in_2024():

    driver.get("https://www.predictit.org/markets/detail/8077/What-will-be-the-Electoral-College-margin-in-the-2024-presidential-election")
    driver.implicitly_wait(0.4)

    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)
    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nELECTORAL COLLEGE MARGIN IN 2024")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def a2024_presidential_election_winner():

    driver.get("https://www.predictit.org/markets/detail/7456/Who-will-win-the-2024-US-presidential-election")
    driver.implicitly_wait(0.4)

    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)
    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\n2024 PRESIDENTIAL ELECTION WINNER")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Which_party_wins_the_presidency_in_2024():

    driver.get("https://www.predictit.org/markets/detail/6867/Which-party-will-win-the-2024-US-presidential-election")
    driver.implicitly_wait(0.4)

    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)
    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nWHICH PARTY WILL WIN THE 2024 U.S. PRESIDENTIAL ELECTION?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Harris_on_2024_democratic_ticket():

    driver.get("https://www.predictit.org/markets/detail/7629/Will-Kamala-Harris-be-on-the-2024-Democratic-ticket")
    driver.implicitly_wait(0.4)

    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)
    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nHARRIS ON 2024 DEMOCRATIC TICKET?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Will_joe_biden_resign_during_his_first_term():

    driver.get("https://www.predictit.org/markets/detail/7136/Will-Joe-Biden-resign-during-his-first-term")
    driver.implicitly_wait(0.4)


    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)

    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nWILL JOE BIDEN RESIGN DURING HIS FIRST TERM?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Which_party_will_win_Georgia_in_the_2024_presidential_election():

    driver.get("https://www.predictit.org/markets/detail/8072/Which-party-will-win-Georgia-in-the-2024-presidential-election")
    driver.implicitly_wait(0.4)


    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)

    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nWHICH PARTY WILL WIN GEORGIA IN THE 2024 PRESIDENTIAL ELECTION?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Harris_the_47th_US_president():

    driver.get("https://www.predictit.org/markets/detail/7419/Will-Kamala-Harris-be-the-47th-US-president")
    driver.implicitly_wait(0.4)


    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)

    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nWILL KAMALA HARRIS BE THE 47TH US PRESIDENT?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Woman_president_elected_in_2024():

    driver.get("https://www.predictit.org/markets/detail/7013/Will-a-woman-be-elected-US-president-in-2024")
    driver.implicitly_wait(0.4)


    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)

    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nWILL A WOMAN BE ELECTED U.S. PRESIDENT IN 2024?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Which_party_will_win_Wisconsin_in_the_2024_presidential_election():

    driver.get("https://www.predictit.org/markets/detail/8076/Which-party-will-win-Wisconsin-in-the-2024-presidential-election")
    driver.implicitly_wait(0.4)


    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)

    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nWHICH PARTY WILL WIN WISCONSIN IN THE 2024 PRESIDENTIAL ELECTION?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Which_party_will_win_the_2024_senate_election_in_arizona():

    driver.get("https://www.predictit.org/markets/detail/8070/Which-party-will-win-the-2024-US-Senate-election-in-Arizona")
    driver.implicitly_wait(0.4)


    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)

    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nWHICH PARTY WILL WIN THE 2024 US SENATE ELECTION IN ARIZONA?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")
def Which_party_will_win_the_2024_US_senate_election_in_ohio():

    driver.get("https://www.predictit.org/markets/detail/8075/Which-party-will-win-the-2024-US-Senate-election-in-Ohio")
    driver.implicitly_wait(0.4)


    try:
        more_button = driver.find_element(By.CLASS_NAME, "market-detail__contracts-toggle-more")
        more_button.click()
        driver.implicitly_wait(0.4)

    except NoSuchElementException:
        print()

    elements = driver.find_elements(By.CLASS_NAME, "button-price__price")

    original_list = []
    for element in elements:
        original_list.append(element.text)

    filtered_list = [s.replace('¢', '').replace('N/A', '').strip() for s in original_list]
    final_str_list = filtered_list[1::2]
    integer_list = [int(item) for item in final_str_list if item.isdigit()]
    print("\nWHICH PARTY WILL WIN THE 2024 US SENATE ELECTION IN OHIO?")
    print("\nMinimum arbitrage profit:", minExpectedValue(integer_list), "")
    if minExpectedValue(integer_list)>0:
        print("\nBUY all 'NO' contracts")
        print("Cost:", sum(integer_list)*0.01)
    else:
        print("\nDO NOT BUY\n\n")


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

def minExpectedValue(integer_list):
    value = (len(integer_list)-1) - (0.01 * sum(integer_list)) - (0.1*(1-0.01*smallest(integer_list, len(integer_list))))
    return(value)

Democratic_vice_presidential_nominee()
time.sleep(7)
Democratic_2024_presidential_nominee()
time.sleep(7)
Electoral_College_margin_in_2024()
time.sleep(7)
a2024_presidential_election_winner()
time.sleep(7)
Which_party_wins_the_presidency_in_2024()
time.sleep(7)
# Harris_on_2024_democratic_ticket()
# time.sleep(7)
# Will_joe_biden_resign_during_his_first_term()
# time.sleep(7)
Which_party_will_win_Georgia_in_the_2024_presidential_election()
time.sleep(7)
# Harris_the_47th_US_president()
# time.sleep(7)
# Woman_president_elected_in_2024()
# time.sleep(7)
Which_party_will_win_Wisconsin_in_the_2024_presidential_election()
time.sleep(7)
Which_party_will_win_the_2024_senate_election_in_arizona()
time.sleep(7)
Which_party_will_win_the_2024_US_senate_election_in_ohio()
time.sleep(7)
