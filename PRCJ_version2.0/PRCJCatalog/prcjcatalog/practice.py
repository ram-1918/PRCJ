'''import requests

url = "http://svbcgold.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the content of the response
    content = response.content.decode("utf-8")

    # Find the index of the start of the gold price
    start = content.find("Today's Price")
    print(start)
    # Find the index of the end of the gold price
    end = content.find("Per Gram")

    # Extract the gold price
    gold_price = content[start:end].split(" ")
    print("Gold price:", gold_price)
else:
    print("Failed to retrieve the gold price.")
'''

'''import requests

url = "https://finance.yahoo.com/commodities"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the content of the response
    content = response.content.decode("utf-8")
    print(content)

    # Find the index of the start of the gold price
    start = content.find("data-reactid=\\\"71\\\"")

    # Find the index of the end of the gold price
    end = content.find("data-reactid=\\\"71\\\"", start + 1)

    # Extract the gold price
    gold_price = content[start:end].split("<")[2].split(">")[1]
    print("Gold price:", gold_price)
else:
    print("Failed to retrieve the gold price.")'''

# importing libraries
from bs4 import BeautifulSoup as BS
import requests
import json


import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/commodities"
url2 = "https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF"
url3 = "https://www.goldprice.com/live-gold-price.html"

response = requests.get(url3)
soup = BeautifulSoup(response.content, "lxml")
#text = soup.findall("span", class_ = "tv-ticker-item-last__last js-symbol-last apply-overflow-tooltip").text
#print(price)
print(soup)
