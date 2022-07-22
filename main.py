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

curmmr1s = allmmr[1]
curmmr2s = allmmr[3]
curmmr3s = allmmr[5]

time.sleep(5)

while(True):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://rocketleague.tracker.network/rocket-league/profile/steam/76561199013490288/overview'
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    allmmr = soup.find_all('div', class_='value')

    if allmmr[1].string != curmmr1s:
        with open("tricky tracker/1s.html", "r") as f:
            doc = BeautifulSoup(f, "html.parser")

            mmr = doc.find_all("td", class_="0")
            mmr[1].string = allmmr[1].string

            timer1 = 0
            

            with open("tricky tracker/1s.html", "w+") as file:
                file.write(str(doc))

            curmmr1s = allmmr[1]
            print("ran1s")

    if allmmr[3].string != curmmr2s:
        with open("tricky tracker/2s.html", "r") as f:
            doc = BeautifulSoup(f, "html.parser")

            mmr = doc.find_all("td", class_="0")
            mmr[1].string = allmmr[3].string

            with open("tricky tracker/2s.html", "w+") as file:
                file.write(str(doc))

            curmmr2s = allmmr[3]
            print("ran2s")
    
    if allmmr[5].string != curmmr3s:
        with open("tricky tracker/3s.html", "r") as f:
            doc = BeautifulSoup(f, "html.parser")

            mmr = doc.find_all("td", class_="0")
            mmr[1].string = allmmr[5].string

            with open("tricky tracker/3s.html", "w+") as file:
                file.write(str(doc))

            curmmr3s = allmmr[5]
            print("ran3s")

    print("ran")
    time.sleep(300)

    
        
