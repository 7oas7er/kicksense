from django.db import models
import datetime


class MoveEvent(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    class Meta:
        ordering = ['-timestamp']


