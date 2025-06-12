from django.shortcuts import render
import uuid
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class AdminDashboard(APIView):
    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')

        print("username:- ", username)
        print("password:- ", password)
        token = str(uuid.uuid4())
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "Login successful", "username": username, "token": token})
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
