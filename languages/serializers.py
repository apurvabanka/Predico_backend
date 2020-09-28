from rest_framework import serializers
from .models import language

class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = language
        fields = ['id','name','paradign']