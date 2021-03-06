# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to="profile/")

    def __str__(self):
        # return self.user.username
        return str(self.user)
    ## create new user  ----------->  create new profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):

        return self.city
