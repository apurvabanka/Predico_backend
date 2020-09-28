from django.shortcuts import render
from rest_framework import status
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerial,serializeResult
# from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import result
from django.contrib.auth.hashers import make_password
from dataCluster.views import cluster
from requests import request
import requests
import logging

logger = logging.getLogger("User Login")



class func(APIView):
    authentication_classes = [TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        num1 = request.GET.get('num1',False)
        num2 = request.GET.get('num2',False)
        if(not num1 or not num2):
            return HttpResponse("<h3>Please enter both entries</h3>")
        try:
            obj = result.objects.get(operation="add",num1=num1,num2=num2)
        except result.DoesNotExist:
            sum = int(num1)+int(num2)
            save_sum = result(operation="add",num1=num1,num2=num2,result=sum)
            save_sum.save()
            return HttpResponse(sum)
        serialize = serializeResult(obj)
        return response.Response(serialize.data['result'])
    def post(self,request):
        num1 = request.data.get('num1',"")
        num2 = request.data.get('num2',"")
        if(num1 == "" or num2 == ""):
            return HttpResponse("Please enter both entries")
        try:
            obj = result.objects.get(operation="sub",num1=num1,num2=num2)
        except result.DoesNotExist:
            sum = int(num1)-int(num2)
            save_sum = result(operation="sub",num1=num1,num2=num2,result=sum)
            save_sum.save()
            resp = requests.get(f'https://jsonplaceholder.typicode.com/todos/1')
            return HttpResponse(resp)
            return HttpResponse(sum)
        serialize = serializeResult(obj)
        resp = requests.get(f'https://jsonplaceholder.typicode.com/todos/1')
        #return response.Response(serialize.data['result'])
        return HttpResponse(resp)
    def put(self,request):
        num1 = request.data.get('num1',"")
        num2 = request.data.get('num2',"")
        if(num1 == "" or num2 == ""):
            return HttpResponse("Please enter both entries")
        try:
            obj = result.objects.get(operation="mul",num1=num1,num2=num2)
        except result.DoesNotExist:
            sum = int(num1)*int(num2)
            save_sum = result(operation="mul",num1=num1,num2=num2,result=sum)
            save_sum.save()
            return HttpResponse(sum)
        serialize = serializeResult(obj)
        return response.Response(serialize.data['result'])
    def delete(self,request):
        num1 = request.data.get('num1',"")
        num2 = request.data.get('num2',"")
        if(num1 == "" or num2 == ""):
            return HttpResponse("Please enter both entries")
        if(int(num2) == 0):
            return HttpResponse("Zero Division Error")
        try:
            obj = result.objects.get(operation="div",num1=num1,num2=num2)
        except result.DoesNotExist:
            sum = int(num1)/int(num2)
            save_sum = result(operation="div",num1=num1,num2=num2,result=sum)
            save_sum.save()
            return HttpResponse(sum)
        serialize = serializeResult(obj)
        return response.Response(serialize.data['result'])


class Register(APIView):
    def post(self,request):
        # serializer = RegiseterSerial(data=request.data)
        # serializer.is_valid(raise_exception=True)
        username = request.data.get("username","")
        password = request.data.get("password","")
        password = make_password(password)
        email = request.data.get("email","")
        find_user = User.objects.filter(username=username)
        find_email = User.objects.filter(email=email)
        if(find_user or find_email):
            return HttpResponse("Username or email already taken",status=400)
        else:
            try:
                reg = User(username=username,password=password,email=email)
                reg.save()
            except:
                pass
            return HttpResponse("Registeration Successful",status=201)


class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerial(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # django_login(request,user)
        logger.error("User tried logging in")
        token, created = Token.objects.get_or_create(user=user)
        return response.Response({"token":token.key},status=200)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        # django_logout(request)
        logger.error("User is logged out")
        return response.Response("Logout Successful")


