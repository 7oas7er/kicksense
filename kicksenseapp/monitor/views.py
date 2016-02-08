from django.views.generic import ListView
from kicksenseapp.collector.models import MoveEvent
import logging

logger = logging.getLogger(__name__)

class MoveeventList(ListView):

    logger.debug("MoveeventList ...")

    model = MoveEvent
    paginate_by = 12
    template_name = 'monitor/moveevent_list.html'
    context_object_name = 'moveevents'

    def get_queryset(self):

        logger.debug("get_queryset...")

        try:
            a = self.request.GET.get('moveevent',)
        except KeyError:
            logger.error("KeyError caught")
            a = None
        if a:
            moveevent_list = MoveEvent.objects.filter(
                name__icontains=a,
                owner=self.request.user
            )
        else:
            moveevent_list = MoveEvent.objects.all().order_by('-timestamp')
        return moveevent_list

    def dispatch(self, *args, **kwargs):
        logger.debug("dispatch...")
        return super(MoveeventList, self).dispatch(*args, **kwargs)
