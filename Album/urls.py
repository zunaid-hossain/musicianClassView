
from django.urls import path
from . import views

urlpatterns = [
    path('',views.AlbumView.as_view() ,name='album'),
    path('delete/<int:id>',views.YourModelDeleteView.as_view(),name='delete'),
    path('edit/<int:id>',views.edit.as_view(),name="edit")
    
]
