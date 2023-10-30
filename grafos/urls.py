from django.urls import path
from .views import obter_dados_relacao, dashboard_page, dashboard_page_fixo, dashboard_page_fixo2
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('dados_relacao/', obter_dados_relacao, name='dados_relacao'),

    path('dashboard/atualizavel', dashboard_page, name='dashboard_page'),

    path('dashboard/fixo', dashboard_page_fixo, name='dashboard_page1'),

    path('dashboard/fixo2', dashboard_page_fixo2, name='dashboard_page2'),

    ### Atores ###
    # GET/cargos/cadastrar
    path('atores/cadastrar', views.CriaAtorView.as_view(), name="cadastra_ator"),

    # GET/cargos
    path('atores/lista', views.ListaAtorView.as_view(), name="lista_ator"),

    # GET/POST/cargos/{pk}
    path('atores/<pk>', views.AtualizaAtorView.as_view(), name="atualiza_ator"),

    # GET/POST/cargos/excluir/{pk}
    path('atores/excluir/<pk>', views.DeletaAtorView.as_view(), name="deleta_ator"),


    ### Conexoes ###
    # GET/areas/cadastrar
    path('conexoes/cadastrar', views.CriaConexaoView.as_view(), name="cadastra_conexao"),

    # GET/areas
    path('conexoes/lista', views.ListaConexaoView.as_view(), name="lista_conexao"),

    # GET/POST/areas/{pk}
    path('conexoes/<pk>', views.AtualizaConexaoView.as_view(), name="atualiza_conexao"),

    # GET/POST/areas/excluir/{pk}
    path('conexoes/excluir/<pk>', views.DeletaConexaoView.as_view(), name="deleta_conexao"),


]