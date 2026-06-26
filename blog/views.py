from django.shortcuts import render
from django.views import generic

class Index (generic.TemplateView):
    template_name = 'blog/index.html'
