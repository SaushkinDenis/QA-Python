import logging

import allure

from Common.BasicCommand import BasicCommand


class AdminPage(BasicCommand):
    AUTH = {'css': "div.panel-body > form > div.text-right > button"}
    logger = logging.getLogger(__name__)

    @allure.step("Аутентификция")
    def auth(self):
        self.logger.info("Authentication")
        self._click(self.AUTH)
