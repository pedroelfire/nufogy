from django.db import models

# Create your models here.

class message(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=500, null=True)