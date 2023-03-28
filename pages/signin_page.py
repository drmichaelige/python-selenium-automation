from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

from pages.base_page import Page


class SigninPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, "h1.a-spacing-small")


    def verify_signin_opened(self):
        expected_text = "Sign in"
        actual_text = self.verify_text(expected_text, *self.SIGN_IN)




