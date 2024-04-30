from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login,logout
from .forms import registerForm, musicianForm
from django.views.generic import FormView
from .models import musician
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here.


@method_decorator(login_required(login_url='/musician/login'), name='dispatch')
class musicianRegistrationView(FormView):
   template_name="musician.html"
   form_class =  musicianForm
   success_url = reverse_lazy('home')
   
   def form_valid(self,form):
      musician = form.save(commit=False)
      musician.save()
      return super().form_valid(form)



@method_decorator(login_required(login_url='/musician/login'), name='dispatch')
class MusicianUpdateView(UpdateView):
    model = musician
    form_class = musicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

class userRegistrationView(FormView):
   template_name="user.html"
   form_class = registerForm
   success_url = reverse_lazy('home')
   
   def form_valid(self,form):
      user = form.save()
      login(self.request, user)
      return super().form_valid(form)



class UserLoginView(LoginView):
   template_name = 'user.html'
   def get_success_url(self):
      return reverse_lazy('home')


login_required(login_url='/musician/login')
def User_Logout(request):
     logout(request)
     return redirect('home')
