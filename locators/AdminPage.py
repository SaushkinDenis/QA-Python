from common.BasicCommand import BasicCommand


class AdminPage(BasicCommand):

    AUTH = {'css': "div.panel-body > form > div.text-right > button"}

    def auth(self):
        self._click(self.AUTH)
