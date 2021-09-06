from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class userprofile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField(default="email@email.com")
    bio = models.CharField(max_length=200)
    pfp = models.ImageField()

