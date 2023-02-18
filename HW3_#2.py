import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
service = Service('C:\GitHub\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
# open Amazon.com
driver.get('https://www.amazon.com/')
# click orders
driver.find_element(By.CSS_SELECTOR,'#nav-orders span.nav-line-2').click()

# verify sign in page open
assert driver.find_element (By.XPATH, "//div[@id='a-page']").is_displayed(), 'Sign in page not opened'

# verify sign in header visible
assert driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').is_displayed(), 'Sign in header not visible'
# verify email input is present
assert driver.find_element(By.CSS_SELECTOR, "input[type='email']").is_displayed(), 'Email input is present'
driver.quit()