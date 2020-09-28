from rest_framework import serializers, exceptions
from .models import centerRestaurantMapping

class serializeCenters(serializers.ModelSerializer):
    class Meta:
        model =  centerRestaurantMapping
        fields = ['center_id','restaurant_id','location']