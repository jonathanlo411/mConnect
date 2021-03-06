# Generated by Django 3.2.5 on 2021-09-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mal_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('eps', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('score', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('picture', models.ImageField(upload_to='')),
                ('rewatching', models.BooleanField()),
                ('rewatched', models.IntegerField()),
                ('comments', models.CharField(max_length=300)),
                ('prio', models.IntegerField()),
            ],
        ),
    ]
