# your_app_name/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timedelta
from .models import Service

def send_reminders():
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    services = Service.objects.filter(reminder_date=tomorrow)
    for service in services:
        send_mail(
            'Reminder: Upcoming Service',
            f'Don\'t forget, you have a service scheduled for {service.service_date}.',
            'sender@example.com',
            [service.vehicle.user.email],
            fail_silently=False,
        )
