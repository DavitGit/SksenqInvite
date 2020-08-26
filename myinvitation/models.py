# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Invitation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=350)

    def __str__(self):
        return self.name + " - " + self.gmail
