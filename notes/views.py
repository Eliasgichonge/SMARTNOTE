from django.shortcuts import render
from django.http import Http404

def list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes/notes_detail.html', {'note': note})
