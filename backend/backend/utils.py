from django.core.mail.message import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site

def send_email(request, email, subject=' ', message=' ',html=' '):
    """
    request
    email
    subject
    message
    html
    """
    mail= EmailMultiAlternatives(subject,message, to=[email])
    if html != ' ':
        mail.attach_alternative(html, 'text/html')
    mail.send()