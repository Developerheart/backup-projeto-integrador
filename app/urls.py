from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('app/anuncios', AnunciosView.as_view(), name='anuncios'),
    path('app/publicacoes', PublicacoesView.as_view(), name='publicacoes'),
    path('app/inserir-anuncio', InserirAnuncioView.as_view(), name='inserir-anuncio'),
    path('app/sobre-nos', SobreNosView.as_view(), name='sobre-nos'),
    path('app/termos-de-uso', TermosUsoView.as_view(), name='termos'),
    path('app/central-de-ajuda', AjudaView.as_view(), name='ajuda'),
    path('app/entre-em-contato', ContatoView.as_view(), name='contato'),
]