import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

drive = webdriver.Chrome()

drive.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = drive.find_elements(By.XPATH, '//*[@id="cookie"]')
cursor = drive.find_elements(By.XPATH, '//*[@id="buyCursor"]')
grandma = drive.find_elements(By.XPATH, '//*[@id="buyGrandma"]')
factory = drive.find_elements(By.XPATH, '//*[@id="buyFactory"]')
mine = drive.find_elements(By.XPATH, '//*[@id="buyMine"]')
ship = drive.find_elements(By.XPATH, '//*[@id="buyShipment"]')
alchemy = drive.find_elements(By.XPATH, '//*[@id="buyAlchemy lab"]')
portal = drive.find_elements(By.XPATH, '//*[@id="buyPortal"]')
time_ma = drive.find_elements(By.XPATH, '//*[@id="buyTime machine"]/span')

while True:
    for e in cookie:
        e.click()
        print('cookie')
    for e in cursor:
        e.click()
        print('cursor')
    for e in grandma:
        e.click()
        print('grandma')
    for e in mine:
        e.click()
        print('mine')
    for e in ship:
        e.click()
        print('ship')
    for e in alchemy:
        e.click()
        print('alchemy')
    for e in time_ma:
        e.click()
        print('time_ma')

time.sleep(60)
drive.close()
