from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserCharacteristics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sphere = models.CharField(max_length=40)
    b5_consc = models.FloatField(default=0.5)
    b5_extr = models.FloatField(default=0.5)
    b5_open = models.FloatField(default=0.5)
    b5_agree = models.FloatField(default=0.5)
    b5_neur = models.FloatField(default=0.5)
    is_startuper = models.BooleanField(default=False)
    twitter_username = models.CharField(max_length=100)
    instagram_username = models.CharField(max_length=100)
    money = models.FloatField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

class Interest(models.Model):
    name = models.CharField(max_length=30)

class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

class Like(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user2")

class Matchings(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")

# Create your models here.
