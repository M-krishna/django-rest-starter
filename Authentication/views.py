from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SignUp
from .serializers import SignUpSerializer

# Create your views here.
class SignUpView(APIView):
    def get(self, request):
        values = request.data
        serializer = SignUpSerializer(values, many = True)
        return Response(serializer.data)
    def post(self, request):
        try:
            user = SignUp.objects.get(email = request.data.get('email'))
            if user:
                return Response({"message": "User ALready Exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            user = SignUp.objects.create(
                firstname = request.data.get('firstname'),
                lastname = request.data.get('lastname'),
                email = request.data.get('email'),
                phone = request.data.get('phone')
            )
            return Response({"message":"Sign up successfull"}, status = status.HTTP_201_CREATED)
        
