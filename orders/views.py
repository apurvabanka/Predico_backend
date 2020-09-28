from django.shortcuts import render
from rest_framework import status, response
from rest_framework.views import APIView
from orders.models import OrderDetails,centerRestaurantMapping
from orders.serializers import serializeCenters
from django.db import IntegrityError
import redis

r = redis.Redis()

# Create your views here.

class Order(APIView):
    def post(self,request):
        customer_id = request.data.get('customer_id',None)
        customer_name = request.data.get('customer_name',None)
        restaurant_id = request.data.get('restaurant_id',None)
        #restaurant_name = request.data.get('restaurant_name',None)
        center_id = request.data.get('center_id',None)
        location = request.data.get('location',None)
        item_name = request.data.get('item_name',None)
        product_price = request.data.get('product_price',None)
        longitude = request.data.get('longitude',None)
        latitude = request.data.get('latitude',None)
        status = r.get(center_id).decode('utf-8')
        print("status = ",status)
        if(status == '1'):
            try:
                obj = OrderDetails(customer_id=customer_id,customer_name=customer_name,restaurant_id=restaurant_id,
                center_id=center_id,item_name=item_name,product_price=product_price,
                longitude=longitude,latitude=latitude)
                obj.save()
            except IntegrityError as e:
                return response(str(e))
            print("Order Placed")
            return response.Response({"message":"Success","Order placed from":location})
        else:
            try:
                obj = centerRestaurantMapping.objects.filter(restaurant_id=restaurant_id)
            except centerRestaurantMapping.DoesNotExist:
                pass
            #serialized_data = serializeCenters(obj)
            center_id = obj[1].center_id
            status = r.get(center_id).decode('utf-8')
            location = obj[1].location
            if(status == '1'):
                try:
                    obj = OrderDetails(customer_id=customer_id,customer_name=customer_name,restaurant_id=restaurant_id,
                    center_id=center_id,item_name=item_name,product_price=product_price,
                    longitude=longitude,latitude=latitude)
                    obj.save()
                except IntegrityError as e:
                    return response(str(e))
                return response.Response({"message":"Success","Order placed from":location})
            else:
                return response.Response({'message':'Order cannot be placed'})