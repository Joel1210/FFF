from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^invalid_registration$', views.register),
    url(r'^invalid_login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout)

]