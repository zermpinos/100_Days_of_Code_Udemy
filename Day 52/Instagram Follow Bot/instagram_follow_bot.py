from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

'''
Webdriver Module
'''
chrome_driver_path = Service(r"")
brave_path = r""
options = webdriver.ChromeOptions()
options.binary_location = brave_path
driver = webdriver.Chrome(service=chrome_driver_path, options=options)


# '''
# Login Module
# '''

# driver.get('https://www.instagram.com/accounts/login/')
# sleep(5)
# optinal_cookies_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
# optinal_cookies_button.click()
# email_entry = driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-of-type(1) > div > label > input')
# email_entry.send_keys(username)
# password_entry = driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-of-type(2) > div > label > input')
# password_entry.send_keys(password)
# password_entry.send_keys(Keys.ENTER)
# sleep(5)
# turn_off_notifications_button = driver.find_element(By.CSS_SELECTOR, 'html > body > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div > div > div:nth-of-type(1) > div > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > button:nth-of-type(2)')
# turn_off_notifications_button.click()
# sleep(5)

# '''
# Find account Module
# '''
# driver.get(f'https://www.instagram.com/{similar_account}')
# sleep(5)
# followers_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
# followers_button.click()
# sleep(15)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

class InstaFollower:

    def __init__(self, path):
        self.chrome_driver_path = BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = path
        self.driver = webdriver.Chrome(service=self.chrome_driver_path, options=self.options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        username_field = self.driver.find_element(By.NAME, username)
        password_field = self.driver.find_element(By.NAME, password)
        username = ''
        password = ''
        username_field.send_keys(username)
        password_field.send_keys(password)

        sleep(2)
        password_field.send_keys(Keys.ENTER)

    def find_followers(self, similar_account):
        sleep(5)
        similar_account = 'cristiano'
        self.driver.get(f"https://www.instagram.com/{similar_account}")
        print(similar_account)

        sleep(2)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CSS_SELECTOR, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
insta_follower = InstaFollower(brave_path)
insta_follower.login("username", "password")
insta_follower.find_followers("similar_account")
insta_follower.follow()
