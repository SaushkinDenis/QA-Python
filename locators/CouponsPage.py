from common.BasicCommand import BasicCommand


class CouponsPage(BasicCommand):

    selector_add_coupons = {'css': "#content > div.page-header > div > div > a > i"}
    selector_create_name_coupons = {'css': "#input-name"}
    selector_create_code_coupons = {'css': "#input-code"}
    selector_create_costumer_login = {'css': "#tab-general > div:nth-child(6) > div > label:nth-child(1) > input[type=radio]"}
    selector_save_button = {'css': "#content > div.page-header > div > div > button"}
    selector_coupons_list = {'css': "#form-coupon > div > table > tbody > tr"}

    def create_coupons(self):
        self._click(self.selector_add_coupons)
        self._input(self.selector_create_name_coupons)
        self._input(self.selector_create_code_coupons)
        self._click(self.selector_create_costumer_login)

    def save_coupons(self):
        self._click(self.selector_save_button)

    def get_len_coupons(self):
        return self._get_len(self.selector_coupons_list)
