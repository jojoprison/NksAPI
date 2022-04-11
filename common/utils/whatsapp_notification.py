import configparser

import requests

from common.utils.paths import get_project_root_path


class WhatsAppNotificator:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(f'{get_project_root_path()}/config.ini')
        db_config = config['whatsapp']

        # phone_qdf phone_eug
        self.phone = db_config['phone_nks_1']
        # token_qdf token_eug
        self.token = db_config['token_nks_1']

    def send_message(self, text):
        payload = {
            'phone': self.phone,
            'token': self.token,
            'text': text
        }

        url = 'https://whin.inutil.info/whin'

        res = requests.post(url, data=payload)
        print(res.text)


if __name__ == '__main__':
    WhatsAppNotificator().send_message('ПРИВЕТ АНДРЕЙ')
