# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

from  django.conf import settings

# Create your views here.
def send_message(request):
    info = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['sub']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],

        )
    context = {
        'info': info,
    }
    return render(request, 'contact.html', context)
