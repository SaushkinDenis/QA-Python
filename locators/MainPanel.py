from common.BasicCommand import BasicCommand


class MainPanel(BasicCommand):

    selector_menu_catalog = {'css': "#menu-catalog > a"}
    selector_menu_products = {'css': "#collapse1 > li:nth-child(2) > a"}
    selector_menu_marketing = {'css': "#menu-marketing > a"}
    selector_menu_marketing_mail = {'css': "#collapse38 > li:nth-child(3) > a"}
    selector_marketing_coupons = {'css': "#collapse38 > li:nth-child(2) > a"}

    def open_catalog(self):
        self._click(self.selector_menu_catalog)
        self._click(self.selector_menu_products)
        return

    def open_mail(self):
        self._click(self.selector_menu_marketing)
        self._click(self.selector_menu_marketing_mail)

    def open_coupons(self):
        self._click(self.selector_menu_marketing)
        self._click(self.selector_marketing_coupons)