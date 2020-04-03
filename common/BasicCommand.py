from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasicCommand:

    driver = None

    def __init__(self, browser):
        self.driver = browser

    def __get_element(self, selector, value=0):
        if 'css' in selector.keys():
            selector = selector['css']
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        return self.driver.find_elements_by_css_selector(selector)[value]

    def _click(self, selector, value=0):
        ActionChains(self.driver).move_to_element(self.__get_element(selector, value)).click().perform()

    def _input(self, selector, value="Example"):
        self.__get_element(selector).send_keys(value)

    def _get_text(self, selector):
        return self.__get_element(selector).text

    def _get_attribute(self, selector, attribute):
        return self.__get_element(selector).get_attribute(attribute)

    def _get_len(self, selector):
        self.__get_element(selector)
        selector = selector['css']
        return len(self.driver.find_elements_by_css_selector(selector))

    def _alert_accept(self):
        WebDriverWait(self.driver, 10).until(ec.alert_is_present()).accept()
