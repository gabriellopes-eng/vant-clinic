from django.contrib import admin

from .models import Profissional


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
	list_display = ("nome", "especialidade", "telefone", "ativo")
	search_fields = ("nome", "especialidade", "telefone")
