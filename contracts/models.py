# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contract(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    amount = models.FloatField('contract amount')
    untreated = models.BooleanField()
    user_from = models.CharField(max_length=200)
    user_to = models.CharField(max_length=200)
    description = models.TextField()
