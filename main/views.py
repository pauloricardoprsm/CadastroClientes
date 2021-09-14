from django.shortcuts import render

# Create your views here.
# A view é responsavel por renderizar o html é onde fica as funçoes
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'main/index.html'