from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UsuarioForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


class IndexView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class SobreNosView(TemplateView):
    template_name = "app/sobre-nos.html"

    def get_context_data(self, **kwargs):
        context = super(SobreNosView, self).get_context_data(**kwargs)
        return context


class TermosUsoView(TemplateView):
    template_name = "app/termos-de-uso.html"

    def get_context_data(self, **kwargs):
        context = super(TermosUsoView, self).get_context_data(**kwargs)
        return context


class AjudaView(TemplateView):
    template_name = "app/central-de-ajuda.html"

    def get_context_data(self, **kwargs):
        context = super(AjudaView, self).get_context_data(**kwargs)
        return context


class ContatoView(TemplateView):
    template_name = "app/entre-em-contato.html"

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
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


def registro_usuario(request):
    if request.method == "POST":
        form_registro = UsuarioForm(request.POST)
        if form_registro.is_valid():
            usuario = form_registro.save()
            login(request, usuario)
            messages.success(request, "Cadastro realizado com sucesso.")
        # return redirect("main:homepage")
        messages.error(request, "Cadastro não realizado. Informações incorretas.")
    form_registro = UsuarioForm()
    return render(request=request, template_name="app/registro.html", context={"form_registro": form_registro})


def login_usuario(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"Você está logado como {username}.")
        else:
            messages.error(request, "Senha ou Usuário incorretos.")

    form_login = AuthenticationForm()
    return render(request=request, template_name="app/login.html", context={"form_login": form_login})


def logout_usuario(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    # return redirect("main:homepage")
