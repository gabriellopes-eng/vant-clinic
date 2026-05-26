from django import forms

from .models import Agendamento


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ["cliente", "profissional", "servico", "data_hora", "observacoes", "status"]
        labels = {
            "cliente": "Client",
            "profissional": "Professional",
            "servico": "Service",
            "data_hora": "Date and time",
            "observacoes": "Notes",
            "status": "Status",
        }
        widgets = {
            "data_hora": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
