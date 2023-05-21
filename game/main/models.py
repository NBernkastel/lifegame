from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_lvl = models.IntegerField()
    user_hp = models.IntegerField()

    def __str__(self):
        return self.user.username


class Daylies(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    count = models.IntegerField(default=0)
    series = models.IntegerField(default=0)
    is_ready = models.BooleanField(default=False)


class Quests(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    is_ready = models.BooleanField(default=False)


class Habits(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    count = models.IntegerField(default=0)
    serial = models.IntegerField(default=0)
