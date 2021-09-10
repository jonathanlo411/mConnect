from django.db import models


class userprofile(models.Model):
    # User Information
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField(default="email@email.com")
    bio = models.CharField(max_length=200)
    pfp = models.ImageField()
    # Keys to access list using APIs
    access_token = models.CharField(default='def_ac', max_length=2000)
    refresh_token = models.CharField(default='def_rf', max_length=2000)
    # For if the accounts are linked
    has_mal = models.BooleanField(default=False)
    has_mdx = models.BooleanField(default=False)

    def __str__(self):
        return self.username
