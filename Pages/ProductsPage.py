import logging

from Common.BasicCommand import BasicCommand
from Pages.ProductPage import ProductPage


class ProductsPage(BasicCommand):
    PRODUCT = {'css': "#form-product > div > table > tbody > tr:nth-child(1)"}
    BUTTON_EDIT_PRODUCT_FIRST = {'css': PRODUCT['css'] + " > td:nth-child(8) > a > i"}    #dsfsddddddddddddddddd
    FLAG_FIRST_PRODUCT = {'css': PRODUCT['css'] + " > td:nth-child(1) > input[type='checkbox']"}
    BUTTONS = {'css': "#content > div.page-header > div > div"}
    BUTTON_ADD_PRODUCT = {'css': BUTTONS['css'] + " > a"}
    BUTTON_DEL_PRODUCT = {'css': BUTTONS['css'] + " > button.btn.btn-danger"}
    LIST_PRODUCTS = {'css': "#form-product > div > table > tbody > tr"}
    FILTER_NAME = {'css': "#input-name"}
    BUTTON_FILTER = {'css': "#button-filter"}

    logger = logging.getLogger("ProductsPage")

    def first_product_selection(self):
        self.logger.info("Open first product")
        self._click(self.BUTTON_EDIT_PRODUCT_FIRST)
        return ProductPage(self.driver)

    def get_len_elements(self):
        return self._get_len(self.LIST_PRODUCTS)

    def add_product(self):
        self.logger.info("Add product")
        self._click(self.BUTTON_ADD_PRODUCT)
        return ProductPage(self.driver)

    def del_product(self):
        self.logger.info("Delete product")
        self._click(self.FLAG_FIRST_PRODUCT)
        self._click(self.BUTTON_DEL_PRODUCT)
        self._alert_accept()
        return self

    def set_name_filter(self, value="Product#1"):
        self._input(self.FILTER_NAME, value)
        return self

    def active_filter(self):
        self._click(self.BUTTON_FILTER)
        return self