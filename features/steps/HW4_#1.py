from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLERS_MENU = (By.CSS_SELECTOR,'#zg_header')
BESTSELLERS_LINKS = (By.XPATH, "//*[contains(@href, '/ref=zg_bs_tab')]")




@then('Verify Bestsellers menu links present')
def verify_bestsellers_menu_links_present(context):
    context.driver.find_element(*BESTSELLERS_MENU)
    # print(element)


@then('Verify Bestsellers has {expected_amount} links')
def verify_bestsellers_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    bestsellers_links = context.driver.find_elements(*BESTSELLERS_LINKS)
    assert len(bestsellers_links) == expected_amount, f'Expected {expected_amount} links but got {len(bestsellers_links)}'