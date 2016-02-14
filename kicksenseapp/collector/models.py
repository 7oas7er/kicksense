from django.db import models
import datetime


class MoveEvent(models.Model):
    timestamp = models.FloatField(default=0)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return "timestamp: " + str(self.timestamp) + " x: " + str(self.x) + " y:" + str(self.y) + " z:" + str(self.z)
