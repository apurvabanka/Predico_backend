from django.shortcuts import render
from rest_framework import status, response
from django.http import HttpResponse,JsonResponse
from rest_framework import response
from rest_framework.views import APIView
import redis
from django.shortcuts import redirect
from dataCluster.tasks import add


r=redis.Redis()

# Create your views here.


class cluster(APIView):
    def get(self,request):
        first_lat = r.get("first_lat").decode('utf-8')
        first_lon = r.get("first_lon").decode('utf-8')
        second_lat = r.get("second_lat").decode('utf-8')
        second_lon = r.get("second_lon").decode('utf-8')
        third_lat = r.get("third_lat").decode('utf-8')
        third_lon = r.get("third_lon").decode('utf-8')
        coordinates = {
            "first_lat":first_lat,
            "first_lon":first_lon,
            "second_lat":second_lat,
            "second_lon":second_lon,
            "third_lat":third_lat,
            "third_lon":third_lon
            }
        #url = redirect("https://app.periscopedata.com/shared/8d691615-2fb6-4fc8-9927-a94e35a29492?")
        #url = "good"
        #add.delay(4,5)
        print(coordinates)
        return JsonResponse(coordinates) 
