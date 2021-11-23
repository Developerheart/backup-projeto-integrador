from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.


class Pessoa(models.Model):
    comercial = "C"
    fixo = "F"
    pessoal = "P"
    TIPO_CHOICES = [
        (comercial, "Comercial"),
        (fixo, "Fixo"),
        (pessoal, "Pessoal")
    ]
    nome = models.CharField(max_length=200, verbose_name='Nome Pessoa')
    email = models.EmailField(max_length=200, verbose_name='E-mail')
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES,
                            default=pessoal, verbose_name='Tipo de telefone')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    numero = models.IntegerField(null=True, blank=False, verbose_name='Número')
    rua = models.CharField(max_length=200, null=True,
                           blank=False, verbose_name='Rua')
    complemento = models.CharField(
        max_length=200, null=True, blank=False, verbose_name='Complemento')
    bairro = models.CharField(max_length=50, null=True,
                              blank=False, verbose_name='Bairro')
    cidade = models.CharField(
        max_length=100, null=True, blank=False, verbose_name='Cidade')
    estado = models.CharField(max_length=50, null=True,
                              blank=False, verbose_name='Estado')

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class PessoaJuridica(Pessoa):
    razao_social = models.CharField(
        max_length=200, verbose_name='Razão Social')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')

    class meta:
        ordering = ['razao_social']


class PessoaFisica(Pessoa):
    sobre = models.CharField(max_length=200, verbose_name='Sobrenome')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')

    class meta:
        ordering = ['razao_social']
