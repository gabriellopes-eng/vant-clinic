from django.urls import path

from .views import (
    AgendamentoCancelarView,
    AgendamentoCreateView,
    AgendamentoListView,
    AgendamentoUpdateView,
)

app_name = "agendamentos"

urlpatterns = [
    path("", AgendamentoListView.as_view(), name="agendamento_list"),
    path("novo/", AgendamentoCreateView.as_view(), name="agendamento_create"),
    path("<int:pk>/editar/", AgendamentoUpdateView.as_view(), name="agendamento_update"),
    path("<int:pk>/cancelar/", AgendamentoCancelarView.as_view(), name="agendamento_cancelar"),
]
