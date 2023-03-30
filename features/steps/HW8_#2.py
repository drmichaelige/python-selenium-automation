from selenium.webdriver.common.by import By
from behave import given, when, then
from tornado.web import url

from pages import cart_page
from pages.base_page import Page




@when('Select Baby department')
def select_dept(context):
    context.app.header.select_department()




@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()

@then('Verify user sees the details')
def verify_new_arrivals(context):
    context.app.header.verify_new_arrivals()