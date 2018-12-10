import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class resturant(models.Model):
    name  = models.CharField(max_length=100)
    cuisine  = models.CharField(max_length=100)
    score = models.IntegerField()
    borough = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    count = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurants_list = ArrayField(models.IntegerField(), default=list)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
