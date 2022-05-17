from django import http
from django.shortcuts import render , redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from numpy import source
from .models import User_details,Post
#from newsapi import NewsApiClient
#from .serializers import PostSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import smtplib
import random
import email.message

# Create your views here.
def login(request):
    if request.method=='POST':
        pass1=request.POST['password']
        email=request.POST['email']
        if User_details.objects.filter(email=email).exists():
            obj1=User_details.objects.get(email=email)
            if obj1.password==pass1:
                request.session['blog_user']=obj1.id
                return redirect('home')
            else:
                messages.info(request,'Wrong Password')
                return redirect('login')
        else:
            messages.info(request,'wrong email entered')


    else:
        return render(request,'login.html')
# Create your views here.


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        
        if User_details.objects.filter(username=username).exists():
            messages.info(request,'Username Already taken')
            print('username taken')
            return redirect('register')
        if User_details.objects.filter(email=email).exists():
            messages.info(request,'Email Already Taken')
            return redirect('register')
        if pass1!=pass2:
            messages.info(request,'Password not matching!!')
            return redirect('register')
        Lower=False
        Upper=False
        num=False
        
        if (pass1==pass2 and len(pass1)>=8):
            for i in pass1:
                if ord(i)>=65 and ord(i)<=91:
                    Upper=True
                    break
            for i in pass1:
                if ord(i)>=97 and ord(i)<=123:
                    Lower=True
                    break
            for i in pass1:
               # print(ord(i))
                if (ord(i)<65 or ord(i)>91) :
                    if (ord(i)<97 or ord(i)>123):
                        
                        num=True
                        break  
            
            #print(num,Upper,Lower)
            if (Lower is True and Upper is True and num is True):
                print(num)
                obj1=User_details()
                obj1.username=username
                obj1.email=email
                obj1.password=pass1
                obj1.save()
                return redirect('login')
            else:
                messages.info(request,'please check validation of your password')
                return redirect('register')
        else:
            messages.info(request,'Password must be atleast 8 character long')
            return redirect('register')


    else:
        return render(request,'register.html')