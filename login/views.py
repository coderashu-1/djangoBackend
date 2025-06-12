from django.shortcuts import render
import uuid
# from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from common_fun.models import LoginIdCred
import json

# Create your views here.

class LoginAuth(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            # print("username:- ", username)
            # print("password:- ", password)
            
            token = str(uuid.uuid4())
            # user = authenticate(username=username, password=password)

            try:
                user = LoginIdCred.objects.filter(login_id=username, login_password=password)
                if user:
                    userType = user[0].login_type
                    return JsonResponse({"message": "Login successful", "status": "success", "username": username, "userType": userType, "token": token}, status=200)
                else:
                    return JsonResponse({"message": "Login ID or Password is incorrect", "status": "fail"}, status=400)

            except:
                return JsonResponse({"message": "Login ID or Password is incorrect", "status": "fail"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON", "status": "fail"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e), "status": "fail"}, status=500)
