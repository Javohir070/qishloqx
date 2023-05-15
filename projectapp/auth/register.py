from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from projectapp.models import Province,Pump,SubProvince,User
from projectapp.forms import PumpForm
from django.http import JsonResponse


def register(request):
    return render (request,'auth/reg.html')
    