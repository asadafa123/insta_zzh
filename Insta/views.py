from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
class helloworld(TemplateView):
    template_name = 'test.html'