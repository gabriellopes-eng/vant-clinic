from django.contrib import admin

from .models import Pagamento


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
	list_display = ("agendamento", "valor", "status", "data_pagamento", "forma_pagamento")
	list_filter = ("status", "forma_pagamento")
