# Generated by Django 2.1.4 on 2018-12-10 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nysanitation', '0002_resturant_violation'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturant',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]