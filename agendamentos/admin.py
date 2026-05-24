from django.contrib import admin

from .models import Agendamento


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
	list_display = ("cliente", "profissional", "servico", "data_hora", "status")
	list_filter = ("status", "profissional", "servico")
	search_fields = ("cliente__nome", "profissional__nome", "servico__nome")
