import logging

from Common.BasicCommand import BasicCommand


class AdminPage(BasicCommand):
    AUTH = {'css': "div.panel-body > form > div.text-right > button"}
    logger = logging.getLogger(__name__)

    def auth(self):
        self.logger.info("Authentication")
        self._click(self.AUTH)
