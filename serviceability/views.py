from django.shortcuts import render
from rest_framework import status, response
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
import redis

r = redis.Redis()

# Create your views here.


class Service(APIView):
    def get(self,request):
        centerId  = request.GET.get("centerId",None)
        print(centerId)
        status = r.get(centerId).decode('utf-8')
        return HttpResponse(status)


    def post(self,request):
        centerId = request.data.get("centerId",None)
        status = request.data.get("status",None)
        r.mset({centerId:status})
        print({centerId:status})
        return HttpResponse("Status Set")