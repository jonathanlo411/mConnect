from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class AnimeEntry(models.Model):
    mal_id = models.IntegerField() #anime id
    title = models.CharField(max_length=200) #title of anime
    eps = models.IntegerField() #num of eps watched
    status = models.CharField(max_length=30) #string determing status (ex. watching)
    score = models.IntegerField() #score that user gives
    rating  = models.IntegerField() #score that anime is rated
    picture = models.ImageField() #picture of anime
    rewatching = models.BooleanField() #bool of rewatching or not
    rewatched = models.IntegerField() #number of times user rewatched anime
    comments = models.CharField(max_length=300) #comments left by user
    prio = models.IntegerField() #int from 0-2

