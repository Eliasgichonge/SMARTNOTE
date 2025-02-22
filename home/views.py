from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})

def authorized(request):
    return render(request, 'home/authorized.html', {})
