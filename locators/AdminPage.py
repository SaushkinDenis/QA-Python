from common.BasicCommand import BasicCommand


class AdminPage(BasicCommand):

    selector_auth = {'css': "div.panel-body > form > div.text-right > button"}

    def auth(self):
        self._click(self.selector_auth)
