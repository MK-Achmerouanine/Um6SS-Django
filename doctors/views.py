from django.http import HttpResponse
from django.shortcuts import render
from .models import Doctor

def index(request):
    context = {
        "doctors": Doctor.objects.all()
    }
    return render(request,'index.html',context)
def home(request):
    context = {
        "doctors": Doctor.objects.all()
    }
    return render(request,'home.html',context)