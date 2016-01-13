from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from models import MoveEvent
from serializers import MoveEventSearializer

class MoveEventViewSet(viewsets.ModelViewSet):
    print("MoveEventViewSet...")

    queryset = MoveEvent.objects.all()

    print(queryset)

    serializer_class = MoveEventSearializer