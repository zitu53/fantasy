from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length = 100)
    owner = models.CharField(max_length = 100)
    played = models.IntegerField(default = 0)
    won = models.IntegerField(default = 0)
    drawn = models.IntegerField(default = 0)
    lost = models.IntegerField(default = 0)
    gd = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 10)
    team = models.ForeignKey(Team)
    goals = models.IntegerField(default = 0)
    assists = models.IntegerField(default = 0)
    price = models.FloatField(default = 0)
    points = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name
    
    
