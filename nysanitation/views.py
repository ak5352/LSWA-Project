from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import resturant, Profile
from django.db.models.query import QuerySet
from pprint import PrettyPrinter

def dprint(object, stream=None, indent=1, width=80, depth=None):
    """
    A small addition to pprint that converts any Django model objects to dictionaries so they print prettier.

    h3. Example usage

        >>> from toolbox.dprint import dprint
        >>> from app.models import Dummy
        >>> dprint(Dummy.objects.all().latest())
         {'first_name': u'Ben',
          'last_name': u'Welsh',
          'city': u'Los Angeles',
          'slug': u'ben-welsh',
    """
    # Catch any singleton Django model object that might get passed in
    if getattr(object, '__metaclass__', None):
        if object.__metaclass__.__name__ == 'ModelBase':
            # Convert it to a dictionary
            object = object.__dict__

    # Catch any Django QuerySets that might get passed in
    elif isinstance(object, QuerySet):
        # Convert it to a list of dictionaries
        object = [i.__dict__ for i in object]

    # Pass everything through pprint in the typical way
    printer = PrettyPrinter(stream=stream, indent=indent, width=width, depth=depth)
    printer.pprint(object)

def index(request):
    return render(request, 'index.html')


def Dashboard(request):
    return render(request, 'Dashboard/index.html')


def Filter(request):
    cuisine = request.GET.get('cuisine', '');
    borough = request.GET.get('borough', '');
    score = request.GET.get('score', '');
    rest = 0
    if (cuisine != '' and borough != '' and score != ''):
        if (cuisine != 'no-preference' and borough != 'no-preference' and score != 'no-preference'):
            rest = resturant.objects.filter(cuisine=cuisine.capitalize()).filter(borough=borough)
            return render(request, 'Filter/index.html', {'results': rest})
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
