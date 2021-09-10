from django.db import models
from signup.models import userprofile
# Create your models here.

class AnimeEntry(models.Model):
    mal_id = models.IntegerField(null=True) #anime id
    title = models.CharField(max_length=200, null=True) #title of anime
    eps = models.IntegerField(null=True) #num of eps watched
    t_eps = models.IntegerField(null=True) #total num of eps in anime
    desc = models.CharField(max_length=5000, null=True) #description of the anime
    status = models.CharField(max_length=30, null=True) #userside string determing status (ex. watching)
    score = models.IntegerField(null=True) #score that user gives
    mean  = models.FloatField(null=True) #score that anime is rated
    picture = models.CharField(max_length=400, null=True) #url of picture of anime
    rewatching = models.BooleanField(null=True) #bool of rewatching or not
    rewatched = models.IntegerField(null=True) #number of times user rewatched anime
    comments = models.CharField(max_length=300, null=True) #comments left by user
    prio = models.IntegerField(null=True) #int from 0-2
    studio = models.CharField(max_length=50, null=True) #studio that made the anime
    airing_time = models.CharField(max_length=30, null=True) #season, year the anime started
    anime_status = models.CharField(max_length=20, null=True) #status of the anime (ex. finished airing)
    source = models.CharField(max_length=20, null=True) #source of the anime (ex. manga)
    genres = models.CharField(max_length=50, null=True) #genres of the anime 
    ranked = models.IntegerField(null=True) #rank where the anime is rated (scoring)
    popularity = models.IntegerField(null=True) #rank where the anime is popular (list popularity)
    members = models.IntegerField(null=True) #number of people that have the anime in their list
    link = models.CharField(max_length=200, null=True) #link to MAL entry
    alt_title = models.CharField(max_length=200, null=True) #alternative title (in jp)

    #user
    userp = models.ForeignKey(to=userprofile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

