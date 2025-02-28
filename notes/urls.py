from django.urls import path
from . import views


urlpatterns = [
    path('', views.list),
    path('notes/<int:pk>', views.detail),
]