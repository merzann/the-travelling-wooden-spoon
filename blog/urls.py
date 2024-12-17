from . import views
from django.urls import path

urlpatterns = [
    # Homepage URL
    path('', views.homepage, name='home'),
]
