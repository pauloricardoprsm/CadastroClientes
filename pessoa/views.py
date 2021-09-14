from django.db import models
from django.shortcuts import render

#Importa classe da view nativa do Django
# Classe de Listagem
from django.views.generic import ListView
# Classe de Criação
from django.views.generic import CreateView
# Classe de Edição
from django.views.generic import UpdateView
# Classe de Exclusão
from django.views.generic import DeleteView


# Importa a model para fazer a listagem em ListaPessoaView
from .models import Pessoa


# Passa o form que foi criados
from .forms import PessoaForm


from django.http import HttpResponse, Http404

# Create your views here.
class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')

    #Cria filtro
    def get_queryset(self):
        """
        Se o usuario digitar algum valor no campo input e pressionar ok

        1 É feito uma requisição para URL
        2 A requisição cai em get_queryset
        3 em GET veririca se existe resultado com o parametro buscar_p_nome
        3.1 se não tiver retorna nulo
        4 Se tiver ele pega o resultado e aplica um filtro
        """
        # 2
        queryset =  super().get_queryset()
        # 3
        filtro_nome = self.request.GET.get('buscar_p_nome') or None

        #4
        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)


        return queryset


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'


class PessoaUpdateView(UpdateView): 
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'


def contatos(request, pk):
    try:
        contatos = Contato.objects.get(pessoa=pk)
    except Contato.doesNotExist:
        raise Http404
    return render(request,'contato/contato_list.html', {'contatos': contatos, 'pk_pessoa': pk_pessoa})
