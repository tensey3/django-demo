from django.shortcuts import render

#from django.views import generic
from django.views.generic.base import TemplateView

class TopView(TemplateView):
    template_name = 'top.html'