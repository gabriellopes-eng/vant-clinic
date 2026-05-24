from django.db import models

from clientes.models import Cliente
from profissionais.models import Profissional
from servicos.models import ServicoEstetico


class Agendamento(models.Model):
	class StatusAgendamento(models.TextChoices):
		AGENDADO = "AGENDADO", "Agendado"
		CANCELADO = "CANCELADO", "Cancelado"
		CONCLUIDO = "CONCLUIDO", "Concluido"

	cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="agendamentos")
	profissional = models.ForeignKey(Profissional, on_delete=models.PROTECT, related_name="agendamentos")
	servico = models.ForeignKey(ServicoEstetico, on_delete=models.PROTECT, related_name="agendamentos")
	data_hora = models.DateTimeField()
	observacoes = models.TextField(blank=True)
	status = models.CharField(max_length=10, choices=StatusAgendamento.choices, default=StatusAgendamento.AGENDADO)
	criado_em = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-data_hora"]

	def __str__(self):
		return f"{self.cliente} - {self.servico} ({self.data_hora:%d/%m/%Y %H:%M})"
