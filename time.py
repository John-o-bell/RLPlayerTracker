from lib2to3.pgen2 import driver
from tracemalloc import start
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


timerStatus = False

def startTimer():
    timer = 0
    timerStatus = True
    while(timerStatus == True):
        timer = timer + 1
        time.sleep(1)
        print(timer)
        
def stopTimer():
    timer = 0
    timerStatus = False
    print("ran")

startTimer()
time.sleep(10)
stopTimer()

