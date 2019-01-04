from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import TodoModel
from .serializers import TodoSerializer

# Create your views here.
class TodoView(APIView):

    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        values = TodoModel.objects.all()    
        todo = TodoSerializer(values, many = True)
        return Response(todo.data)

    def post(self, request):
        values = request.data
        todoserializer = TodoSerializer(data = values)
        if todoserializer.is_valid():
            todoserializer.save()
            return Response({"message": "Todo created"}, status = status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            value = TodoModel.objects.get(id = request.data.get('id'))
            value.delete()
            return Response({"message":"Deleted Successfully"}, status = status.HTTP_200_OK)
        except Exception:
            value = None
            return Response({"message":"Not Found"}, status = status.HTTP_404_NOT_FOUND)

class GetOneTodoView(APIView):
    
    def get(self, request, *args, **kwargs):
        try:
            todo = TodoModel.objects.get(id = self.kwargs['pk'])
            value = TodoSerializer(todo)
            return Response(value.data)
        except Exception:
            return Response({"message": "Not Found"}, status = status.HTTP_404_NOT_FOUND)

