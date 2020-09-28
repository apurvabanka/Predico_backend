from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import language
from .serializers import LanguageSerializers

class LangView(viewsets.ModelViewSet):
    queryset = language.objects.all()
    serializer_class = LanguageSerializers


# Create your views here.
