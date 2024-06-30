from django.db import models

class Request(models.Model):
    text = models.CharField(max_length=100)