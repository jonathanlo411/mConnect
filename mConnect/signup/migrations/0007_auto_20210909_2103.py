# Generated by Django 3.2.5 on 2021-09-10 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_auto_20210909_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='anime_list',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='manga_list',
        ),
    ]
