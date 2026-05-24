from django.urls import path

from .views import RelatorioResumoView

app_name = "relatorios"

urlpatterns = [
    path("resumo/", RelatorioResumoView.as_view(), name="resumo"),
]
