from django.shortcuts import render,redirect
from .import forms 
from .models import Album
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.views.generic import FormView



@method_decorator(login_required(login_url='/musician/login'), name='dispatch')
class AlbumView(FormView):
   template_name="album.html"
   form_class =  forms.AlbumForm
   success_url = reverse_lazy('home')
   
   def form_valid(self,form):
      album = form.save(commit=False)
      album.save()
      return super().form_valid(form)






@method_decorator(login_required(login_url='/musician/login'), name='dispatch')
class YourModelDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('home') 
    template_name = 'delete.html'
    pk_url_kwarg = 'id'

 



@method_decorator(login_required(login_url='/musician/login'), name='dispatch')
class edit(UpdateView):
    model = Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'