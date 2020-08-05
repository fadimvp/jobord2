# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.fields import related
from django.utils.text import slugify

JobType = (
    ('full time ', 'Full Time'),
    ('part time ', 'Part Time '),
)


def image_upload(instnce, filename):
    image_name, exxtention = filename.split(".")
    return "jobs/%s/%s.%s" % (instnce.title, instnce.image, exxtention)


class Job(models.Model):
    owner = models.ForeignKey(User, related_name='owner_job', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=25, choices=JobType)
    publish_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField()
    experience = models.IntegerField(default=1)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_ob', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    cv = models.FileField()
    cover_letter = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
