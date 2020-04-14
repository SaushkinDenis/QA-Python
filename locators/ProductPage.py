import time
from os.path import abspath

from common.BasicCommand import BasicCommand


class ProductPage(BasicCommand):
    FIELD_NAME_PRODUCT = {'css': "#input-name1"}
    PRODUCT = {'css': "#language1 > div:nth-child(2) > div > div > div.note-toolbar.panel-heading > div.note-btn-group.btn-group.note-style > div"}
    STYLE_TEXT_INFORMATION_PRODUCT = {'css': PRODUCT['css'] + " > button"}
    STYLE_BLOCKQUOTE_TEXT_PRODUCT = {'css': PRODUCT['css'] + " > div > li:nth-child(4) > a"}
    BUTTON_SAVE = {'css': "#content > div.page-header > div > div > button"}
    MENU_IMAGE = {'css': "#form-product > ul > li:nth-child(9) > a"}
    FIRST_IMAGE = {'css': "#thumb-image"}
    BUTTON_EDIT_FIRST_IMAGE = {'css': "#button-image"}
    BUTTON_UPLOAD_FILE = {'css': "'#button-upload'"}
    FIELD_INPUT_FILE = {'css': "input[type='file']"}
    PATH_IMAGE = abspath("..") +"/common/image.png"
    LOAD_NEW_IMAGE = {'css': "#filemanager > div > div.modal-body > div:nth-child(3) > div:nth-child(4) > a"}

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

    def import_image(self):
        self._click(self.MENU_IMAGE)
        self._click(self.FIRST_IMAGE)
        self._click(self.BUTTON_EDIT_FIRST_IMAGE)
        time.sleep(2)
        self.driver.execute_script("$(" + self.BUTTON_UPLOAD_FILE['css'] + ").click();")
        self._input(self.FIELD_INPUT_FILE, self.PATH_IMAGE)
        self._click(self.LOAD_NEW_IMAGE)
        return self
