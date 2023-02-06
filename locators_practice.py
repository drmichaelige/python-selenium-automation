import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
service = Service('C:\GitHub\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')


# find locators practice

# By ID ( Search Amazon )
driver.find_element(By.ID, 'twotabsearchtextbox')

# By Xpath, tag and attribute
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//img[@alt='Gillette Intimate Trimmer, Gillette & Venus Razors & Refills']")

# By Xpath, multiple attr
driver.find_element(By.XPATH, "//span[@class='a-truncate-cut' and @aria-hidden='true']")

# By Xpath, contains:
driver.find_element(By.XPATH, "//img[contains(@alt, 'Valentine')]")

# contains AND attr
driver.find_element(By.XPATH, "//div[contains(@class, 'fluid-card') and @data-a-card-type='basic']")

# By Xpath, without a tag
driver.find_element(By.XPATH, "//*[@title='Watch now']")
driver.find_element(By.XPATH, "//*[contains(@alt, 'Black voices') and @class='landscape-image']")

# By xpath, attr starts with certain value:
driver.find_element(By.XPATH, "//a[starts-with(@href, '/gp/css/order-history?ref')]")

# By xpath, text
driver.find_element(By.XPATH, "//a[text()='Amazon Basics']")

# Contains text:
driver.find_element(By.XPATH, "//a[contains(text(), 'Amazon Basics')]")

# By xpath, going from parent node ==> child
driver.find_element(By.XPATH, "//div[@class='nav-progressive-content']//a[text()='Best Sellers']")
