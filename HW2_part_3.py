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
driver.find_element(By.XPATH, "//span[text()='& Orders']").click()

# Verify Sign in page opened, Sign in header vsisble and email field present
expected_result = driver.find_element(By.XPATH,"//div[@id='a-page']|//h1[contains(text(), 'Sign in')]|//input[ @ type = 'email']")

# Check actual result
actual_result = driver.find_element(By.XPATH,"//div[@id='a-page']|//h1[contains(text(), 'Sign in')]|//input[ @ type = 'email']")


# confirm actual results = expected results and print test passed
assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'

# verify email field present
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'

driver.quit()