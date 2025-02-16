from django.shortcuts import render
from django.http import Http404

from notes.models import Note


def list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
