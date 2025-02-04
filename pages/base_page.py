from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://www.amazon.com/'

    def click(self, *locator):  #(By.ID, 'value..')
        self.driver.find_element(*locator).click()

    def open_page(self, page_address=''):
        self.driver.get(f'{self.base_url}{page_address}')

    # def input_text(self, text, *locator):
    #     self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, text, *locator):
        current_text = self.driver.find_element(*locator).text

        assert current_text == text, f'Expected {text}, but got {current_text}'
        #assert current_text == text

    #def input_text(self, text, *locator):
        #self.driver.find_element(*locator).send_keys(text)

    #def verify_text(self, text, *locator):
        ##assert current_text == text


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, end_url=''):
        print(f'{self.base_url}{end_url}')
        self.driver.get(f'{self.base_url}{end_url}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'

    #def Verify_correct_options_present(self):
        #self.wait_for_element_appear(*self.SELECTION_ARRIVALS)