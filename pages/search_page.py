from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class SearchPage(Page):

    INPUT_SEARCH = (By.ID, 'twotabsearchtextbox')
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".a-price-whole")
    # SEARCH_SUBMIT = (By.NAME, 'btnK')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.a-section span.a-color-state')

    def input_keyword(self, text):
        print(text)
        print(*self.INPUT_SEARCH)
        self.input_text(text=text, *self.INPUT_SEARCH)


    def click_on_first_product(self):
        self.click(*self.FIRST_PRODUCT)


#     context.driver.find_element(*SEARCH_INPUT)
#     #search.clear()
#     # search.send_keys(search_word)
#     # sleep(4)


# @then('Click on search icon')
# def click_on_search_icon(context):
#     context.driver.find_element(*SEARCH_ICON).click()

#
# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     expected_result = '{search_word}'
#     actual_result = context.driver.find_element(*SEARCH_RESULTS).text()
#     assert expected_result == actual_result,f'Expected query not in {expected_result}, but got {actual_result}'
