from django.views.generic import ListView
from kicksenseapp.collector.models import MoveEvent
from chartit import DataPool, Chart
from django.shortcuts import render
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
                  #'pointStart': 'Date.UTC(2016,1,14)',
                  #'pintInterval':'1000',
                  'type': 'spline',
                  'stacking': False},
                'terms':{
                  'timestamp': [
                    'x',
                    'y',
                    'z']
                  }}],
            chart_options =
              {
                'zoomType': 'x',
                'title': {'text': 'Move events of KickSense sensor over time'},
                'xAxis': {'title': {'text': 'Time'}, 'type':'datetime', 'dateTimeLabelFormats':
                                {'millisecond':"%A, %b %e, %H:%M:%S.%L",
                                 'second':"%A, %b %e, %H:%M:%S",'minute':"%A, %b %e, %H:%M",
                                 'hour':"%A, %b %e, %H:%M",
                                 'day':"%A, %b %e, %Y",
                                 'week':"Week from %A, %b %e, %Y",
                                 'month':"%B %Y",
                                 'year':"%Y"},
                          'units': [['millisecond',	['500']]],
                          'tickinterval':'3600*1000'},
                'legend': {'align': 'left','verticalAlign':'middle','layout':'vertical'},
                'tooltip': {'dateTimeLabelFormats':
                                {'millisecond':"%A, %b %e, %H:%M:%S.%L",
                                 'second':"%A, %b %e, %H:%M:%S",'minute':"%A, %b %e, %H:%M",
                                 'hour':"%A, %b %e, %H:%M",
                                 'day':"%A, %b %e, %Y",
                                 'week':"Week from %A, %b %e, %Y",
                                 'month':"%B %Y",
                                 'year':"%Y"}
                            }
              }
    )

    #Step 3: Send the chart object to the template.
    return render(request,'monitor/moveevent_chart.html',{'moveeventchart': cht})

