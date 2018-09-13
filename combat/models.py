from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200)
    perception = models.IntegerField(default=10)
    armorclass = models.IntegerField(default=10)
    hitpoints = models.IntegerField(default=30)
    initiative = models.IntegerField(default=0)
    def __str__(self):
        return self.name
