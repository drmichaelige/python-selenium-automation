from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLERS_MENU = (By.CSS_SELECTOR,'#zg_header')
BESTSELLERS_LINKS = (By.XPATH, "//*[contains(@href, '/ref=zg_bs_tab')]")


@given('Open Amazon BestSellers page')
def open_gamazon_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify Bestsellers menu links present')
def verify_bestsellers_menu_links_present(context):
    context.driver.find_element(*BESTSELLERS_MENU)
    # print(element)


@then('Verify Bestsellers has {expected_amount} links')
def verify_bestsellers_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    bestsellers_links = context.driver.find_elements(*BESTSELLERS_LINKS)
    assert len(bestsellers_links) == expected_amount, f'Expected {expected_amount} links but got {len(bestsellers_links)}'