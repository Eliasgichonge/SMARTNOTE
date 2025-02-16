from django.shortcuts import render
from  . models import Note

def list(request):
    all_notes = Notes.objects.all()

