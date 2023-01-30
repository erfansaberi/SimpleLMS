from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Homepage
class HomePageView(TemplateView):
    template_name = 'index.html'
