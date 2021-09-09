# Generated by Django 3.2.5 on 2021-09-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MangaEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mal_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('chps', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('score', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('picture', models.ImageField(upload_to='')),
                ('rereading', models.BooleanField()),
                ('reread', models.IntegerField()),
                ('comments', models.CharField(max_length=300)),
                ('prio', models.IntegerField()),
            ],
        ),
    ]