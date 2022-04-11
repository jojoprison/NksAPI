from django.core.mail import send_mail

from NksAPI import settings


class EmailNotificator:
    def send_email(self, text):
        send_mail(
            subject='Заказ test',
            message=text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=settings.RECIPIENT_ADDRESS.split(','),
            fail_silently=False,
        )


if __name__ == '__main__':
    EmailNotificator().send_email('Тестовое сообщение')
