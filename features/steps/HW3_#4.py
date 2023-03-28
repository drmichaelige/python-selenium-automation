from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BOOK = (By.CSS_SELECTOR, '#nav-cart-count')


@when('Input text {text}')
def input_text(context, text):
    context.app.header.input_search(text)


@then('Click on product')
def click_on_product(context):
    context.app.product.add_product()
    context.driver.find_element(By.XPATH, "//span[@class='a-price']").click()


@then('Click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()


@then('Confirm cart count for {expected_result}')
def confirm_cart_count(context, expected_result):
    expected_result = '1'
    actual_result = context.driver.find_element(*SEARCH_BOOK).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} did not match expected {expected_result}'
