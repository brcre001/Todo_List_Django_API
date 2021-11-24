from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class TodoList(APIView):
    
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        todo = request.data
        new_todo = Todo(label=todo["label"], done=todo["done"])
        new_todo.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
