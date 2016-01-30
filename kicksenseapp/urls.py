from django.conf.urls import url, include
from django.contrib import admin
from kicksenseapp.collector import views
from kicksenseapp.monitor.views import MoveeventList
from kicksenseapp import settings

urlpatterns = [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin', include(admin.site.urls)),
    url(r'^moveevent/$', views.moveevent_list),
    url(r'^moveevent/(?P<pk>[0-9]+)/$', views.moveevent_detail),
    url(r'^monitor/list/$', MoveeventList.as_view(), name="moveevent_list"),
]