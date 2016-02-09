from django.conf.urls import url, include
from django.contrib import admin
from kicksenseapp.collector import views as collector_views
from kicksenseapp.monitor import views as monitor_views
from kicksenseapp import settings

urlpatterns = [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin', include(admin.site.urls)),
    url(r'^moveevent/$', collector_views.moveevent_list),
    url(r'^moveevent/(?P<pk>[0-9]+)/$', collector_views.moveevent_detail),
    url(r'^monitor/chart/$', monitor_views.moveevent_chart_view, name="moveevent_chart"),
    url(r'^monitor/list/$', monitor_views.MoveeventList.as_view(), name="moveevent_list"),
]