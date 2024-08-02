from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_no_prices(url):
    # Setup Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the URL
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be available

    # Find the "no" price elements
    no_price_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'market-outcome__row--no')]//span[contains(@class, 'market-outcome__price')]")
    
    # Extract and print the "no" prices
    no_prices = [elem.text for elem in no_price_elements]

    # Close the driver
    driver.quit()

    return no_prices

url = "https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination"
no_prices = get_no_prices(url)

print("List of 'No' prices:")
for price in no_prices:
    print(price)
