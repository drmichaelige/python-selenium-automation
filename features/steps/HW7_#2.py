from selenium.webdriver.common.by import By
from behave import given, when, then
from tornado.web import url

from pages import cart_page
from pages.base_page import Page



from behave import given, when, then


@given('Open Amazon product_id page')
def product_url(context):
     context.driver.get(url)


@when('Click Add to cart')
def add_to_cart(context):
    context.app.cart_page.add_to_cart()
    #context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()


@then('Verify cart count is increased by 1')
def verify_cart_count_text(context):
    context.app.cart_page.verify_cart_count()
    # print(cart_page.cart_count())


# @when('Input text {text}')
# def input_value(context, text):
#     context.app.search_page.input_keyword(text)
#     # search.clear()
#     # search.send_keys(search_word)
#     # sleep(4)


# @then('Click select product')
# def click_select_product(context):
#     context.driver.find_element(*SELECT_PRODUCT).click()

@when('Click on search icon')
def click_on_search_icon(context):
    context.app.header.click_on_search()


@when('Click on the first product')
def click_on_first_product(context):
    context.app.search_page.click_on_first_product()


