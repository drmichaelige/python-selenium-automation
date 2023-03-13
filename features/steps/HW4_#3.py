from selenium.webdriver.common.by import By
from behave import given, when, then



CS_PAGE = (By.XPATH, "//h1[contains(text(),'Welcome to Amazon Customer Service')]")
ELEMENT_1 = (By.CSS_SELECTOR,'.header-subtext.subtext-container')
ELEMENT_2 = (By.CSS_SELECTOR,'.issue-card-container')
ELEMENT_3 = (By.XPATH,"//h2[contains(text(),'Search our help library')]")
ELEMENT_4 = (By.CSS_SELECTOR, '#hubHelpSearchInput')
ELEMENT_5 = (By.XPATH,"//h2[contains(text(),'All help topics')]")
ELEMENT_6 = (By.CSS_SELECTOR,'.help-topics-list-wrapper')



@then('Verify Customer Service page present')
def verify_cs_page_present(context):
    context.driver.find_element(*CS_PAGE)


@then('Verify Customer Service page elements')
def verify_cs_page_elements(context):
    context.driver.find_element(*ELEMENT_1)
    context.driver.find_element(*ELEMENT_2)
    context.driver.find_element(*ELEMENT_3)
    context.driver.find_element(*ELEMENT_4)
    context.driver.find_element(*ELEMENT_5)
    context.driver.find_element(*ELEMENT_6)