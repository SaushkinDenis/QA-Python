from locators.AdminPage import AdminPage
from locators.CouponsPage import CouponsPage
from locators.MailPage import MailPage
from locators.MainPanel import MainPanel
from locators.ProductPage import ProductPage
from locators.ProductsPage import ProductsPage


class TestAdminPage:

    def test_edit_product(self, browser):
        new_name_product = "Apple Cinema 35\""
        AdminPage(browser).auth()

        ProductsPage(browser).first_product_selection()
        ProductPage(browser).edit_name_product(new_name_product)
        ProductPage(browser).edit_text_style_product()
        ProductPage(browser).save_changes()

        MainPanel(browser).open_catalog()
        ProductsPage(browser).first_product_selection()
        assert ProductPage(browser).get_name_product() == new_name_product

    def test_add_product(self, browser):
        AdminPage(browser).auth()

        before_int = ProductsPage(browser).get_len_elements()
        ProductsPage(browser).add_product()
        ProductPage(browser).edit_name_product()
        ProductPage(browser).save_changes()

        MainPanel(browser).open_catalog()
        assert ProductsPage(browser).get_len_elements() - before_int == 1

    def test_del_product(self, browser):
        AdminPage(browser).auth()

        before_int = ProductsPage(browser).get_len_elements()
        ProductsPage(browser).del_product()

        MainPanel(browser).open_catalog()
        assert before_int - ProductsPage(browser).get_len_elements() == 1

    def test_use_filter(self, browser):
        AdminPage(browser).auth()

        ProductsPage(browser).set_name_filter("Ipod")
        ProductsPage(browser).active_filter()
        assert ProductsPage(browser).get_len_elements() == 4

    def test_send_mail(self, browser):
        AdminPage(browser).auth()
        MainPanel(browser).open_mail()

        MailPage(browser).create_mail()
        MailPage(browser).send_message()

    def test_create_coupon(self, browser):
        AdminPage(browser).auth()
        MainPanel(browser).open_coupons()

        before_int = CouponsPage(browser).get_len_coupons()
        CouponsPage(browser).create_coupons()
        CouponsPage(browser).save_coupons()

        assert CouponsPage(browser).get_len_coupons() - before_int == 1
