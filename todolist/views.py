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
        """
        Returns the complete list of Todos
        """
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Creates a new Todo
        """

        # Data of the new todo coming in the request
        todo = request.data

        # Using information in request to generate a new todo
        new_todo = Todo.objects.create(label=todo["label"], done=todo["done"])
        
        # Saving the new todo to the database
        new_todo.save()

        # Serializing the data of the new todo for readability in JSON
        serializer = TodoSerializer(todo)

        # Returning the serialized new todo
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        todo_object = Todo.objects.get()

        data = request.data

        todo_object.label = data["label"]
        todo_object.done = data["done"]

        todo_object.save()

        serializer = TodoSerializer((todo_object))

        return Response(serializer.data)

    def delete(self, position):
        """
        Deletes a specific todo
        """
        remove_todo = request.data
