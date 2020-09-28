from django.shortcuts import render
from rest_framework import status, response
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView

# Create your views here.

#Get list of Items
class Predictions(APIView):
    def get(self,request):
        items = [
            'Item 1',
            'Item 2',
            'Item 3',
            'Item 4',
        ]
        print(items)
        return JsonResponse(items, safe=False)

    def post(self,request):
        Items= {
            "Item 1":{
                "2020/5/23":50,
                "2020/5/24":55,
                "2020/5/25":60,

            },
            "Item 2":{
                "2020/5/23":50,
                "2020/5/24":55,
                "2020/5/25":60,

            },
            "Item 3":{
                "2020/5/23":50,
                "2020/5/24":55,
                "2020/5/25":60,

            },
            "Item 4":{
                "2020/5/23":50,
                "2020/5/24":55,
                "2020/5/25":60,

            },
        }
        item = request.data.get("item",None)
        date = request.data.get("date",None)
        print(item,date)
        try: 
            a=Items[item][date]
        except KeyError:
            a='0'
        return HttpResponse(a)



