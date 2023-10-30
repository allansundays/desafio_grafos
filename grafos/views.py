from django.shortcuts import render
from .models import Conexao, Ator
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import AtorForm, ConexaoForm

def obter_dados_relacao(request):
    relacoes = Conexao.objects.all()
    dados_relacao = []
    for relacao in relacoes:

        dados_relacao.append({
            'nome_source': relacao.conexaoA.nome,
            'imagem_source': relacao.conexaoA.link_imagem,
            'descricao_source': relacao.conexaoA.descricao,
            'nome_target': relacao.conexaoB.nome,
            'imagem_target': relacao.conexaoB.link_imagem,
            'descricao_target': relacao.conexaoB.descricao,
        })

    return JsonResponse({'dados_relacao': dados_relacao})

def dashboard_page(request):
    return render(request, 'grafos/dashboards/dash_atualizavel.html')

def dashboard_page_fixo(request):
    return render(request, 'grafos/dashboards/dash_fixo.html')

def dashboard_page_fixo2(request):
    return render(request, 'grafos/dashboards/dash_fixo2.html')
    
def index(request):
    return render(request, 'grafos/index.html')

class ListaAtorView(ListView):
    template_name = "grafos/atores/lista.html"
    model = Ator
    context_object_name = "atores"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class CriaAtorView(CreateView):
    template_name = "grafos/atores/cria.html"
    model = Ator
    form_class = AtorForm
    success_url = reverse_lazy("lista_ator")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class AtualizaAtorView(UpdateView):
    template_name = "grafos/atores/atualiza.html"
    model = Ator
    fields = '__all__'
    context_object_name = 'ator'
    success_url = reverse_lazy("lista_ator")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class DeletaAtorView(DeleteView):
    template_name = "grafos/atores/exclui.html"
    model = Ator
    context_object_name = 'ator'
    success_url = reverse_lazy("lista_ator")

class HomeAtorView(TemplateView):
    template_name = "grafos/atores/index.html"






class ListaConexaoView(ListView):
    template_name = "grafos/conexoes/lista.html"
    model = Conexao
    context_object_name = "conexoes"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class CriaConexaoView(CreateView):
    template_name = "grafos/conexoes/cria.html"
    model = Conexao
    form_class = ConexaoForm
    success_url = reverse_lazy("lista_conexao")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class AtualizaConexaoView(UpdateView):
    template_name = "grafos/conexoes/atualiza.html"
    model = Conexao
    fields = '__all__'
    context_object_name = 'conexao'
    success_url = reverse_lazy("lista_conexao")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class DeletaConexaoView(DeleteView):
    template_name = "grafos/conexoes/exclui.html"
    model = Conexao
    context_object_name = 'conexao'
    success_url = reverse_lazy("lista_conexao")


class HomeAtorView(TemplateView):
    template_name = "grafos/conexoes/index.html"
