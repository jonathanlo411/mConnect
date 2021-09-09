from django.db import models

# Create your models here.

class MangaEntry(models.Model):
    mal_id = models.IntegerField() #manga id
    title = models.CharField(max_length=200) #title of manga
    chps = models.IntegerField() #num of ch read
    status = models.CharField(max_length=30) #string determing status (ex. watching)
    score = models.IntegerField() #score that user gives
    rating  = models.IntegerField() #score that manga is rated
    picture = models.ImageField() #picture of manga
    rereading = models.BooleanField() #bool of rereadingg or not
    reread = models.IntegerField() #number of times user reread manga
    comments = models.CharField(max_length=300) #comments left by user
    prio = models.IntegerField() #int from 0-2

    def __str__(self):
        return self.title