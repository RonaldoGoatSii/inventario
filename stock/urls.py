from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_artigo, name='criar_artigo'),
    path('editar/<int:artigo_id>/', views.editar_artigo, name='editar_artigo'),
    path('eliminar/<int:artigo_id>/', views.eliminar_artigo, name='eliminar_artigo'),
    path('', views.lista_artigos, name='lista_artigos'), #sempre que quiser adicionar um caminhos, tenho de inserir aqui, como, quando estou na página eliminar, e clico no botão de voltar, vou querer que este vá para a pagina inicial
]
