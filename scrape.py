from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#Find all quote & author elements 
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

#Open the CSV file for writing
with open("scraped_quotes.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["QUOTES", "AUTHORS"])
    #Iterate over the paired quotes and authors
    for quote, author in zip(quotes, authors):
        #print(type(quote), type(author))
        print(quote.text + " _ " + author.text)
        writer.writerow([quote.text, author.text])
    

#connor test