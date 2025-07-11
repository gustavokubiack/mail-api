from django.core.mail import send_mail
from django.conf import settings
from subscribers.models import Subscriber


class EmailService:
    
    def send_email_to_new_subscriber(self, subscriber: Subscriber):
        """
        Sends a welcome email to a new subscriber.
        
        :param subscriber: The Subscriber instance to whom the email will be sent.
        """
        subject = "Bem-vindo ao nosso serviço de assinatura!"
        message = f"Olá {subscriber.name},\n\nObrigado por se inscrever em nosso serviço. Estamos felizes em tê-lo conosco!"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [subscriber.email]
        
        send_mail(subject, message, from_email, recipient_list)