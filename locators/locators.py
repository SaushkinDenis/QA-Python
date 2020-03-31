from common.BasicCommand import BasicCommand


class AdminPage(BasicCommand):

    selector_menu_catalog = {'css': "#menu-catalog > a"}
    selector_menu_products = {'css': "#collapse1 > li:nth-child(2) > a"}
    selector_auth = {'css': "div.panel-body > form > div.text-right > button"}

    def open_catalog(self):
        self._click(self.selector_menu_catalog['css'])
        self._click(self.selector_menu_products['css'])
        return

    def auth(self):
        self._click(self.selector_auth['css'])


class ListProductsPage(BasicCommand):
    selector_product = {'css': "#form-product > div > table > tbody > tr:nth-child(1)"}
    selector_edit_product_first = {'css': selector_product['css'] + " > td:nth-child(8) > a > i"}    #dsfsddddddddddddddddd
    selector_flag_first_product = {'css': selector_product['css'] + " > td:nth-child(1) > input[type='checkbox']"}
    selector_button = {'css': "#content > div.page-header > div > div"}
    selector_add_product = {'css': selector_button['css'] + " > a"}
    selector_del_product = {'css': selector_button['css'] + " > button.btn.btn-danger"}
    selector_list_product = {'css': "#form-product > div > table > tbody > tr"}

    def first_product_selection(self):
        self._click(self.selector_edit_product_first['css'])

    def get_len_elements(self):
        return self._get_len(self.selector_list_product['css'])

    def add_product(self):
        self._click(self.selector_add_product['css'])

    def del_product(self):
        self._click(self.selector_flag_first_product['css'])
        self._click(self.selector_del_product['css'])
        self._alert_accept()


class ProductPage(BasicCommand):
    selector_name_product = {'css': "#input-name1"}
    selector_product = {'css': "#language1 > div:nth-child(2) > div > div > div.note-toolbar.panel-heading > div.note-btn-group.btn-group.note-style > div"}
    selector_text_product_style = {'css': selector_product['css'] + " > button"}
    selector_text_product_style_blockquote = {'css': selector_product['css'] + " > div > li:nth-child(4) > a"}
    selector_product_save = {'css': "#content > div.page-header > div > div > button"}

    def edit_text_style_product(self):
        self._click(self.selector_text_product_style['css'])
        self._click(self.selector_text_product_style_blockquote['css'])

    def edit_name_product(self, value="Product#1"):
        self._input(self.selector_name_product['css'], value)

    def save_changes(self):
        self._click(self.selector_product_save['css'])

    def get_name_product(self):
        return self._get_attribute(self.selector_name_product['css'], "value")
