from django.db import models


class user(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    resturants = models.ArrayField(models.CharField(max_length=100))

class resturants(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=100)
    Zipcode  = models.CharField(max_length=100)
    Address  = models.CharField(max_length=100)
    Sanitation = models.DecimalField(max_digits=999, decimal_places=2)
    Sickness = models.IntergerField()

# Create your models here.
