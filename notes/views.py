from django.shortcuts import render
from . models import Notes

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/list.html', {'notes': notes})
