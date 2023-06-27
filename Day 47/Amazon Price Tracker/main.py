'''
This was made for amazon but it can obviously work with any kind of online shop.
'''

from bs4 import BeautifulSoup
import requests
import smtplib
import os

product = 'https://www.amazon.com/ASUS-GeForce-Gaming-Graphics-DisplayPort/dp/B0BGT61797/' \
          'ref=sr_1_2?crid=2MMF4QGN4UB1K&keywords=4090&qid=1687861045&sprefix=4090%2Caps%2C254&sr=8-2'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Accept-Language': 'en-US,en;q=0.8'
}

page = requests.get(product, headers=HEADERS)
soup = BeautifulSoup(page.content, "lxml")

YOUR_SMTP_ADDRESS = os.getenv('YOUR_SMTP_ADDRESS')  # Read from environment variable
YOUR_EMAIL = os.getenv('YOUR_EMAIL')  # Read from environment variable
YOUR_PASSWORD = os.getenv('YOUR_PASSWORD')  # Read from environment variable


def send_email(title, price, url):
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{title} is now {price}\n{url}".encode("utf-8")
        )


def extract_price(soup):
    try:
        price = soup.find("span", attrs={'class': 'a-offscreen'}).get_text().replace(',', '')
        return price
    except AttributeError:
        return 'Price not found'


def extract_product_name(soup):
    try:
        product_name = soup.find("span", attrs={"id": 'productTitle'}).string.strip().replace(',', '')
        return product_name
    except AttributeError:
        return 'Product name not found'


product_name = extract_product_name(soup)
product_price = extract_price(soup)

BUY_PRICE = 2000

print(f"Product Name = {product_name}")
print(f"Product Price = {product_price}")


def check_price():
    response = requests.get(product, headers=HEADERS)
    soup = BeautifulSoup(response.content, "lxml")
    title = soup.find(id="productTitle").get_text().strip()
    price = float(soup.find(class_="a-offscreen").get_text().replace('$', '').replace(',', ''))
    if price < BUY_PRICE:
        send_email(title, price, product)


check_price()
