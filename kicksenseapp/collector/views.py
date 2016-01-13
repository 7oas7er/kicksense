from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from models import MoveEvent
from serializers import MoveEventSearializer

class MoveEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MoveEvent.objects.all().order_by('-date_joined')
    serializer_class = MoveEventSearializer