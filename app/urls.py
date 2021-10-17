from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('app/anuncios', AnunciosView.as_view(), name='anuncios'),
    path('app/publicacoes', PublicacoesView.as_view(), name='publicacoes'),
     path('app/inserir-anuncio', InserirAnuncioView.as_view(), name='inserir-anuncio'),
]