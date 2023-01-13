from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password = request.POST['pwd1']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')   #home page
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        user_name=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        if pwd1 == pwd2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"This user name is already taken")
                return redirect('register')
            elif  User.objects.filter(email=email).exists():
                    messages.info(request,"This email id is  already registered")
                    return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,first_name=fname,last_name=lname,email=email,password=pwd1)
                user.save()
                return redirect('login')
                print("A new user is created")
        else:
            messages.info(request, "password does nt match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')