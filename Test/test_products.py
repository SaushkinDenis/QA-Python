import logging
import time

from Pages.AdminPage import AdminPage
from Pages.CouponsPage import CouponsPage
from Pages.MainPanel import MainPanel
from Pages.ProductPage import ProductPage
from Pages.ProductsPage import ProductsPage


class TestAdminPage:
    TEXT_NEW_NAME_PRODUCT = "Apple Cinema 30\""
    TEXT_FILTER_SEARCH = "Ipod"

    def test_edit_product(self, remote):
        logger = logging.getLogger(__name__)
        logger.info("\nRunning " + __name__)
        AdminPage(remote).auth()

        ProductsPage(remote) \
            .first_product_selection() \
            .edit_name_product(self.TEXT_NEW_NAME_PRODUCT) \
            .edit_text_style_product() \
            .upload_image() \
            .save_changes()

        time.sleep(3)
        MainPanel(remote) \
            .open_catalog() \
            .first_product_selection()
        assert ProductPage(remote).get_name_product() == self.TEXT_NEW_NAME_PRODUCT
        logger.info("Stopped " + __name__)

    def test_add_product(self, remote):
        logger = logging.getLogger(__name__)
        logger.info("\nRunning " + __name__)
        AdminPage(remote).auth()

        before_int = ProductsPage(remote).get_len_elements()
        ProductsPage(remote) \
            .add_product() \
            .edit_name_product() \
            .upload_image() \
            .save_changes()

        time.sleep(2)
        MainPanel(remote).open_catalog()
        assert ProductsPage(remote).get_len_elements() - before_int == 1
        logger.info("Stopped " + __name__)

    def test_del_product(self, remote):
        logger = logging.getLogger(__name__)
        logger.info("\n Running " + __name__)
        AdminPage(remote).auth()

        before_int = ProductsPage(remote).get_len_elements()
        ProductsPage(remote).del_product()

        time.sleep(2)
        MainPanel(remote).open_catalog()
        assert before_int - ProductsPage(remote).get_len_elements() == 1
        logger.info("Stopped " + __name__)

    def test_use_filter(self, remote):
        logger = logging.getLogger(__name__)
        logger.info("\n Running " + __name__)
        AdminPage(remote).auth()

        ProductsPage(remote) \
            .set_name_filter(self.TEXT_FILTER_SEARCH) \
            .active_filter()

        assert ProductsPage(remote).get_len_elements() == 4
        logger.info("Stopped " + __name__)

    def test_send_mail(self, remote):
        logger = logging.getLogger(__name__)
        logger.info("\n Running " + __name__)
        AdminPage(remote).auth()
        MainPanel(remote) \
            .open_mail() \
            .create_mail() \
            .send_message()
        logger.info("Stopped " + __name__)

    def test_create_coupon(self, remote):
        logger = logging.getLogger(__name__)
        logger.info("\n Running " + __name__)
        AdminPage(remote).auth()
        MainPanel(remote) \
            .open_coupons()

        before_int = CouponsPage(remote).get_len_coupons()
        CouponsPage(remote)\
            .create_coupons() \
            .save_coupons()

        time.sleep(2)
        MainPanel(remote) \
            .open_coupons()

        assert CouponsPage(remote).get_len_coupons() - before_int == 1
        logger.info("Stopped " + __name__)
