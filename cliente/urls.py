from django.urls import path

from .views import PessoaFisicaCreate, PessoaFisicaDelete, PessoaFisicaListagemListView, PessoaFisicaUpdate
from .views import PessoaJuridicaCreate, PessoaJuridicaUpdate,PessoaJuridcaDelete, PessoaJuridicaListagemListView

urlpatterns = [
    path('cadastrar/pessoa-fisica/', PessoaFisicaCreate.as_view(), name='pessoa-fisica-cadastro'),
    path('atualizar/pessoa-fisica/<int:pk>/', PessoaFisicaUpdate.as_view(), name='pessoa-fisica-atualizar'),
    path('deletar/pessoa-fisica/<int:pk>/', PessoaFisicaDelete.as_view(), name='pessoa-fisica-deletar'),
    path('listagem/pessoa-fisica/', PessoaFisicaListagemListView.as_view(), name='pessoa-fisica-listagem'),

    path('cadastrar/pessoa-juridica/', PessoaJuridicaCreate.as_view(), name='pessoa-juridica-cadastro'),
    path('atualizar/pessoa-juridica/<int:pk>/', PessoaJuridicaUpdate.as_view(), name='pessoa-juridica-atualizar'),
    path('deletar/pessoa-juridica/<int:pk>/', PessoaJuridcaDelete.as_view(), name='pessoa-juridica-deletar'),
    path('listagem/pessoa-juridica/', PessoaJuridicaListagemListView.as_view(), name='pessoa-juridica-listagem')
    
]