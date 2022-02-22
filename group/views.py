from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def group(request):
    return HttpResponse("group called...")

def index(request):
    context ={
        'name':'FLIPKART',
    }
    return render(request,'group/index.html',context)

def contactus(request):
    context ={
        'contact_name':["dhiraj","priya","riya"],
    }
    return render(request, 'group/contactus.html',context)

def aboutus(request):
    context = {
        'isActive':True,
        'age':20
    }
    return render(request, 'group/aboutus.html',context)
