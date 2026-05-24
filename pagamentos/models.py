from django.db import models

from agendamentos.models import Agendamento


class Pagamento(models.Model):
	class StatusPagamento(models.TextChoices):
		PENDENTE = "PENDENTE", "Pendente"
		PAGO = "PAGO", "Pago"

	agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE, related_name="pagamento")
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	status = models.CharField(max_length=10, choices=StatusPagamento.choices, default=StatusPagamento.PENDENTE)
	data_pagamento = models.DateField(null=True, blank=True)
	forma_pagamento = models.CharField(max_length=30, blank=True)
	criado_em = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-criado_em"]

	def __str__(self):
		return f"Pagamento {self.agendamento_id} - {self.status}"
