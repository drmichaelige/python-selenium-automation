from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open Amazon page")
def open_amazon_page(context):
    context.app.main_page.open_amazon()


@when('Click Amazon Orders link')
def click_orders_link(context):
    context.app.header.click_orders()


@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    context.app.signin_page.verify_signin_opened()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart()


@then('Verify Your Shopping Cart is empty text present')
def verify_cart_empty_text(context):
    context.app.cart_page.verify_cart_empty()
