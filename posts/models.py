# BLOGSTER by Alexander Abraham
# a.k.a. "The Black Unicorn" a.k.a. "Angeldust Duke".
# Licensed under the MIT license.

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=2000)
    description = models.CharField(max_length=20000)
    body = models.TextField(max_length=200000)
    date = models.DateTimeField(verbose_name='date',auto_now=True)
    def __str__(self):
        return self.title
