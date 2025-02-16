from django.shortcuts import render
from django.http import HttpResponse
from  datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class HomeView(TemplateView):
      template_name = 'home/welcome.html'
      extra_context = {'today': datetime.today()}


class AuthorizedView(TemplateView):
      template_name = 'home/authorized.html'

@login_required(login_url='/admin/')
def authorized(request):
    return render(request, 'home/authorized.html', {})
