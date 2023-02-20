from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BOOK = (By.CSS_SELECTOR, '#nav-cart-count')


@when('Input text {text}')
def input_search_word(context, text):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(text)


@when('Click on search icon')
def click_on_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button').click()


@when('Click on product')
def click_on_product(context):
    context.driver.find_element(By.XPATH, "//span[@class='a-price']").click()


@when('Click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()


@then('Confirm cart count for {expected_result}')
def confirm_cart_count(context, expected_result):
    expected_result = '1'
    actual_result = context.driver.find_element(*SEARCH_BOOK).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} did not match expected {expected_result}'
