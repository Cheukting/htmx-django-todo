from django.urls import path

from tasks.views import delete_task, display_tasks, create_task

urlpatterns = [
    path('create_task/', create_task, name='create_task'),
    path('tasks/', display_tasks, name='display_tasks'),
    path('tasks/<int:id>/delete/', delete_task, name='delete_task'),
]
