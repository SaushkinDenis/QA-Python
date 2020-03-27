import time

from selenium.common.exceptions import UnexpectedAlertPresentException

from common.BasicCommand import BasicCommand
from locators.locators import locators


class Test_Admin_Page:

    def test_edit_product(self, browser, waits):

        driver = BasicCommand(browser)

        driver._click(locators.ListProductsPage.selector_edit_product_first['css'])
        driver._input(locators.ProductPage.selector_name_product['css'], "Apple Cinema 35\"")
        driver._click(locators.ProductPage.selector_text_product_style['css'])
        driver._click(locators.ProductPage.selector_text_product_style_blockquote['css'])
        driver._click(locators.ProductPage.selector_product_save['css'])

        driver._click(locators.AdminPage.selector_menu_catalog['css'])
        driver._click(locators.AdminPage.selector_menu_products['css'])
        driver._click(locators.ListProductsPage.selector_edit_product_first['css'])

        assert driver._get_attribute(locators.ProductPage.selector_name_product['css'], "value") == "Apple Cinema 35\""


    def test_add_product(self, browser, waits):
        driver = BasicCommand(browser)

        a = driver._get_len(locators.ListProductsPage.selector_list_product['css']) + 1

        driver._click(locators.ListProductsPage.selector_add_product['css'])
        driver._input(locators.ProductPage.selector_name_product['css'], "Product #1")
        driver._click(locators.ProductPage.selector_product_save["css"])
        time.sleep(5)
        driver._click(locators.AdminPage.selector_menu_catalog['css'])
        driver._click(locators.AdminPage.selector_menu_products['css'])

        assert a == driver._get_len(locators.ListProductsPage.selector_list_product['css'])

    def test_del_product(self, browser, waits):
        driver = BasicCommand(browser)

        a = driver._get_len(locators.ListProductsPage.selector_list_product['css']) - 1
        driver._click(locators.ListProductsPage.selector_flag_first_product['css'])
        driver._click(locators.ListProductsPage.selector_del_product['css'])
        driver._alert_accept()
        time.sleep(5)
        driver._click(locators.AdminPage.selector_menu_catalog['css'])
        driver._click(locators.AdminPage.selector_menu_products['css'])
        time.sleep(5)


        assert a ==  driver._get_len(locators.ListProductsPage.selector_list_product['css'])



