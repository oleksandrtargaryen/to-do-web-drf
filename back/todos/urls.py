from django.urls import path
from .views import TodoDetailAPIView, TodoListCreateAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name = 'todo_list_create'),
    path('todos/<int:todo_id>/', TodoDetailAPIView.as_view(), name = 'todo_detail'),
]