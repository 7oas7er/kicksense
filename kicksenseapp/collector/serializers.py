from django.core.urlresolvers import reverse
from django.db import models
from rest_framework import serializers
from models import MoveEvent

class MoveEventSearializer(serializers.HyperlinkedModelSerializer):
    print('MoveEventSerealizer...')
    model = MoveEvent

