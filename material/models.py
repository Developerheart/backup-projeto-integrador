from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django.utils import tree

# Create your models here.


class Categoria (models.Model):
    descricao = models.CharField(max_length=150, verbose_name='Descrição')

    def __str__(self):
        return "{}".format(self.descricao)



class Material(models.Model):
    imagem = models.ImageField(upload_to='produtos', null=True,blank=True)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    categoria = models.ForeignKey(Categoria, on_delete=PROTECT)
    detalhes = models.CharField(max_length=150)
    peso = models.DecimalField(decimal_places=1, max_digits=4)

    usuario = models.ForeignKey(User, on_delete=PROTECT)
    def __str__(self):
        return "Descrição:{} |Categoria: {} |Detalhes: {}|Peso: {} Kg ".format(self.descricao, self.categoria, self.detalhes, self.peso)
