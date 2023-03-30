from selenium.webdriver.common.by import By
from behave import given, when, then
from tornado.web import url


@then('Verify Baby store is selected')
def verify_selected_dept(context):
    context.app.search_results_page.verify_selected_dept()
