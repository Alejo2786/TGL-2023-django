

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def enviar_correo_confirmacion(email):
    send_mail(
        'Confirmación de cuenta',
        'Gracias por registrarte en nuestro blog.',
        'noreply@example.com',
        [email],
        fail_silently=False,
    )
