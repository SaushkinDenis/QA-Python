from common.BasicCommand import BasicCommand


class ProductPage(BasicCommand):
    selector_name_product = {'css': "#input-name1"}
    selector_product = {'css': "#language1 > div:nth-child(2) > div > div > div.note-toolbar.panel-heading > div.note-btn-group.btn-group.note-style > div"}
    selector_text_product_style = {'css': selector_product['css'] + " > button"}
    selector_text_product_style_blockquote = {'css': selector_product['css'] + " > div > li:nth-child(4) > a"}
    selector_product_save = {'css': "#content > div.page-header > div > div > button"}

    def edit_text_style_product(self):
        self.waits(self.selector_text_product_style)
        self._click(self.selector_text_product_style)
        self._click(self.selector_text_product_style_blockquote)

    def edit_name_product(self, value="Product#1"):
        self._input(self.selector_name_product, value)

    def save_changes(self):
        self._click(self.selector_product_save)

    def get_name_product(self):
        return self._get_attribute(self.selector_name_product, "value")
