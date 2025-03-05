from django.shortcuts import render
from django.http import Http404
from .models import Notes
from .forms import NotesForm
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class NotesDeleteView(DeleteView):
      model = Notes
      success_url = '/smart/notes'
      template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
      model = Notes
      form_class = NotesForm
      success_url = '/smart/notes'


class NotesCreateView(CreateView):
      model = Notes
      form_class = NotesForm
      success_url = '/smart/notes'


class NotesListView(LoginRequiredMixin, ListView):
      model = Notes
      context_object_name = "notes"
      template_name = "notes/notes_list.html"
      login_url = "/admin"


class NotesDetailView(DetailView):
      model = Notes
      context_object_name = "note"
      template_name = 'notes/notes_detail.html'

