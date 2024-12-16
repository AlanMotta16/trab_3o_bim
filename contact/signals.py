from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Contact

@receiver(post_save, sender=Contact)
def send_response_email(sender, instance, **kwargs):
    if instance.respondido and instance.resposta:
        send_mail(
            subject="Resposta ao seu contato",
            message=f"Olá {instance.nome},\n\n{instance.resposta}",
            from_email="contato@eventif.com.br",
            recipient_list=[instance.email],
            fail_silently=False,
        )
