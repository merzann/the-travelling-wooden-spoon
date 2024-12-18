from . import views
from django.urls import path

urlpatterns = [
    # Homepage URL
    path('', views.homepage, name='home'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
]
