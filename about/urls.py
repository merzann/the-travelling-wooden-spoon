from django.urls import path
from . import views

urlpatterns = [
    # Other URLs
    path('', views.about_page, name='about_page'),
]
