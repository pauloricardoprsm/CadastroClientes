from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    #Coloca o nome do field que se quer editar
    data_nascimento = forms.DateField(
        #Passa o componente como tex input
        widget=forms.TextInput(
            #o campo attrs forcene o atributo que podemos enviar, como fariamos no html
            attrs={'type':'date'}
        )
    )
    class Meta:
        model = Pessoa
        fields = [
            'nome_completo', 
            'data_nascimento', 
            'ativa'
            # Também pode ser passado '(__all__) para passar todos os parametros            
        ]
