from django.urls import path
from . import views

urlpatterns = [
    path('create_todo/', views.create_todo, name='create_todo'),  # /todos/create_todo/
    path('', views.index, name='index'),  # /todos/  (목록/메인용)
]