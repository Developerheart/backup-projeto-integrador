from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index():
    context = {}
    template = loader.get_template('app/cadastrar-usuario.html')
    return HttpResponse(template.render(context, request))
