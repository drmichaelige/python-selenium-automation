from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):

    CART_EMPTY = (By.CSS_SELECTOR,'.a-row.sc-your-amazon-cart-is-empty')
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    CART_COUNT = (By.ID, 'nav-cart-count')

    def verify_cart_empty(self):
        expected_text = "Your Amazon Cart is empty"
        actual_text = self.find_element(*self.CART_EMPTY).text
        print("|" + expected_text + "|")
        print("|" + actual_text + "|")
        assert expected_text == actual_text, f'Expected text not found'

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def verify_cart_count(self):
        expected_text = "1"
        actual_text = self.find_element(*self.CART_COUNT).text
        print("expected_text")
        print("actual_text")
        assert expected_text == actual_text, f'Expected text not found'