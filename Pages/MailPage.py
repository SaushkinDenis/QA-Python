import logging

from Common.BasicCommand import BasicCommand



class MailPage(BasicCommand):
    FIELD_AUTHOR = {'css': "#input-store > option"}
    BUTTON_OPEN_SELECT_FROM = {'css': "#input-to"}
    BUTTON_SELECT_TO = {'css': "#input-to > option"}
    FIELD_SUBJECT = {'css': "#input-subject"}
    TEXT_SUBJECT = "SUB"
    FIELD_MESSAGE = {'css': "#content > div.container-fluid > div > div.panel-body > form > div:nth-child(8) > div > div > div.note-editing-area > div.note-editable.panel-body"}
    TEXT_MESSAGE = "New message"
    BUTTON_SEND_MAIL = {'css': "#button-send"}

    logger = logging.getLogger("MailPage")

    def create_mail(self):
        self.logger.info("Create mail")
        self._click(self.FIELD_AUTHOR)
        self._click(self.BUTTON_OPEN_SELECT_FROM)
        self._click(self.BUTTON_SELECT_TO, 3)
        self._input(self.FIELD_SUBJECT, self.TEXT_SUBJECT)
        self._input(self.FIELD_MESSAGE, self.TEXT_MESSAGE)
        return self

    def send_message(self):
        self.logger.info("Send mail")
        self._click(self.BUTTON_SEND_MAIL)