from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserCharacteristics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extraversion = models.FloatField()
    benevolence = models.FloatField()
    good_faith = models.FloatField()
    neuroticism = models.FloatField()
    intelligence = models.FloatField()

class Interest(models.Model):
    name = models.CharField(max_length=30)

class UserInterest:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)



# Create your models here.
