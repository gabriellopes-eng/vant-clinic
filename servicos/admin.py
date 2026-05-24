from django.contrib import admin

from .models import ServicoEstetico


@admin.register(ServicoEstetico)
class ServicoEsteticoAdmin(admin.ModelAdmin):
	list_display = ("nome", "duracao_minutos", "preco", "ativo")
	search_fields = ("nome",)
