from django.db import models

# Create your models here.

class NewsEntrys(models.Model):
    title = models.CharField(max_length=70, null=True)
    date = models.DateField(null=True)
    desc = models.CharField(max_length=500, null=True)
    category = models.CharField(max_length=30, null=True)