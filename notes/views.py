from typing import List
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from . models import Notes


class NotesListView(ListView):
      model = Notes
      context_objects_name = "notes"
      template_name = "notes/notes_list.html"


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})