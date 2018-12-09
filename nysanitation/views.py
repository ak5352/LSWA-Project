from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')


def Dashboard(request):
    return render(request, 'Dashboard/index.html')


def Filter(request):
    return render(request, 'Filter/index.html')


def Login(request):
    email = request.GET.get('email', '');
    passw = request.GET.get('pass', '');
    if (email != "" and passw != ""):
        usern = User.objects.get(email=email.lower()).username
        user = authenticate(username=usern, password=passw)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')
    return render(request, 'Login/index.html')


def Register(request):
    user = request.GET.get('name', '');
    email = request.GET.get('email', '');
    passw = request.GET.get('pass', '');
    if (user != "" and passw != "" and email != ""):
        user = User.objects.create_user(user, email, passw)
        user.save()
        user = authenticate(username=user, password=passw)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')
    return render(request, 'Register/index.html')


def Search(request):
    return render(request, 'Search/index.html')
