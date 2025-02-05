from django.urls import path
from.views import create_task, get_task, update_task, delete_task
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to the Task Management API!"})

urlpatterns=[
    path('', api_home, name='api_home'),
    path('tasks/create/',create_task,name='create_task'),
    path('tasks/',get_task,name='get_task'),
    path('tasks/<int:id>/',update_task,name='update_task'),
    path('tasks/<int:id>/',update_task,name='update_task'),
    path('tasks/<int:id>/delete/',delete_task,name='delete_task'),

]