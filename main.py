from lib2to3.pgen2 import driver
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

while(True):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://rocketleague.tracker.network/rocket-league/profile/epic/hydro127/overview'
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    allmmr = soup.find_all('div', class_='value')

    mmr1s = allmmr[1]
    mmr2s = allmmr[3]
    mmr3s = allmmr[5]
