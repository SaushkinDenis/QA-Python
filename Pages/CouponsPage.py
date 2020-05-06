import logging

import allure

from Common.BasicCommand import BasicCommand


class CouponsPage(BasicCommand):

    BUTTON_ADD_COUPONS = {'css': "#content > div.page-header > div > div > a > i"}
    FIELD_NAME_COUPONS = {'css': "#input-name"}
    FIELD_CODE_COUPONS = {'css': "#input-code"}
    BUTTON_COSTUMER_LOGIN = {'css': "#tab-general > div:nth-child(6) > div > label:nth-child(1) > input[type=radio]"}
    BUTTON_SAVE = {'css': "#content > div.page-header > div > div > button"}
    LIST_COUPONS = {'css': "#form-coupon > div > table > tbody > tr"}

    logger = logging.getLogger(__name__)

    @allure.step("Создание")
    def create_coupons(self):
        self.logger.info("Create coupons")
        self._click(self.BUTTON_ADD_COUPONS)
        self._input(self.FIELD_NAME_COUPONS)
        self._input(self.FIELD_CODE_COUPONS)
        self._click(self.BUTTON_COSTUMER_LOGIN)
        return self

    @allure.step("Сохранение")
    def save_coupons(self):
        self.logger.info("Save coupons")
        self._click(self.BUTTON_SAVE)

    def get_len_coupons(self):
        return self._get_len(self.LIST_COUPONS)
