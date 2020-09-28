from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create, name='create'),
    path('update/<int:pk>/',views.update, name='update'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    path('<int:article_pk>/comments/',views.comment_create,name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/',views.comment_delete,name='comment_delete'),
]
