from django.views.generic import ListView
from kicksenseapp.collector.models import MoveEvent
from chartit import DataPool, Chart
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
            moveevent_list = MoveEvent.objects.all()
        return moveevent_list

    def dispatch(self, *args, **kwargs):
        logger.debug("dispatch...")
        return super(MoveeventList, self).dispatch(*args, **kwargs)

    def moveevent_chart_view(request):
     #Step 1: Create a DataPool with the data we want to retrieve.
        moveeventdata = \
            DataPool(
               series=
                [{'options': {
                   'source': MoveEvent.objects.all()},
                  'terms': [
                    'timestamp',
                    'x',
                    'y',
                    'z']}
                 ])
        #Step 2: Create the Chart object
        cht = Chart(
                datasource = moveeventdata,
                series_options =
                  [{'options':{
                      'type': 'line',
                      'stacking': False},
                    'terms':{
                      'timestamp': [
                        'x',
                        'y',
                        'z']
                      }}],
                chart_options =
                  {'title': {
                       'text': 'Move events of KickSense sensor over time'},
                   'xAxis': {
                        'title': {
                           'text': 'Time'}}})

        #Step 3: Send the chart object to the template.
        return render_to_response({'moveeventdata': cht})

