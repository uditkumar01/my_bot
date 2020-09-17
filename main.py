import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i7/dp/B081JWZQJB/ref=sr_1_1_sspa?crid=12N2J0LT83PP8&dchild=1&keywords=macbook+air&qid=1600259708&sprefix=macb%2Caps%2C389&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUjhRTDdOUlJDVjRSJmVuY3J5cHRlZElkPUEwMTI5MzE3MzZURFFMVlBDWktKRyZlbmNyeXB0ZWRBZElkPUEwNDgzOTc4M0FCOVEwUFhXNDJIMyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"}
PRICE_VALUE = 160

def trackPrices():
    price = float(getPrice())
    if price > PRICE_VALUE:
        diff = int(price - PRICE_VALUE)
        print(f"Still £{diff} too expensive")
    else:
        print("Cheaper! Notifying...")
        sendEmail()
    pass

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    raw_price = soup.find(id='priceblock_ourprice').get_text().strip()
    price = ""
    for i in raw_price:
        if '0'<=i<='9':
            price+=i
    print(title)
    print(price)
    return price

def sendEmail():
    
    pass

if __name__ == "__main__":
    trackPrices()