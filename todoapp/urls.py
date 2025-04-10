from django.urls import path
from .views import TodoListCreateAPIView, TodoDetailAPIView

urlpatterns = [
    path('todo/', TodoListCreateAPIView.as_view(), name='todo_list_create'),
    path('todo/<int:pk>/', TodoDetailAPIView.as_view(), name='todo_detail'),
]
