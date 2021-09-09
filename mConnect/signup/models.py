from django.db import models

# Importing other models
from animelist.models import AnimeEntry
from mangalist.models import MangaEntry

class userprofile(models.Model):
    # User Information
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField(default="email@email.com")
    bio = models.CharField(max_length=200)
    pfp = models.ImageField()
    # Keys to access list using APIs
    access_token = models.CharField(default='def_ac', max_length=400)
    refresh_token = models.CharField(default='def_rf', max_length=400)
    # For if the accounts are linked
    has_mal = models.BooleanField(default=False)
    has_mdx = models.BooleanField(default=False)
    # Lists
    anime_list = models.ForeignKey(AnimeEntry, on_delete=models.CASCADE, null=True)
    manga_list = models.ForeignKey(MangaEntry, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
