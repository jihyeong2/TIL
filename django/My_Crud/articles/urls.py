from . import views
from django.urls import path
app_name='articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:article_pk>/', views.update, name='update'),
    path('detail/<int:article_pk>/', views.detail, name='detail'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
]