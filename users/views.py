from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.http import JsonResponse
from django.views import View
import json
# from users.backend import MongoLoginBackend
from common_fun.models import LoginIdCred

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        print("==================================")
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        print("username:- ", username, "password:- ", password)
        # user = MongoLoginBackend().authenticate(request, username=username, password=password)
        user = LoginIdCred.objects.filter(login_id=username, login_password=password)
        if user:
            print("Found=============")
            return JsonResponse({"message": "Login successfully", "login_type": user[0].login_type}, status=200)
            # return JsonResponse({"message": "Login successful",})
        else:
            return JsonResponse({"message": "Invalid Loging Id or password"}, status=401)
        