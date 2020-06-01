from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasicCommand:

    driver = None

    def __init__(self, browser):
        self.driver = browser

    def __get_element(self, selector):
        if 'css' in selector.keys():
            selector = selector['css']
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, selector)))
        return self.driver.find_elements_by_css_selector(selector)

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__get_element(selector)[index]).click().perform()

    def _input(self, selector, value="Example", index=0):
        element = self.__get_element(selector)[index]
        element.clear()
        element.send_keys(value)

    def _get_text(self, selector, index=0):
        return self.__get_element(selector)[index].text

    def _get_attribute(self, selector, attribute, index=0):
        return self.__get_element(selector)[index].get_attribute(attribute)

    def _get_len(self, selector):
        return len(self.__get_element(selector))

    def _alert_accept(self):
        WebDriverWait(self.driver, 10).until(ec.alert_is_present()).accept()
