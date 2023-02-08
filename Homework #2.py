import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
service = Service('C:\GitHub\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')