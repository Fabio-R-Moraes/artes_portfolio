from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='photos-home'),
    path('photo/<int:id>/', views.photo, name='photos-photo'),
]