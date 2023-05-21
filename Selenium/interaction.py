from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

drive = webdriver.Chrome()

# drive.get('https://en.wikipedia.org/wiki/Main_Page')
# element = drive.find_elements(By.XPATH, '//*[@id="articlecount"]/a[1]')
# for element in element:
    # element.click()

# drive.get('https://www.python.org/')
# search = drive.find_elements(By.XPATH, '//*[@id="id-search-field"]')
# for element in search:
#     element.send_keys('Documentation')
#     element.send_keys(Keys.ENTER)
#
# time.sleep(30)
# drive.close()

drive.get('https://londonappbrewery.com/sendy/subscription?f=m7Xj2bDOCQnlJ27yezLEAtJi1mhUIxOaJcJGZYMLLX6wx5MZd0b2FunBI8dOomNt&_ga=2.196108904.532664633.1683769767-1872585859.1683769767')
name = drive.find_elements('//*[@id="name"]')
for e in name:
    e.send_keys('Leticia Rocha')
time.sleep(10)
email = drive.find_elements('//*[@id="email"]')
for e in email:
    e.send_keys('leticiarochacorretora@gmail.com')
time.sleep(10)
check_box = drive.find_elements('//*[@id="gdpr"]')
for e in check_box:
    e.click()
time.sleep(10)
# cap = drive.find_element('//*[@id="recaptcha-anchor"]/div[1]')
# cap.click()
# time.sleep(10)
# sub = drive.find_element('//*[@id="submit"]')
# sub.click()
time.sleep(30)
drive.close()