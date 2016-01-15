from django.views.generic import ListView
from kicksenseapp.collector.models import MoveEvent

class MoveeventList(ListView):
    model = MoveEvent
    paginate_by = 12
    template_name = 'monitor/moveevent_list.html'
    context_object_name = 'moveevent'

    def get_queryset(self):
            try:
                a = self.request.GET.get('moveevent',)
            except KeyError:
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
        return super(MoveeventList, self).dispatch(*args, **kwargs)
