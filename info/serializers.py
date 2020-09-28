from rest_framework import serializers,exceptions
from .models import user
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['name','position']

class salarySerializer(serializers.ModelSerializer):
    info = infoSerializer()

    class Meta:
        model = User
        fields = ['username','email','info']

class LoginSerial(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        username = data.get("username","")
        password = data.get("password","")
        
        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "Account disabled"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provode username and password"
            raise exceptions.ValidationError(msg)
        return data