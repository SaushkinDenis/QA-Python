from common.BasicCommand import BasicCommand


class ProductsPage(BasicCommand):
    selector_product = {'css': "#form-product > div > table > tbody > tr:nth-child(1)"}
    selector_edit_product_first = {'css': selector_product['css'] + " > td:nth-child(8) > a > i"}    #dsfsddddddddddddddddd
    selector_flag_first_product = {'css': selector_product['css'] + " > td:nth-child(1) > input[type='checkbox']"}
    selector_button = {'css': "#content > div.page-header > div > div"}
    selector_add_product = {'css': selector_button['css'] + " > a"}
    selector_del_product = {'css': selector_button['css'] + " > button.btn.btn-danger"}
    selector_list_product = {'css': "#form-product > div > table > tbody > tr"}
    selector_filter_name = {'css': "#input-name"}
    selector_filter_button = {'css': "#button-filter"}

    def first_product_selection(self):
        self._click(self.selector_edit_product_first)

    def get_len_elements(self):
        return self._get_len(self.selector_list_product)

    def add_product(self):
        self._click(self.selector_add_product)

    def del_product(self):
        self._click(self.selector_flag_first_product)
        self._click(self.selector_del_product)
        self._alert_accept()

    def set_name_filter(self, value="Product#1"):
        self._input(self.selector_filter_name, value)

    def active_filter(self):
        self._click(self.selector_filter_button)