# Import necessary libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Use selenium to bypass the CAPTCHA
'''
Webdriver Module
'''
chrome_driver_path = Service(r"G:\- Projects\Python Projects\Best\100 Days\-- CHROME-DRIVER --\chromedriver.exe")
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
options = webdriver.ChromeOptions()
options.binary_location = brave_path
driver = webdriver.Chrome(service=chrome_driver_path, options=options)
driver.get('https://www.zillow.com/homes/for_sale/1-_beds/?searchQueryState={"pagination":{},"usersSearchTerm":null,"mapBounds":{"west":-122.736359,"east":-122.354589,"south":37.639829,"north":37.929824},"regionSelection":[],"isMapVisible":true,"filterState":{"pmf":{"value":false},"fore":{"value":false},"auc":{"value":false},"nc":{"value":false},"fr":{"value":true},"fsbo":{"value":false},"cmsn":{"value":false},"pf":{"value":false},"fsba":{"value":false}},"isListVisible":true,"mapZoom":11}')  # The following tends to be problematic due to zillows anti-bot protection
# Wait for the page to load
sleep(100)

# Get the page source
html = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all the links to the property listings
all_link_elements = soup.select(".list-card-top a")

# Extract the actual URLs from the link elements
all_links = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

# Find all the address elements
all_address_elements = soup.select(".list-card-info address")

# Extract the actual addresses from the address elements
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

# Find all the price elements and extract the prices
all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    try:
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)

# Fill out a Google Form with the scraped data
for n in range(len(all_links)):
    driver.get('https://forms.gle/ocJF6UpDnjZzANJC8')
    sleep(2)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
