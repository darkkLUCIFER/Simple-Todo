from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>/', views.todo_detail, name='detail'),
    path('delete/<int:pk>/', views.todo_delete, name='delete'),
    path('new_todo/', views.todo_create, name='new_todo'),
    path('update-todo/<int:pk>/',views.update_todo,name= 'update_todo')
]
