from ..models import Todo
from django.shortcuts import get_object_or_404


def get_user_todos(user):
    return Todo.objects.filter(user=user).order_by('-created_at')



def create_todo(user, data):
    return Todo.objects.create(
        user=user,
        title=data.get('title'),
        content=data.get('description','')
        )


def get_todo_by_id(user, todo_id):
    return get_object_or_404(user=user, id=todo_id)


def update_todo(user, todo_id, data):
    todo = get_todo_by_id(user, todo_id)
    todo.title = data.get('title', todo.title)
    todo.content = data.get('content', todo.content)
    todo.completed = data.get('completed', todo.completed)
    todo.save()
    return todo


def delete_todo(user, todo_id):
    todo = get_todo_by_id(user, todo_id)
    todo.delete()
    return True

