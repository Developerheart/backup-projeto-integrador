from django.db import models
from django.forms.forms import Form
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Material

from django.urls import reverse_lazy

# Create your views here.


class MaterialCreate (CreateView):
    model = Material
    fields = ['descricao','imagem','categoria', 'detalhes', 'peso', 'usuario']
    template_name = 'material/form.html'
    success_url = reverse_lazy('listar-material')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro de material'
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = 'Cadastrar'

        context['icon2'] = '<i class="fa fa-reply" aria-hidden="true"></i>'

        return context


class MaterialUpdate(UpdateView):
    model = Material
    fields = ['descricao','imagem' ,'categoria', 'detalhes', 'peso', 'usuario']
    template_name = 'material/form-upload.html'
    success_url = reverse_lazy('listar-material')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Atualizar Material"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['icon2'] = '<i class = "fa fa-reply" aria-hidden = "true" > </i >'
        context['botao'] = 'Atualizar'

        return context


class MaterialDelete(DeleteView):
    model = Material
    template_name = 'material/form-delete.html'
    success_url = reverse_lazy('listar-material')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Material"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['icon2'] = '<i class = "fa fa-reply" aria-hidden = "true" > </i >'
        context['botao'] = 'Excluir'

        return context


class MaterialList(ListView):
    model = Material
    template_name = 'material/list/list-material.html'
