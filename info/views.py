from django.shortcuts import render
from rest_framework import status
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import LoginSerial
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,generics
from .models import user
from .serializers import infoSerializer,salarySerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

authentication_class = [TokenAuthentication]
permission_class = [IsAuthenticated]

# @api_view(['GET','POST'])
# def user_info(request):
#     if request.method == "GET":
#         obj = user.objects.all()
#         serializer = infoSerializer(obj,many=True)
#         return response.Response(serializer.data)
#     elif request.method == "POST":
#         # authentication_class = (TokenAuthentication)
#         serializer = infoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data,status=status.HTTP_201_CREATED)
#         return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class user_info(APIView):
    # authentication_classes = [TokenAuthentication]
    def get(self,request):
        obj = user.objects.all()
        serializer = infoSerializer(obj,many=True)
        return response.Response(serializer.data)
    def post(self,request):
        serializer = infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerial(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request,user)
        token , created = Token.objects.get_or_create(user=user)
        return response.Response({"token":token.key},status=200)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )
    def post(self, request):
        request.user.auth_token.delete()
        django_logout(request)
        return response.Response(status=204)

class employeeListView(generics.ListAPIView):
    serializer_class = salarySerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend,)
    flter_fields = ('username','email','info__designation',)


@api_view(['GET'])
def info_detail(request,pk):
    try:
        obj = User.objects.get(name=pk)
    except user.DoesNotExist:
        return response.Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = infoSerializer(obj)
    return response.Response(serializer.data)


