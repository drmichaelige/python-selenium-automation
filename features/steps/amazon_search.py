from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
#SEARCH_SUBMIT = (By.NAME, 'btnK')
SEARCH_ICON = (By.CSS_SELECTOR, '#nav-search-submit-button')
SEARCH_RESULTS = (By.CSS_SELECTOR, '.a-section span.a-color-state')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.driver.find_element(*SEARCH_INPUT)
    #search.clear()
    # search.send_keys(search_word)
    # sleep(4)


@then('Click on search icon')
def click_on_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()

#
# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     expected_result = '{search_word}'
#     actual_result = context.driver.find_element(*SEARCH_RESULTS).text()
#     assert expected_result == actual_result,f'Expected query not in {expected_result}, but got {actual_result}'
