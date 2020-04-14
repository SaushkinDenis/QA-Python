from common.BasicCommand import BasicCommand
from locators.CouponsPage import CouponsPage
from locators.MailPage import MailPage
from locators.ProductsPage import ProductsPage


class MainPanel(BasicCommand):

    MENU_CATALOG = {'css': "#menu-catalog > a"}
    MENU_PRODUCTS = {'css': "#collapse1 > li:nth-child(2) > a"}
    MENU_MARKETING = {'css': "#menu-marketing > a"}
    MENU_MARKETING_MAIL = {'css': "#collapse38 > li:nth-child(3) > a"}
    MENU_MARKETING_COUPONS = {'css': "#collapse38 > li:nth-child(2) > a"}

    def open_catalog(self):
        self._click(self.MENU_CATALOG)
        self._click(self.MENU_PRODUCTS)
        return ProductsPage(self.driver)

    def open_mail(self):
        self._click(self.MENU_MARKETING)
        self._click(self.MENU_MARKETING_MAIL)
        return MailPage(self.driver)

    def open_coupons(self):
        self._click(self.MENU_MARKETING)
        self._click(self.MENU_MARKETING_COUPONS)
        return CouponsPage(self.driver)
