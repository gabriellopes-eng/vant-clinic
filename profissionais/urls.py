from django.urls import path

from .views import (
    ProfissionalCreateView,
    ProfissionalDeleteView,
    ProfissionalListView,
    ProfissionalUpdateView,
)

app_name = "profissionais"

urlpatterns = [
    path("", ProfissionalListView.as_view(), name="profissional_list"),
    path("novo/", ProfissionalCreateView.as_view(), name="profissional_create"),
    path("<int:pk>/editar/", ProfissionalUpdateView.as_view(), name="profissional_update"),
    path("<int:pk>/excluir/", ProfissionalDeleteView.as_view(), name="profissional_delete"),
]
