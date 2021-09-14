from django.db import models

# Create your models here.
class Pessoa(models.Model):
    """
    Define os campos do banco de dados
    null=True, blank=True faz aceitar campos vazios 
    """

    nome_completo = models.CharField(max_length=256, null=True, blank=True)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome_completo
    

class Contato(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome