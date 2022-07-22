from lib2to3.pgen2 import driver
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://rocketleague.tracker.network/rocket-league/profile/steam/76561199013490288/overview'
driver.get(url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

allmmr = soup.find_all('div', class_='value')

print(allmmr[1].string)

with open("tricky tracker/1s.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

mmr = doc.find_all("td", class_="0")
mmr[1].string = allmmr[1].string

with open("tricky tracker/1s.html", "w+") as file:
    file.write(str(doc))
