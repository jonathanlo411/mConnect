# Generated by Django 3.2.5 on 2021-09-08 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20210906_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='access_token',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='refresh_token',
            field=models.IntegerField(default=0),
        ),
    ]
