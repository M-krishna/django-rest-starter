from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentModel
from .serializers import StudentSerializer

# Create your views here.
class StudentView(APIView):
    def get(self, request):
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        values = request.data
        stuSerializer = StudentSerializer(data = values)
        if stuSerializer.is_valid():
            stuSerializer.save()
            return Response({"message": 'Created'}, status=status.HTTP_201_CREATED)
        
    def put(self, request):
        pass

    def delete(self, request):
        try:
            values = StudentModel.objects.get(id = request.data.get('id'))
            values.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            values = None
            return Response({"message": "Not Exist"}, status=status.HTTP_404_NOT_FOUND)