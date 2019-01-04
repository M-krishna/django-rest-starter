from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeModel
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeView(APIView):

    def get(self, request):
        employees = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        values = request.data
        empserializer = EmployeeSerializer(data = values)
        if empserializer.is_valid():
            empserializer.save()
            return Response({},status.HTTP_200_OK)
    
    def put(self, request):
        values = EmployeeModel.objects.get(emp_id=request.data.get('emp_id'))
        values.firstname = request.data.get('firstname')
        values.lastname = request.data.get('lastname')
        values.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            values = EmployeeModel.objects.get(emp_id=request.data.get('emp_id'))
            values.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            values = None
            return Response(status=status.HTTP_404_NOT_FOUND)
