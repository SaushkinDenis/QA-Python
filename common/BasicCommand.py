from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.locators import locators
from selenium.webdriver.common.alert import Alert


class BasicCommand:

    driver = None

    def __init__(self, browser):
        self.driver = browser
        self.driver.get(locators.ListProductsPage.url['css'])
        self._click(locators.AdminPage.selector_auth['css'])

    def __element(self, selector):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def _click(self, selector):
        ActionChains(self.driver).move_to_element(self.__element(selector)).click().perform()

    def _input(self, selector, value="Example"):
        self.__element(selector).send_keys(value)

    def _text(self, selector):
        return self.__element(selector).text

    def _get_attribute(self, selector, attribute):
        return self.__element(selector).get_attribute(attribute)

    def _get_len(self, selector):
        self.__element(selector)
        return len(self.driver.find_elements_by_css_selector(selector))

    def _alert_accept(self):
        WebDriverWait(self.driver, 10).until(ec.alert_is_present()).accept()
