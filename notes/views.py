from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import DetailView, ListView


class NotesListView(ListView):
      model = Notes
      context_object_name = "notes"
      template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
      model = Notes
      context_object_name = "note"
      template_name = 'notes/notes_detail.html'

