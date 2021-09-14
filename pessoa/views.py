from django.db import models
from django.shortcuts import render

#Importa classe da view nativa do Django
from django.views.generic import ListView

# Importa a model para fazer a listagem em ListaPessoaView
from .models import Pessoa

# Create your views here.
class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')