from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "app/index.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
    

class AnunciosView(TemplateView):
    template_name = "app/anuncios.html"
    

    def get_context_data(self, **kwargs):
        context = super(AnunciosView, self).get_context_data(**kwargs)
        return context
    

class PublicacoesView(TemplateView):
    template_name = "app/publicacoes.html"
    

    def get_context_data(self, **kwargs):
        context = super(PublicacoesView, self).get_context_data(**kwargs)
        return context
    

class InserirAnuncioView(TemplateView):
    template_name = "app/inserir-anuncio.html"

    
    def get_context_data(self, **kwargs):
        context = super(InserirAnuncioView, self).get_context_data(**kwargs)
        return context
    


