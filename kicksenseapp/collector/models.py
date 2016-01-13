from django.db import models

class MoveEvent(models.Model):
    x = models.FloatField
    y = models.FloatField
    z = models.FloatField
    kicker = models.ForeignKey(Kicker, editable=False, related_name="Kicker")


class Kicker(models.Model):
    id = models.CharField

