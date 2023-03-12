from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_INPUT_SEARCH = (By.ID, "twotabsearchtextbox")
SELECT_PRODUCT = (By.XPATH, "//span[@class='a-price']")
ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-button')
CART_ITEMS = (By.ID, "nav-cart-count")


@then('Click select product')
def click_select_product(context):
    context.driver.find_element(*SELECT_PRODUCT).click()


@then('Store the product name')
def store_the_product_name (context):
    context.product_name = context.driver.find_element(*SELECT_PRODUCT).text


@then('Verify cart count for {expected_result}')
def verify_cart_count(context, expected_result):
    expected_result = '1'
    actual_result = context.driver.find_element(*CART_ITEMS).text
    print(expected_result)
    print(actual_result)
    assert expected_result == actual_result, f'Error! Actual text {actual_result} did not match expected {expected_result}'
