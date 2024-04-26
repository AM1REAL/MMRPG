from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@shared_task
def new_response(pk, title, user):
    html_content = render_to_string(
        'response_created.html',
        {
            'text': '',
            'link': f'{settings.SITE_URL}/posts/responses/{pk}'
        }
    )
    mgs = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=user
    )
    mgs.attach_alternative(html_content, 'text/html')
    mgs.send()

@shared_task
def response_accepted(pk, title, user):
    html_content = render_to_string(
        'response_created.html',
        {
            'text': '',
            'link': f'{settings.SITE_URL}/posts/{pk}'
        }
    )
    mgs = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=user
    )
    mgs.attach_alternative(html_content, 'text/html')
    mgs.send()

