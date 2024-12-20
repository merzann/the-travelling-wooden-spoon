from . import views
from django.urls import path
from .views import delete_comment

urlpatterns = [
    path('', views.homepage, name='home'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('recipes/', views.recipes_view, name='recipes_view'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]
