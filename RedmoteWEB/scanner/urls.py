from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json/switches_info', views.json_switches_info, name='json_switches_info')
]
