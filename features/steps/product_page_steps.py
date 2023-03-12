from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open Amazon page')
def open_amazon(context):
     context.driver.get('https://www.amazon.com/')
     context.driver.implicitly_wait(1)


@given('Open BestSellers page')
def open_bestsellers_page(context):
    context.driver.get(f'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@given('Open Amazon {product_id} page')
def open_amazon(context, product_id):
     context.driver.get(f'https://www.amazon.com/dp/{product_id}/')
     # context.driver.implicitly_wait(1)

