#from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.signin_page import SigninPage
# from pages.new_page import NewPage


#from pages.signin_page_steps import SigninPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.signin_page = SigninPage(self.driver)
        self.cart_page = CartPage(self.driver)
        # self.verify_cart_count = CartPage(self.driver)
        self.search_page = SearchPage(self.driver)
        #self.new_page = NewPage(self.driver)
        # self.search_results_page = SearchResultsPage(self.driver)