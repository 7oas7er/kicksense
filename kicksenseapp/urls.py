from django.conf.urls import url, include
from django.contrib import admin
from collector import views
from monitor.views import MoveeventList
import settings

urlpatterns = [
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin', include(admin.site.urls)),
    url(r'^moveevent/$', views.moveevent_list),
    url(r'^moveevent/(?P<pk>[0-9]+)/$', views.moveevent_detail),
    url(r'^monitor/list/$', MoveeventList.as_view(), name="moveevent_list"),
]