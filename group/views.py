from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def group(request):
    return HttpResponse("group called...")

def index(request):
    return render(request,'group/index.html')

def contactus(request):
    return render(request, 'group/contactus.html')

def aboutus(request):
    return render(request, 'group/aboutus.html')
