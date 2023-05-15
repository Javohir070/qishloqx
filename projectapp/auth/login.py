from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from projectapp.models import Province,Pump,SubProvince,User
from projectapp.forms import PumpForm
from django.http import JsonResponse






def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        user = User.objects.filter(username=username).first()
        if not user:
             return render(request,'auth/login.html',{'error':"Siz kiritgan User bazada yoq"})
        login(request,user)
        return redirect('index')
        
    return render(request,'auth/login.html')

