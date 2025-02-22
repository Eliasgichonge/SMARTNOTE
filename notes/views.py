from django.shortcuts import render
from . models import Note

def list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/list.html', {'notes': all_notes})