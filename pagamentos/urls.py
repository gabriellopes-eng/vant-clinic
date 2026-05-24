from django.urls import path

from .views import (
    PagamentoCreateView,
    PagamentoDeleteView,
    PagamentoListView,
    PagamentoUpdateView,
)

app_name = "pagamentos"

urlpatterns = [
    path("", PagamentoListView.as_view(), name="pagamento_list"),
    path("novo/", PagamentoCreateView.as_view(), name="pagamento_create"),
    path("<int:pk>/editar/", PagamentoUpdateView.as_view(), name="pagamento_update"),
    path("<int:pk>/excluir/", PagamentoDeleteView.as_view(), name="pagamento_delete"),
]
