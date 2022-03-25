import requests

payload = {
        'phone': '79100938360',
        'token': '61ae9c33384068ab6673f4fd3c84611088776e58',
        'text': 'test_sq',
    }


def first():
    url = 'https://whin.inutil.info/whin'

    x = requests.post(url, data=payload)

    print(x.text)


if __name__ == '__main__':
    first()
