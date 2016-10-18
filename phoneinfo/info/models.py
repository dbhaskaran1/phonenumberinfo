from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PhoneInfo(models.Model):
   phone_number = models.CharField(max_length=15)
   country = models.CharField(max_length=2)
   carrier = models.CharField(max_length=15)
