# Generated by Django 3.2.5 on 2021-09-10 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_auto_20210909_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='access_token',
            field=models.CharField(default='def_ac', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='refresh_token',
            field=models.CharField(default='def_rf', max_length=2000),
        ),
    ]
