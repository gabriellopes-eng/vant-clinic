from django.urls import path

from .views import (
    ServicoEsteticoCreateView,
    ServicoEsteticoDeleteView,
    ServicoEsteticoListView,
    ServicoEsteticoUpdateView,
)

app_name = "servicos"

urlpatterns = [
    path("", ServicoEsteticoListView.as_view(), name="servico_list"),
    path("novo/", ServicoEsteticoCreateView.as_view(), name="servico_create"),
    path("<int:pk>/editar/", ServicoEsteticoUpdateView.as_view(), name="servico_update"),
    path("<int:pk>/excluir/", ServicoEsteticoDeleteView.as_view(), name="servico_delete"),
]
