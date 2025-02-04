from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@when('Click Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-text-container').click()



@then('Cart page opens')
def cart_page_opens(context):
    context.driver.find_element(By.ID, 'sc-active-cart')


@then('Verify the cart count is {expected_result}')
def verify_cart_count(context, expected_result):
    actual_result = context.find_element()
    assert actual_result == expected_result


@then('Verify "Your Amazon Cart is Empty" is displayed')
def verify_search_result(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'