
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from bankapp.models import Detail


def index(request):
    return render(request,'index.html')

def Welcome(request):
    return render(request,'wel.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('add')
        else:
            messages.info(request,'invalid password')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['Password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,
                                      email=email)

                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('login')

def add(request):
        if request.method == "POST":
            name = request.POST.get('name')
            address = request.POST.get('address')
            date = request.POST.get('date')
            age = request.POST.get('age')
            phone_num= request.POST.get('phone_num')
            email = request.POST.get('email')
            detail = Detail(name=name, address=address, date=date, age=age,phone_num=phone_num,email=email)
            detail.save()
            return redirect('Welcome')

        return render(request, 'add.html')


