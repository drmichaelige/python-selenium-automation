import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
service = Service('C:\GitHub\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//div[@class='nav-line-1-container']").click()

# find locator for Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")


# find locator for Continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

# find locator for Need help link
driver.find_element (By.XPATH,"//span[contains(text(), 'Need help?')]")

# find locator for Need help link Click
driver.find_element (By.XPATH,"//span[contains(text(), 'Need help?')]").click()

# find locator for Forgot your password link
driver.find_element (By.XPATH,"//div[@aria-expanded='true']//a[contains(text(), 'Forgot your password?')]")

# find locator for Other issues with Sign-In link
driver.find_element(By.XPATH,"//div[@aria-expanded='true']//a[contains(text(), 'Other issues with Sign-In')]")

# find locator for Create your Amazon account button
driver.find_element (By.XPATH,"//a[@id='createAccountSubmit']")

# find locator for Conditions of use link
driver.find_element (By.XPATH,"//div[@class='a-section a-spacing-small a-text-center a-size-mini']//a[contains(text(),'Conditions of Use')]")

# find locator for Privacy Notice link
driver.find_element (By.XPATH,"//div[@class='a-section a-spacing-small a-text-center a-size-mini']//a[contains(text(),'Privacy Notice')]")

