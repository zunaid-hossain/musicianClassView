
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.musicianRegistrationView.as_view() ,name='musician'),
    path('edit/<int:id>/', views.MusicianUpdateView.as_view(), name='edit_musician'),
    path('register',views.userRegistrationView.as_view(),name='Register'),
    path('login',views.UserLoginView.as_view(),name='login'),
    path('logout',views.User_Logout,name='logout')
    

]
