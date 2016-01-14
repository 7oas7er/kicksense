from django.conf.urls import url
from collector import views

urlpatterns = [
    url(r'^moveevent/$', views.moveevent_list),
    url(r'^moveevent/(?P<pk>[0-9]+)/$', views.moveevent_detail),
]