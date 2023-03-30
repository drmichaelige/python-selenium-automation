from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.nav-a-content')
    SUBNAV_BABY = (By.CSS_SELECTOR,"#nav-subnav[data-category='baby-products']")

    def  verify_search_resullt(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_selected_dept(self):
        self.wait_for_element_appear(*self.SUBNAV_BABY)