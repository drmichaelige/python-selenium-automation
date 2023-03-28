from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):

    SEARCH_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, '#nav-search-submit-button')
    ORDERS = (By.CSS_SELECTOR, '#nav-orders')
    CART_ICON = (By.ID, 'nav-cart-count')




    # def input_text(self, text, SEARCH_INPUT):
    #     self.driver.find_element(*self.SEARCH_INPUT).send_keys(text)


    def input_search(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def click_on_search(self):
        self.click(*self.SEARCH_ICON)


    def click_orders(self):
        self.click(*self.ORDERS)

    def click_cart(self):
        self.click(*self.CART_ICON)
