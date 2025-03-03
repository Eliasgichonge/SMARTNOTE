from django.urls import path
from . import views


urlpatterns = [
    path('', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
]