from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "telefone", "email", "observacoes", "ativo"]
        labels = {
            "nome": "Name",
            "telefone": "Phone",
            "email": "Email",
            "observacoes": "Notes",
            "ativo": "Active",
        }
