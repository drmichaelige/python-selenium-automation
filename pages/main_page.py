from selenium.webdriver.common.by import By


from pages.base_page import Page


class MainPage(Page):

    def open_amazon(self):
         self.open_page()


    def open_amazon_product_page(self):
         self.open_url('https://www.amazon.com/dp/B09Y939KR2/')
         context.driver.implicitly_wait(1)