

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
# Path to chromedriver
service = Service('/Users/pabloe/Documents/chromedriver')

# Optional: Configure options for Chrome
options = Options()
# options.add_argument('--headless')  # Run in headless mode if needed

# Initialize the WebDriver with the Service and Options
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination')
prices = driver.find_elements_by_xpath('button-price__price')
print(prices)
time.sleep(10000)

# Your scraping code here

