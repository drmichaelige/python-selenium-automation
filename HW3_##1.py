import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
service = Service('C:\GitHub\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
# open Amazon.com
driver.get('https://www.amazon.com/')

# openHello sign in page
driver.find_element(By.CSS_SELECTOR, '#nav-link-accountList')

#click new customer create account
driver.find_element(By.XPATH, "//div[@id='nav-signin-tooltip']//a[contains(text(), 'Start here.')]").click()

# Amazon logo locator
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")

# create account locator
driver.find_element(By.XPATH, "//h1[contains(text(), 'Create account')]")

# First and last name input
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#  email input
driver.find_element(By.CSS_SELECTOR, "input[type='email']")

#  password input
driver.find_element(By.CSS_SELECTOR, "input[type='password']")

#  password characters limit
driver.find_element(By.CSS_SELECTOR, '.a-alert-content')

# re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# continue
driver.find_element(By.CSS_SELECTOR, '#continue')

# condition of use
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")

#  privacy notice
driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")

# Sign in
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')
