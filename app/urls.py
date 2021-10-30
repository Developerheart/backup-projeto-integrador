from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/cadastre-se/', views.registro_usuario, name="registro"),
    path('home/login/', views.login_usuario, name='login'),
    path('logout', views.logout_usuario, name= "logout"),

    path('anuncios/', AnunciosView.as_view(), name='anuncios'),
    path('publicacoes/', PublicacoesView.as_view(), name='publicacoes'),
    path('inserir-anuncio/', InserirAnuncioView.as_view(), name='inserir-anuncio'),
    path('sobre-nos/', SobreNosView.as_view(), name='sobre-nos'),
    path('termos-de-uso/', TermosUsoView.as_view(), name='termos'),
    path('central-de-ajuda/', AjudaView.as_view(), name='ajuda'),
    path('entre-em-contato/', ContatoView.as_view(), name='contato'),
]