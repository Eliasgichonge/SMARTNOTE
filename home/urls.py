from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView),
    path('authorized', views.authorized)
]