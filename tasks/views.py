from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer


@api_view(['POST'])
def create_task(request):
    """Create a new a task"""
    serializer= TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_401_BAD_REQUEST)

@api_view(['GET'])
def get_task(request):
    """Fetch all task"""
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT'])
def update_task(request, id):
    """Update a task"""
    try:
        task=Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({"Error":"Task not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer=TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer=TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request, id):
    """Delete a Task"""
    try:
        task= Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({"Error":"Task not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)