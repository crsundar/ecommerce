from django.urls import path
from .import views 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('all/', views.all, name='products'),
]