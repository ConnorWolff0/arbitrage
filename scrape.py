'''
from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

names = soup.findAll("span", attrs = {"class": "market-contract-horizontal-v2__title-text"})
print(names)

page_to_scrape = requests.get("https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#Find all quote & author elements 
quotes = soup.findAll("span", attrs={"class": "market-contract-horizontal-v2__title-text"})
#authors = soup.findAll("small", attrs={"class": "button-price__price"})

with open("scraped_quotes.csv", "w", newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(["NAMES"])
    for quote in quotes:
        print(quote.text)
        writer.writerow(quote.text)

# 
# #Open the CSV file for writing
# with open("scraped_quotes.csv", "w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["QUOTES", "AUTHORS"])
#     #Iterate over the paired quotes and authors
#     for quote, author in zip(quotes, authors):
#         #print(type(quote), type(author))
#         print(quote.text + " _ " + author.text)
#         writer.writerow([quote.text, author.text])
# '''
'''
from bs4 import BeautifulSoup
import requests

webpage_response = requests.get("https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination")

webpage = webpage_response.content
print(webpage)


'''
from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.predictit.org/markets/detail/8089/Who-will-win-the-2024-Democratic-vice-presidential-nomination")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

names = soup.findAll("span", attrs = {"class": "market-contract-horizontal-v2__title-text"})
print(names)