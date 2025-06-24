from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="listar"),
    path("adicionar", views.adicionar, name="adicionar"),
    path("excluir/<str:pk>", views.excluir, name="excluir"),
    path("editar/<str:pk>", views.editar, name="editar"),
]
