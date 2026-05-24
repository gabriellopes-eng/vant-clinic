from django import forms

from .models import Pagamento


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ["agendamento", "valor", "status", "data_pagamento", "forma_pagamento"]
        widgets = {
            "data_pagamento": forms.DateInput(attrs={"type": "date"}),
        }
