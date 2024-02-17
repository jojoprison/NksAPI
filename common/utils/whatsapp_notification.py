import configparser

import requests

from common.utils.paths import get_project_root_path


class WhatsAppNotificator:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(f'{get_project_root_path()}/config.ini')
        db_config = config['whatsapp']

        # self.recipients = ({'phone': db_config['phone_nks_1'], 'token': db_config['token_nks_1']},
        #                    {'phone': db_config['phone_nks_2'], 'token': db_config['token_nks_2']},
        #                    {'phone': db_config['phone_nks_3'], 'token': db_config['token_nks_3']},
        #                    {'phone': db_config['phone_qdf'], 'token': db_config['token_qdf']})
        # debug
        self.recipients = ({'phone': db_config['phone_qdf'], 'token': db_config['token_qdf']},)

        # self.phone = db_config['phone_nks_1']
        # self.token = db_config['token_nks_1']

    def send_message(self, text):
        # for recipient in self.recipients:
        config = configparser.ConfigParser()
        config.read(f'{get_project_root_path()}/config.ini')
        db_config = config['whatsapp']
        payload = {
            'phone': db_config['phone_nks'],
            'token': db_config['token_nks'],
            'text': text
        }

        url = 'https://whin.inutil.info/whin'

        requests.post(url, data=payload)


if __name__ == '__main__':
    WhatsAppNotificator().send_message('ПРИВЕТ АНДРЕЙ')
