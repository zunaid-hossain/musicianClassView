from django.shortcuts import render,redirect
from Album.models import Album
from musician.models import musician
from django.views.generic import ListView


class HomeListView(ListView):
    model = Album 
    template_name = 'home.html'  
    context_object_name = 'data' 