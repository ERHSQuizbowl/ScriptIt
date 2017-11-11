# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Document(models.Model):
    document = models.FileField(upload_to='documents/')