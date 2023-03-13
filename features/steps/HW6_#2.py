from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

B_LINKS = (By.CSS_SELECTOR,'#zg_header li')
B_HEADER = (By.CSS_SELECTOR,'#zg_banner_text')


@then('Verify customer can click through bestsellers links and correct page opens')
def verify_click_thru_bestsellers(context):
    bestsellers_links = context.driver.find_elements(*B_LINKS)
    print(bestsellers_links)

    for i in range(len(bestsellers_links)):
        link_to_click = context.driver.find_elements(*B_LINKS)[i]
        link_text = link_to_click.text
        link_to_click.click()
        header_text = context.driver.find_element(*B_HEADER).text
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'