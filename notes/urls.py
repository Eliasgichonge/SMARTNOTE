from django.urls import path
from . import views


urlpatterns = [
    path('notes', views.NotesListView),
    path('notes/<int:pk>', views.detail),
]