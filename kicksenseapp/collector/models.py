from django.db import models

class MoveEvent(models.Model):
    x = models.FloatField
    y = models.FloatField
    z = models.FloatField


