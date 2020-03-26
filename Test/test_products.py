import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import locators

class Test_AdminPage():

    driver = None

    def test_edit_product(self, browser, waits):
        self.driver = browser
        self.driver.get(locators.ListProductsPage.url['css'])

        self._click(locators.AdminPage.selector_auth['css'])
        self._click(locators.ListProductsPage.selector_edit_product_first['css'])

        self._input(locators.ProductPage.selector_name_product['css'], "Apple Cinema 35\"")
        self._click(locators.ProductPage.selector_text_product_style['css'])
        self._click(locators.ProductPage.selector_text_product_style_blockquote['css'])
        self._click(locators.ProductPage.selector_product_save['css'])

        # self._click(locators.ListProductsPage.selector_edit_product_first['css'])

        assert self._text(locators.ProductPage.selector_name_product['css']) == "Apple Cinema 35\""


    def test_add_product(self, browser, waits):
        self.driver = browser
        self.driver.get(locators.ListProductsPage.url['css'])

        self._click(locators.AdminPage.selector_auth['css'])


    def test_del_product(self, browser, waits):
        self.driver = browser
        self.driver.get(locators.ListProductsPage.url['css'])

        self._click(locators.AdminPage.selector_auth['css'])

        


    def __element(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def _click(self, selector):
        ActionChains(self.driver).move_to_element(self.__element(selector)).click().perform()

    def _input(self, selector, value="Example"):
        self.__element(selector).send_keys(value)

    def _text(self, selector):
        return self.__element(selector).text
