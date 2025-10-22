from django.shortcuts import render

#from django.views import generic
from django.views.generic.base import TemplateView

class StartView(TemplateView):
    template_name = 'start.html'