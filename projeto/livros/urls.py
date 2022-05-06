from . import views
from django.urls import path

app_name = 'livros'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('lista', views.lista, name = 'lista'),
    path('<int:item_id>', views.detail, name='detail'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listac', views.ListaC.as_view(), name='listac'),
    path('relatorio', views.relatorio, name = 'relatorio'),
    path('html', views.html, name = 'html'),
] 