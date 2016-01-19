from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import MoveEvent
from serializers import MoveEventSerializer
import logging

logger = logging.getLogger(__name__)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def moveevent_list(request):
    """
    List all move events, or create a new one.
    """

    logger.debug("moveevent_list...")

    if request.method == 'GET':
        logger.debug("GET received")
        moveevents = MoveEvent.objects.all()
        serializer = MoveEventSerializer(moveevents, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        logger.debug("POST received")
        logger.debug("Request body is " + request.body)
        data = JSONParser().parse(request)
        serializer = MoveEventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def moveevent_detail(request, pk):
    """
    Retrieve, update or delete a move event.
    """
    try:
        moveevent = MoveEvent.objects.get(pk=pk)
    except MoveEvent.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MoveEventSerializer(moveevent)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MoveEventSerializer(moveevent, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        moveevent.delete()
        return HttpResponse(status=204)

