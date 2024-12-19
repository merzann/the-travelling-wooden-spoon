from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='home'),
    path('recipes/', views.recipes_view, name='recipes_view'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]
