from django.urls import path
from django.conf.urls import url
from querybuilderapp import views

urlpatterns = [
    path('', views.home, name='qbhome',),
]