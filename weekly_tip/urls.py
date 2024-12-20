from django.urls import path
from . import views

urlpatterns = [
    path('', views.weekly_tip, name='weekly_tip'),
]
