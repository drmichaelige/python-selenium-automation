from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Store original windows')
def store_current_windows(context):
    context.current_window = context.driver.current_window_handle
    print(context.current_window)


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('ALL WINDOWS:', windows)
    context.driver.switch_to.window(windows[0])

    # context.current_window = context.driver.current_window_handle
    # print(context.current_window)
    # print('\nAFTER WE SWITCHED:')
    # print(context.current_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))


@then('Close page switch back to original')
def close_switch_to_original(context):
    context.driver.close()