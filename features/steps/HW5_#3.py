from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_IMAGE = (By.CSS_SELECTOR, '.s-product-image-container')
#PRODUCT_IMAGE = (By.CSS_SELECTOR, '.s-image.s-image-padding')
PRODUCT_NAME =  (By.CSS_SELECTOR,'div.a-section.s-title-instructions-style')
SEARCH_RESULTS = (By.CSS_SELECTOR,'div[data-component-type=s-search-result]')


@then('Verify all results have product image and name')
def verify_product_image_name (context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(f'Number of products found: {len(all_products)}')
    print(all_products)

    for product in all_products:
       assert product.find_element(*PRODUCT_IMAGE).is_displayed(), 'Product image is missing'


       product_name = product.find_element(*PRODUCT_NAME).text
       assert product.find_element(*PRODUCT_NAME).is_displayed(), 'Product name is missing'

