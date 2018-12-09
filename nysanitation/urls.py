from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('Filter/', views.Filter, name='Filter'),
    path('Login/', views.Login, name='Login'),
    path('Register/', views.Register, name='Register'),
    path('Search/', views.Search, name='Search'),
]
