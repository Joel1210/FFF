from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forumslist$', views.list),
    url(r'^forums/(?P<event_id>\d+)$', views.forum), 
    url(r'^postcomment$', views.postComment),
    

]