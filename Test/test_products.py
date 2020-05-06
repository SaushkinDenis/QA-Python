import logging
import time
import allure
import pytest

from Pages.AdminPage import AdminPage
from Pages.CouponsPage import CouponsPage
from Pages.MainPanel import MainPanel
from Pages.ProductPage import ProductPage
from Pages.ProductsPage import ProductsPage


class TestAdminPage:
    TEXT_NEW_NAME_PRODUCT = "Apple Cinema 30\""
    TEXT_FILTER_SEARCH = "Ipod"

    @allure.link("https://github.com/SaushkinDenis/QA-Python/tree/dz14")
    @allure.feature('Тестирование')
    @allure.story('Products')

    @allure.title("Редактирование продукта")
    @allure.description("описание теста")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_product(self, remote_browser):
        browser = remote_browser
        logger = logging.getLogger(__name__)
        logger.info("\nRunning " + __name__)
        AdminPage(browser).auth()

        ProductsPage(browser) \
            .first_product_selection() \
            .edit_name_product(self.TEXT_NEW_NAME_PRODUCT) \
            .edit_text_style_product() \
            .upload_image() \
            .save_changes()

        time.sleep(3)
        MainPanel(browser) \
            .open_catalog() \
            .first_product_selection()
        assert ProductPage(browser).get_name_product() == self.TEXT_NEW_NAME_PRODUCT
        logger.info("Stopped " + __name__)

    @allure.feature('Тестирование')
    @allure.story('Products')
    @allure.title("Добавление продукта")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_product(self, remote_browser):
        browser = remote_browser
        logger = logging.getLogger(__name__)
        logger.info("\nRunning " + __name__)
        AdminPage(browser).auth()

        before_int = ProductsPage(browser).get_len_elements()
        ProductsPage(browser) \
            .add_product() \
            .edit_name_product() \
            .upload_image() \
            .save_changes()

        time.sleep(2)
        MainPanel(browser).open_catalog()
        assert ProductsPage(browser).get_len_elements() - before_int == 1
        logger.info("Stopped " + __name__)

    @allure.feature('Тестирование')
    @allure.story('Products')
    @allure.title("Удаление продукта")
    @allure.severity(allure.severity_level.NORMAL)
    def test_del_product(self, remote_browser):
        browser = remote_browser
        logger = logging.getLogger(__name__)
        logger.info("\n Running " + __name__)
        AdminPage(browser).auth()

        before_int = ProductsPage(browser).get_len_elements()
        ProductsPage(browser).del_product()

        time.sleep(2)
        MainPanel(browser).open_catalog()
        assert before_int - ProductsPage(browser).get_len_elements() == 0
        logger.info("Stopped " + __name__)

    @allure.feature('Тестирование')
    @allure.story('Products')
    @allure.title("Использование фильтра поиска")
    @allure.severity(allure.severity_level.NORMAL)
    def test_use_filter(self, remote_browser):
        browser = remote_browser
        logger = logging.getLogger(__name__)
        logger.info("\n Running " + __name__)
        AdminPage(browser).auth()

        ProductsPage(browser) \
            .set_name_filter(self.TEXT_FILTER_SEARCH) \
            .active_filter()

        assert ProductsPage(browser).get_len_elements() == 4
        logger.info("Stopped " + __name__)

    @allure.story("Почта")
    @allure.title("Отправка почты")
    @allure.severity(allure.severity_level.NORMAL)
    def test_send_mail(self, remote_browser):
        browser = remote_browser
        logger = logging.getLogger(__name__)
        logger.info("\n Running " + __name__)
        AdminPage(browser).auth()
        MainPanel(browser) \
            .open_mail() \
            .create_mail() \
            .send_message()
        logger.info("Stopped " + __name__)

    @allure.story("Купоны")
    @allure.title("Создание купона")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_coupon(self, remote_browser):
        browser = remote_browser
        logger = logging.getLogger(__name__)
        logger.info("\n Running " + __name__)
        AdminPage(browser).auth()
        MainPanel(browser) \
            .open_coupons()

        before_int = CouponsPage(browser).get_len_coupons()
        CouponsPage(browser)\
            .create_coupons() \
            .save_coupons()

        time.sleep(2)
        MainPanel(browser) \
            .open_coupons()

        assert CouponsPage(browser).get_len_coupons() - before_int == 1
        logger.info("Stopped " + __name__)
