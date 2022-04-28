from django.core.mail import send_mail

from NksAPI import settings


class EmailNotificator:
    def send_email(self, order_id, text):
        send_mail(
            subject=f'Заказ №{order_id}',
            message=text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=settings.RECIPIENT_ADDRESS.split(','),
            fail_silently=False,
        )


if __name__ == '__main__':
    EmailNotificator().send_email(1, 'Тестовое сообщение')
