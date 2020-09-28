from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(request):
    return HttpResponseRedirect('/other')

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1)+int(val2)
    return render(request,"result.html",{'result':res})

def other(request):
    return HttpResponse("This is the other page")