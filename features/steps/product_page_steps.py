from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

CS_LINK = (By.CSS_SELECTOR,"a[href*='nav_cs_customerservice']")
COU_PAGE = (By.CSS_SELECTOR,"a[href*='gp/help/customer/display.html?nodeId=508088&ref_=footer_cou']")
PRIVACY_NOTICE = (By.CSS_SELECTOR,"a[href*='privacy']")


# @given('Open Amazon page')
# def open_amazon(context):
#      context.driver.get('https://www.amazon.com/')
#      context.driver.implicitly_wait(1)


@given('Open BestSellers page')
def open_bestsellers_page(context):
    context.driver.get(f'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@given('Open Amazon {product_id} page')
def open_amazon(context, product_id):
     context.driver.get(f'https://www.amazon.com/dp/{product_id}/')
     # context.driver.implicitly_wait(1)


@then('Go to Customer Service page')
def go_to_cs_page(context):
    context.driver.find_element(*CS_LINK).click()


@given('Open Conditions of Use page')
def open_cs_page(context):
    context.driver.find_element(*COU_PAGE)


@given('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()