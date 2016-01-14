from rest_framework import serializers
from models import MoveEvent


class MoveEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveEvent
        fields = ('x', 'y', 'z')
