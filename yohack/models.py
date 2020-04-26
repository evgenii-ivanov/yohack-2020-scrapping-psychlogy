from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserCharacteristics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sphere = models.CharField(max_length=40)
    b5_consc = models.FloatField()
    b5_extr = models.FloatField()
    b5_open = models.FloatField()
    b5_agree = models.FloatField()
    b5_neur = models.FloatField()
    is_startuper = models.BooleanField(default=False)
    twitter_username = models.CharField(max_length=100)
    instagram_username = models.CharField(max_length=100)

class Interest(models.Model):
    name = models.CharField(max_length=30)

class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)



# Create your models here.
