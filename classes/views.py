from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
       
    return render(request, 'signup.html',)

def login(request):
    return render(request, 'login.html')

def notice(request):
    return render(request, 'notice.html')

def gallery(request):
    return render(request, 'gallery.html')

def enquiry(request):
    return render(request, 'enquiry.html')

