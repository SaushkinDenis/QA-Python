from common.BasicCommand import BasicCommand


class MailPage(BasicCommand):

    selector_select_author = {'css': "#input-store > option"}
    selector_open_select_to = {'css': "#input-to"}
    selector_select_to = {'css': "#input-to > option"}
    selector_subject = {'css': "#input-subject"}
    subject_text = "SUB"
    selector_message = {'css': "#content > div.container-fluid > div > div.panel-body > form > div:nth-child(8) > div > div > div.note-editing-area > div.note-editable.panel-body"}
    message_text = "New message"
    selector_send_mail_button = {'css': "#button-send"}

    def create_mail(self):
        self._click(self.selector_select_author)
        self._click(self.selector_open_select_to)
        self._click(self.selector_select_to, 3)
        self._input(self.selector_subject, self.subject_text)
        self._input(self.selector_message, self.message_text)

    def send_message(self):
        self._click(self.selector_send_mail_button)