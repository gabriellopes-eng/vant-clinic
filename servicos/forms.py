from django import forms

from .models import ServicoEstetico


class ServicoEsteticoForm(forms.ModelForm):
    class Meta:
        model = ServicoEstetico
        fields = ["nome", "descricao", "duracao_minutos", "preco", "ativo"]
        labels = {
            "nome": "Name",
            "descricao": "Description",
            "duracao_minutos": "Duration (minutes)",
            "preco": "Price",
            "ativo": "Active",
        }
