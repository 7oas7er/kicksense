from django.db import models
import datetime


class MoveEvent(models.Model):
    timestamp = models.FloatField(default=0)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    class Meta:
        ordering = ['-timestamp']
