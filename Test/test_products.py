from locators.locators import ListProductsPage, ProductPage, AdminPage

class Test_Admin_Page:

    def test_edit_product(self, browser):
        new_name_product = "Apple Cinema 35\""

        AdminPage(browser).auth()
        ListProductsPage(browser).first_product_selection()
        ProductPage(browser).edit_name_product(new_name_product)
        ProductPage(browser).edit_text_style_product()
        ProductPage(browser).save_changes()

        AdminPage(browser).open_catalog()
        ListProductsPage(browser).first_product_selection()
        assert ProductPage(browser).get_name_product() == new_name_product

    def test_add_product(self, browser):
        AdminPage(browser).auth()

        before_int = ListProductsPage(browser).get_len_elements()
        ListProductsPage(browser).add_product()
        ProductPage(browser).edit_name_product()
        ProductPage(browser).save_changes()

        AdminPage(browser).open_catalog()

        assert ListProductsPage(browser).get_len_elements() - before_int == 1

    def test_del_product(self, browser):
        AdminPage(browser).auth()

        before_int = ListProductsPage(browser).get_len_elements()
        ListProductsPage(browser).del_product()

        AdminPage(browser).open_catalog()

        assert before_int - ListProductsPage(browser).get_len_elements() == 1

