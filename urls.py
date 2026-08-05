from django.urls import path
from . import views

app_name="puapp"

urlpatterns=[
    path('', views.task_list, name='puapp_list'),]