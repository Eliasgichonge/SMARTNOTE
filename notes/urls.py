from django.urls import path
from . import views


urlspatterns = [
    path('notes/', views.list),
]