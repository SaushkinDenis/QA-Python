from common.BasicCommand import BasicCommand


class ProductPage(BasicCommand):
    FIELD_NAME_PRODUCT = {'css': "#input-name1"}
    PRODUCT = {'css': "#language1 > div:nth-child(2) > div > div > div.note-toolbar.panel-heading > div.note-btn-group.btn-group.note-style > div"}
    STYLE_TEXT_INFORMATION_PRODUCT = {'css': PRODUCT['css'] + " > button"}
    STYLE_BLOCKQUOTE_TEXT_PRODUCT = {'css': PRODUCT['css'] + " > div > li:nth-child(4) > a"}
    BUTTON_SAVE = {'css': "#content > div.page-header > div > div > button"}

    def edit_text_style_product(self):
        self._click(self.STYLE_TEXT_INFORMATION_PRODUCT)
        self._click(self.STYLE_BLOCKQUOTE_TEXT_PRODUCT)
        return self

    def edit_name_product(self, value="Product#1"):
        self._input(self.FIELD_NAME_PRODUCT, value)
        return self

    def save_changes(self):
        self._click(self.BUTTON_SAVE)
        return self

    def get_name_product(self):
        return self._get_attribute(self.FIELD_NAME_PRODUCT, "value")
