from django.urls import path

from .views import (
    ClienteCreateView,
    ClienteDeleteView,
    ClienteListView,
    ClienteUpdateView,
)

app_name = "clientes"

urlpatterns = [
    path("", ClienteListView.as_view(), name="cliente_list"),
    path("novo/", ClienteCreateView.as_view(), name="cliente_create"),
    path("<int:pk>/editar/", ClienteUpdateView.as_view(), name="cliente_update"),
    path("<int:pk>/excluir/", ClienteDeleteView.as_view(), name="cliente_delete"),
]
