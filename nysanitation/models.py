import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField


class user(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    resturants = ArrayField(models.CharField(max_length=100))

class resturants(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=100)
    Zipcode  = models.CharField(max_length=100)
    Address  = models.CharField(max_length=100)
    Sanitation = models.DecimalField()
    Sickness = models.IntegerField()

# Create your models here.
