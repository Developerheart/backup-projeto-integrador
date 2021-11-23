from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PessoaFisica, PessoaJuridica


class PessoaFisicaCreate(CreateView):
    model = PessoaFisica
    fields= ['nome','sobre','cpf','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'clientes/formcliente.html'
    success_url = reverse_lazy('pessoa-fisica-listagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Física"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar']='cadastrar'

        return context



class PessoaFisicaUpdate(UpdateView):
     model = PessoaFisica
     fields= ['nome','cpf','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
     template_name = 'clientes/formcliente.html'
     success_url = reverse_lazy('pessoa-fisica-listagem')

     def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Atualizar Cliente Pessoa Física"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Atualizar'

        return context



class PessoaFisicaDelete(DeleteView):
    model = PessoaFisica
    template_name = 'clientes/delete.html'
    success_url = reverse_lazy('pessoa-fisica-listagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Pessoa Fisica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['icon2'] = '<i class = "fa fa-reply" aria-hidden = "true" > </i >'
        context['botao'] = 'Excluir'

        return context




class PessoaFisicaListagemListView(ListView):
    model = PessoaFisica
    template_name = 'clientes/list-cliente.html'


#=================================== PESSSOA JURIDICA ===================================



class PessoaJuridicaCreate(CreateView):
    model = PessoaJuridica
    fields= ['nome','razao_social','cnpj','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'clientes/formcliente.html'
    success_url = reverse_lazy('pessoa-juridica-listagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Juridica"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar']='cadastrar'

        return context



class PessoaJuridicaUpdate(UpdateView):
     model = PessoaJuridica
     fields= ['nome','razao_social','cnpj','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
     template_name = 'clientes/formcliente.html'
     success_url = reverse_lazy('pessoa-juridica-listagem')

     def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Atualizar Cliente Pessoa Juridica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Atualizar'

        return context



class PessoaJuridcaDelete(DeleteView):
    model = PessoaJuridica
    template_name = 'clientes/delete.html'
    success_url = reverse_lazy('pessoa-juridica-listagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Pessoa Juridica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['icon2'] = '<i class = "fa fa-reply" aria-hidden = "true" > </i >'
        context['botao'] = 'Excluir'

        return context





class PessoaJuridicaListagemListView(ListView):
    model = PessoaJuridica
    template_name = 'clientes/list-clientejuridico.html'

