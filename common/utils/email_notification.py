import configparser

from django.core.mail import send_mail

from common.utils.paths import get_project_root_path


class EmailNotificator:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(f'{get_project_root_path()}/config.ini')
        db_config = config['email']

        self.email_from = db_config['email_from']
        self.email_to = db_config['email_to']

    def send_email(self, text):
        send_mail(
            'Заказ test',
            text,
            self.email_from,
            [self.email_to],
            fail_silently=False,
        )


if __name__ == '__main__':
    EmailNotificator().send_email('Тестовое сообщение')
