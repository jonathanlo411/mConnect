# Generated by Django 3.2.5 on 2021-11-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEntrys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, null=True)),
                ('date', models.DateField(null=True)),
                ('desc', models.CharField(max_length=500, null=True)),
                ('category', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]