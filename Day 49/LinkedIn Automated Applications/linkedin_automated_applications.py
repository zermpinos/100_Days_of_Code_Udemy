from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

email = 'panoszermpinos@gmail.com'
password = r"kÙÀÚÊ]ðÅ+½#+ç¼µ×UÙ·áðÎn£\ÓnÓ»³la´æf^qQ '"
phone = '6974764432'

chrome_driver_path = Service(r"G:\- Projects\Python Projects\Best\100 Days\-- CHROME-DRIVER --\chromedriver.exe")
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

options = webdriver.ChromeOptions()
options.binary_location = brave_path
driver = webdriver.Chrome(service=chrome_driver_path, options=options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3649796468&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom')

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(2)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(email)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(2)
    easy_apply_button = driver.find_elements(By.CSS_SELECTOR, '.artdeco-button__text')
    for element in easy_apply_button:
        if element.text == "Easy Apply":
            element.click()
            break
    next_button = driver.find_elements(By.CSS_SELECTOR, '.artdeco-button__text')
    for element in next_button:
        if element.text == 'Next':
            element.click()
            break
    review_button = driver.find_elements(By.CSS_SELECTOR, '.artdeco-button__text')
    for element in review_button:
        if element.text == 'Review':
            element.click()
            break
    submit_button = driver.find_elements(By.CSS_SELECTOR, '.artdeco-button__text')
    for element in submit_button:
        if element.text == "Submit application":
            element.click()
            break
    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    close_button.click()
time.sleep(5)
driver.quit()
