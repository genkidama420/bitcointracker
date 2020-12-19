# Import Packages

import datetime
from time import sleep
import urllib3
from bs4 import BeautifulSoup


# Get coinmarketcap front page
http = urllib3.PoolManager()
page = http.request('GET', "https://coinmarketcap.com/")


# Create Soup Object with lxml parser
soup = BeautifulSoup(page.data, 'lxml')

# Extract the current bitcoin value

def getValue():
    bitcoinRow = soup.find_all('table')[0].find_all('tr')[1].find_all('div', class_="price___3rj7O")
    text = str(bitcoinRow)
    dollarIndex = text.find('$')

    value = str()

    while dollarIndex < len(text):
        value += text[dollarIndex]

        if text[dollarIndex] == '<':
            value = value[:-1]
            break

        dollarIndex += 1
    
    now = datetime.datetime.now()
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dtString, value)


# Print initial output
getValue()

sleep(180)

while True:
    getValue()
    sleep(180)





