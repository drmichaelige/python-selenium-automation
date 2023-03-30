from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):

    SEARCH_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, '#nav-search-submit-button')
    ORDERS = (By.CSS_SELECTOR, '#nav-orders')
    CART_ICON = (By.ID, 'nav-cart-count')
    NEW_ARRIVALS =(By.CSS_SELECTOR,"a[aria-label= 'New Arrivals']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')




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

    def select_department(self):
        department_dd = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department_dd)
        select.select_by_value('search-alias=baby-products')




    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def  verify_new_arrivals(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS)