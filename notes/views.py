from django.shortcuts import render
from .models import Note

def list(request):  # Renamed function from "list" to "notes_list"
    all_notes = Note.objects.all()  # Get all notes from the database
    return render(request, 'notes/notes_list.html', {'notes': all_notes})