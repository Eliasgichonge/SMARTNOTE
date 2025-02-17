from typing import List
from django.shortcuts import render
from django.http import Http404
from notes.models import Note
from django.views.generic import DetailView, ListView


class NoteListView(ListView):
      model = Note
      template_name = 'notes/note_list.html'
      context_object_name = 'notes'


class NoteDetailView(DetailView):
      model = Note
      template_name = 'notes/note_detail.html'
      context_object_name = 'note'

def detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/note_detail.html', {'note': note})
