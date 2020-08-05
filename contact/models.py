# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Info(models.Model):
    place = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=245)

    class Meta:
        verbose_name = 'INFO'
        verbose_name_plural = 'INFOS'
    def __str__(self):
            return self.email

