from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_INPUT_SEARCH = (By.ID, "twotabsearchtextbox")
SEARCH_ICON = (By.CSS_SELECTOR, '#nav-search-submit-button')
SELECT_PRODUCT = (By.XPATH, "//span[@class='a-price']")
ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-button')
CART_ITEMS = (By.ID, "nav-cart-count")


@when('Click the search icon')
def click_the_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click select product')
def click_select_product(context):
    context.driver.find_element(*SELECT_PRODUCT).click()


@then('Verify cart count for {expected_result}')
def verify_cart_count(context, expected_result):
    expected_result = '1'
    actual_result = context.driver.find_element(*CART_ITEMS).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} did not match expected {expected_result}'
