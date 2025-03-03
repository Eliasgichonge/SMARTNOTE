from django.urls import path
from . import views


urlpatterns = [
    path('', views.NotesListView.as_view(), name=""),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
]