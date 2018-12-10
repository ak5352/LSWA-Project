from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import resturant, Profile
from django.db.models.query import QuerySet
from pprint import PrettyPrinter
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import get_object_or_404

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


@login_required(login_url='/Login/')
def Dashboard(request):
    if request.method == 'POST':
        r_id = request.POST["r_id"]
        rest = resturant.objects.filter(pk=r_id).update(count = F('count')+1)
        user = request.user
        user.profile.restaurants_list.append(r_id)
        user.save()

    user_rests = user.profile.restaurants_list
    rest = resturant.objects.filter(id__in=user_rests)
    return render(request, 'Dashboard/index.html', {'results': rest})


def Filter(request):
    cuisine = request.GET.get('cuisine', '');
    borough = request.GET.get('borough', '');
    score = request.GET.get('score', '');
    if cuisine != '' and borough != '' and score != '':
        print("HERE")
        kwargs = {}
        if cuisine != 'no-preference':
            kwargs["cuisine"]=cuisine.capitalize()
        if borough != 'no-preference':
            kwargs["borough"]=borough
        if score != 'no-preference':
            kwargs["score"]=int(score)

        rest = resturant.objects.filter(**kwargs)
        return render(request, 'Filter/index.html', {'results': rest})
    return render(request, 'Filter/index.html')


def Login(request):
    email = request.POST.get('email', '');
    passw = request.POST.get('pass', '');
    user = None
    if (email != "" and passw != ""):
        try:
            usern = get_object_or_404(User, email=email.lower())
        except:
            return render(request, 'Login/index.html', {'failed': True})
        user = authenticate(username=usern.name, password=passw)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')
    return render(request, 'Login/index.html')


def Register(request):
    user = request.POST.get('name', '');
    email = request.POST.get('email', '');
    passw = request.POST.get('pass', '');
    if (user != "" and passw != "" and email != ""):
        try:
            user = User.objects.create_user(user, email, passw)
            user.save()
        except:
            return render(request, 'Register/index.html', {'failed': True})
        user = authenticate(username=user, password=passw)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')
    return render(request, 'Register/index.html')


def Search(request):
    return render(request, 'Search/index.html')
