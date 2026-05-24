from django import forms

from .models import ServicoEstetico


class ServicoEsteticoForm(forms.ModelForm):
    class Meta:
        model = ServicoEstetico
        fields = ["nome", "descricao", "duracao_minutos", "preco", "ativo"]
