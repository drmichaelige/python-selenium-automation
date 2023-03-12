from selenium.webdriver.common.by import By
from behave import given, when, then


PRODUCT_NAME = (By.CSS_SELECTOR,'#productTitle')
PRODUCT_PRICE = (By.CSS_SELECTOR,'td.a-span12 span.a-price-range')
COLOR_OPTIONS =(By.CSS_SELECTOR,'#variation_color_name li')
CURRENT_COLOR =(By.CSS_SELECTOR,'#variation_color_name .selection')


@then('Store Product Name and Price')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text
    print(f'Current product price: {context.product_price}')


@then ('Verify customer can click through colors')
def verify_customer_can_select_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()


    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)

  #



